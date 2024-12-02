#!/usr/bin/env python
# coding: utf-8

# For only obtaining prediction from already trained model

import pandas as pd
import keras_nlp
import os
import pickle
from tensorflow import keras
import tensorflow.keras.backend as K
import numpy as np
from pandas import Series
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn import metrics
import tensorflow as tf
import time
import uuid
import re
from urllib.parse import urlparse, parse_qs
import zipfile
import json
import datetime
from io import BytesIO
from api.models import StatusCodeEnum
from huggingface_hub import snapshot_download

# STR_UUID = "9f6e9e21-9326-41ec-aab1-086556f4ad7c"

NUM_BEAMS = 1
INDEX_LAYER = 1
INDEX_LAYER_FOR_WEIGHTS = 3
INDEX_W = 7

KEYWORD_CHECK_FOR_APIFUZZER = "APIFuzzer" #1
KEYWORD_CHECK_FOR_KITERUNNER = "Kiterunner" #2
KEYWORD_CHECK_FOR_RESTLER = "RESTler" #3
KEYWORD_CHECK_FOR_SCHEMATHESIS = "Schemathesis" #4

COLUMN_CSV_SEQUENCE = "payloads"
STR_PREFIX_TO_SS_URL = "https : / / domain_name / user_name / api_name / api_ver / <FUZZ_HERE> FUZZED_TO "
STR_INVALID_PAYLOAD = "Provided payload-URL has been found invalid and cannot be parsed."

NAME_DIR_INPUT_CSV = "input_fuzzer_identification"
NAME_ML_DATASET_CSV = COLUMN_CSV_SEQUENCE + ".csv"

PATH_HUGGINGFACE = "listlazarus/slaf"
NAME_MODEL = 'seq2seq_transformer'
NAME_CLASSIFIER_FILE = 'rf_classifier.pkl'

def load_interim_data(file_path):
    # print("loading saved file at", file_path)
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data

def load_test_data(path_input, request_result):
    df_csv_test = None
    # Iterate over the directory structure
    full_path = "" # os.path.join(path_input, NAME_DIR_INPUT_CSV, NAME_ML_DATASET_CSV)
    for root, dirs, files in os.walk(path_input):
        # Check if the directory contains the required CSV file
        if NAME_ML_DATASET_CSV in files and NAME_DIR_INPUT_CSV in root:
            full_path = os.path.join(root, NAME_ML_DATASET_CSV)

    if os.path.exists(full_path) == False:
        status_msg = NAME_ML_DATASET_CSV + " file not found in " + NAME_DIR_INPUT_CSV + \
            " directory within .zip file!"
        request_result.status.status_code = StatusCodeEnum.FAILED
        request_result.status.status_msg = status_msg
        return df_csv_test, request_result

    df_csv_test = pd.read_csv(full_path)
    # print("Total datapoints:", len(df_csv_test.index))
    
    if df_csv_test.dropna().empty:
        status_msg = "Empty " + NAME_ML_DATASET_CSV + " file found in " + NAME_DIR_INPUT_CSV + " directory within .zip file!"
        request_result.status.status_code = StatusCodeEnum.FAILED
        request_result.status.status_msg = status_msg
        return df_csv_test, request_result
    
    if COLUMN_CSV_SEQUENCE not in df_csv_test.columns:
        status_msg = "Column '" + COLUMN_CSV_SEQUENCE  + "' not found in " + NAME_ML_DATASET_CSV + " file!"
        request_result.status.status_code = StatusCodeEnum.FAILED
        request_result.status.status_msg = status_msg
        return df_csv_test, request_result

    return df_csv_test, request_result

def process_url(url):
    # Define the reserved special characters in a URL
    reserved_special_chars = ":/?#[]@!$&'()*+,;="
    
    # Check if the URL is valid
    try:
        result = urlparse(url)
        if not all([result.scheme, result.netloc]):
            return None
    except:
        return None
    
    # Replace reserved special characters with <space>special character<space>
    def replacer(match):
        char = match.group(0)
        return f' {char} '

    processed_url = re.sub(r'[' + re.escape(reserved_special_chars) + ']', replacer, url)
    words = processed_url.split()
    return processed_url

def get_input_sequences(str_test_datapoint):
    inp_seq = process_url(str_test_datapoint)
    if inp_seq is None:
        return None
    inp_seq = STR_PREFIX_TO_SS_URL + inp_seq.replace("\"","")
    inp_seq = re.sub(r'\s+', ' ', inp_seq)
    lst_sequences = [inp_seq] * 2
    return lst_sequences

def get_specific_transformer(PATH_TRANSFORMER):
    # print('Loading transformer from', PATH_TRANSFORMER)
    # print('Loading transformer...')
    transformer = keras.models.load_model(PATH_TRANSFORMER)
    return transformer

def get_specific_classifier(PATH_CLASSIFIER):
    # print('Loading classifier from', PATH_CLASSIFIER)
    # print('Loading classifier...')
    with open(PATH_CLASSIFIER, 'rb') as f:
        clf = pickle.load(f)
    return clf

def hard_sigmoid(x):
    return np.maximum(0, np.minimum(1, 0.2*x+0.5))

def evaluate(model, nodes_to_evaluate, x, y=None):
    symb_inputs = (model._feed_inputs)
    f = K.function(symb_inputs, nodes_to_evaluate)
    x_ = x
    return f(x_)

def get_activations_single_layer(model, x, layer_name=None):
    nodes = [layer.output for layer in model.layers if layer.name == layer_name or layer_name is None]
    # we process the placeholders later (Inputs node in Keras). Because there's a bug in Tensorflow.
    input_layer_outputs, layer_outputs = [], []
    [input_layer_outputs.append(node) if 'input_' in node.name else \
     layer_outputs.append(node) for node in nodes]
    activations = evaluate(model, layer_outputs, x, y=None)
    activations_dict = dict(zip([output.name for output in layer_outputs], activations))
    activations_inputs_dict = dict(zip([output.name for output in input_layer_outputs], x))
    result = activations_inputs_dict.copy()
    result.update(activations_dict)
    ret_list = np.squeeze(list(result.values())[0])
    return ret_list

def layerName(model, layer):
    layerNames = [layer.name for layer in model.layers]
    return layerNames[layer]

def cal_hidden_state(model, test):
    lenTest = len(test[0])
    layer_name = layerName(model, INDEX_LAYER)
    acx = get_activations_single_layer(model, test, layer_name)
    W = model.layers[INDEX_LAYER_FOR_WEIGHTS].get_weights()[INDEX_W]
    f_t = []
    for i in range(0, lenTest):
        f_gate = hard_sigmoid(np.dot(acx[i, :], W))
        f_t.append(f_gate)
    return f_t

def get_embeddings(transformer, lst_input, inp_tokenizer, MAX_SEQUENCE_LENGTH):
    encoder_input_tokens = \
    inp_tokenizer(lst_input).to_tensor(shape=(None, MAX_SEQUENCE_LENGTH))
    f_t = cal_hidden_state(transformer, [encoder_input_tokens, encoder_input_tokens])
    return f_t

####################

def get_class_names_from_labels(lst):
    lst_ret = []
    for label in lst:
        if label == 1:
            lst_ret.append(KEYWORD_CHECK_FOR_APIFUZZER)
        elif label == 4:
            lst_ret.append(KEYWORD_CHECK_FOR_SCHEMATHESIS)
        elif label == 2:
            lst_ret.append(KEYWORD_CHECK_FOR_KITERUNNER)
        elif label == 3:
            lst_ret.append(KEYWORD_CHECK_FOR_RESTLER)
    return lst_ret

def get_classifier_predictions(lst_input, transformer, inp_tokenizer, clf, MAX_SEQUENCE_LENGTH):
    embeddings = get_embeddings(transformer, lst_input, inp_tokenizer, MAX_SEQUENCE_LENGTH)
    lst_predicted_label = clf.predict(embeddings)
    return lst_predicted_label

def get_models_predictions(num_beams, lst_sequences, inp_tokenizer, transformer, clf, MAX_SEQUENCE_LENGTH):
    lst_classifier_predictions = get_classifier_predictions(lst_sequences, transformer, inp_tokenizer, clf, MAX_SEQUENCE_LENGTH)
    return lst_classifier_predictions

def get_fuzzer_repository(str_fuzzer_name):
    str_fuzzer_repository = ""
    if str_fuzzer_name == KEYWORD_CHECK_FOR_APIFUZZER:
        str_fuzzer_repository = "https://pypi.org/project/APIFuzzer"
    elif str_fuzzer_name == KEYWORD_CHECK_FOR_KITERUNNER:
        str_fuzzer_repository = "https://github.com/assetnote/kiterunner"
    elif str_fuzzer_name == KEYWORD_CHECK_FOR_RESTLER:
        str_fuzzer_repository =  "https://github.com/microsoft/restler-fuzzer"
    elif str_fuzzer_name == KEYWORD_CHECK_FOR_SCHEMATHESIS:
        str_fuzzer_repository = "https://github.com/schemathesis/schemathesis"
    return str_fuzzer_repository

def get_fuzzer_description(str_fuzzer_name):
    str_fuzzer_description = ""
    if str_fuzzer_name == KEYWORD_CHECK_FOR_APIFUZZER:
        str_fuzzer_description = "APIFuzzer (HTTP API Testing Framework) is a robust framework designed" + \
        " to automate the discovery and exploitation of vulnerabilities in web applications through input" + \
        " fuzzing. It supports extensive HTTP request testing, using random mutations to simulate " + \
        " real-world attacks that can disrupt application stability and security."
    elif str_fuzzer_name == KEYWORD_CHECK_FOR_KITERUNNER:
        str_fuzzer_description = "Kiterunner (API Route Testing Framework) targets API routes overlooked" + \
        " by traditional tools, using detailed Swagger and OpenAPI datasets to brute-force endpoints and" + \
        " expose significant security flaws. Its precise attacks can uncover unauthorized access and data" + \
        " breaches in modern applications."
    elif str_fuzzer_name == KEYWORD_CHECK_FOR_RESTLER:
        str_fuzzer_description =  "RESTler (Stateful REST API Fuzzing Tool) from Microsoft Research" + \
        " systematically analyzes and exploits REST APIs' vulnerabilities through intelligent fuzzing. " + \
        "It sequences API calls to exploit deep service states, posing severe security risks for cloud" + \
        " services not rigorously tested against advanced attack strategies."
    elif str_fuzzer_name == KEYWORD_CHECK_FOR_SCHEMATHESIS:
        str_fuzzer_description = "Schemathesis (Advanced API Testing Framework) leverages API specs to " + \
        "automatically generate and execute tests that identify and exploit vulnerabilities, ensuring" + \
        " thorough exposure of potential security loopholes in APIs. Its broad testing approach can lead" + \
        " to substantial disruptions and compromises in system integrity."
    return str_fuzzer_description

def load_or_download_model():
    PATH_ML_INPUT_DIR = os.path.join(os.environ["HF_HOME"], "models")
    PATH_MAX_SEQUENCE_LENGTH = os.path.join(PATH_ML_INPUT_DIR, 'MAX_SEQUENCE_LENGTH.pkl')
    PATH_INP_VOCAB = os.path.join(PATH_ML_INPUT_DIR, 'inp_vocab.pkl')
    PATH_TRANSFORMER = os.path.join(PATH_ML_INPUT_DIR, NAME_MODEL)
    PATH_CLASSIFIER = os.path.join(PATH_ML_INPUT_DIR, NAME_CLASSIFIER_FILE)

    if os.path.exists(PATH_MAX_SEQUENCE_LENGTH) == False or \
        os.path.exists(PATH_INP_VOCAB) == False or \
            os.path.exists(PATH_TRANSFORMER) == False or \
                os.path.exists(PATH_CLASSIFIER) == False:
        print("Model files not found at", PATH_ML_INPUT_DIR, ". Downloading the files...")
        if os.path.exists(PATH_ML_INPUT_DIR) == False:
            os.makedirs(PATH_ML_INPUT_DIR)
        snapshot_download(repo_id=PATH_HUGGINGFACE, ignore_patterns=["*.gitattributes"], \
                        local_dir=PATH_ML_INPUT_DIR)
    else:
        print("Model files already found at", PATH_ML_INPUT_DIR, ". Loading from local storage...")
    
    return PATH_MAX_SEQUENCE_LENGTH, PATH_INP_VOCAB, PATH_TRANSFORMER, PATH_CLASSIFIER
    
def fuzzer_identification(path_input, request_result):
    results = []

    try:
        PATH_MAX_SEQUENCE_LENGTH, PATH_INP_VOCAB, PATH_TRANSFORMER, \
            PATH_CLASSIFIER = load_or_download_model()
        
        # print("\nLooking for saved model, and parameters...")
        if os.path.exists(PATH_MAX_SEQUENCE_LENGTH) == False or \
            os.path.exists(PATH_INP_VOCAB) == False or \
                os.path.exists(PATH_TRANSFORMER) == False or \
                    os.path.exists(PATH_CLASSIFIER) == False:
            status_msg = "Mandatory files not found!"
            status_msg = status_msg + " Please ensure the following files are available:"
            status_msg = status_msg + " 1)" + PATH_MAX_SEQUENCE_LENGTH
            status_msg = status_msg + " 2)" + PATH_INP_VOCAB
            status_msg = status_msg + " 3)" + PATH_TRANSFORMER
            status_msg = status_msg + " 4)" + PATH_CLASSIFIER
            request_result.status.status_code = StatusCodeEnum.FAILED
            request_result.status.status_msg = status_msg
            return results, request_result
            
        df_csv_test, request_result = load_test_data(path_input, request_result)
        if request_result.status.status_code == StatusCodeEnum.FAILED:
            return results, request_result

        # print("Loading parameters...")
        MAX_SEQUENCE_LENGTH = load_interim_data(PATH_MAX_SEQUENCE_LENGTH)
        inp_vocab = load_interim_data(PATH_INP_VOCAB)

        # print("Loading models...")
        transformer = get_specific_transformer(PATH_TRANSFORMER)
        clf = get_specific_classifier(PATH_CLASSIFIER)

        # print("Configuring tokenizers using saved parameters...")
        inp_tokenizer = keras_nlp.tokenizers.WordPieceTokenizer(vocabulary=inp_vocab, lowercase=False)

        for index, row in df_csv_test.iterrows():
            str_test_datapoint = row[COLUMN_CSV_SEQUENCE]
            lst_sequences = get_input_sequences(str_test_datapoint)
            str_user_input = str_test_datapoint
            str_prediction = ""
            str_repository = ""
            if lst_sequences is None:
                str_description = STR_INVALID_PAYLOAD
            else:
                lst_classifier_predictions = \
                    get_models_predictions(NUM_BEAMS, lst_sequences, inp_tokenizer, transformer, clf, MAX_SEQUENCE_LENGTH)
                lst_predicted_class_names = get_class_names_from_labels(lst_classifier_predictions)
                predicted_class_name = lst_predicted_class_names[0]
                str_prediction = predicted_class_name
                str_description = get_fuzzer_description(predicted_class_name)
                str_repository = get_fuzzer_repository(predicted_class_name)
            results.append({
                "payload": str_user_input,
                "identified_fuzzer": str_prediction,
                "fuzzer_description": str_description,
                "fuzzer_repository": str_repository
            })

        return results, request_result
        
    except Exception as exc:
        request_result.status.status_code = StatusCodeEnum.FAILED
        request_result.status.status_msg = f"An unexpected error occurred: {exc}"
        return results, request_result