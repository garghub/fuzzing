
# Payload Analysis of Adversaries’ Tooling: Automated Identification of Fuzzers  

This repository accompanies the paper *"Payload Analysis of Adversaries’ Tooling: Automated Identification of Fuzzers"*.

---

## Overview  
The repository includes:  
1. **Dataset**: Payloads generated during experimentation using APIFuzzer, Kiterunner, RESTler, and Schemathesis on the five APIs developed for this study.  
2. **Source Code**: Implementation of the combined deep learning and machine learning architecture for payload analysis and classification.  
3. **Trained Models**: Pre-trained models for replicating our classification results.  
4. **Supplementary Scripts**: Tools for data preprocessing, analysis, and visualization.  
5. **Docker Setup**: A containerized environment to execute the fuzzers on the provided APIs, enabling users to replicate or generate the dataset independently.  

---

## Purpose of the Docker Setup  
The Docker container is designed to streamline the execution of fuzzers against the five custom APIs developed for our study. This setup is particularly useful for:  
- **Reproducing Results**: Users can replicate the dataset used in the paper by executing the fuzzers with the provided scripts.  
- **Generating New Data**: The container allows users to regenerate the entire dataset or customize the fuzzing process for their own experimentation.  

The APIs, built following the OpenAPI specification, represent diverse scenarios, including CRUD operations, OAuth2 flows, and IoT interactions, making them ideal for evaluating fuzzing techniques.  

---

## How to Use the Docker Setup  

### Step 1: Build the Docker Image  
```bash
cd path/to/docker_fuzzing
docker buildx build --platform linux/amd64 -t image_fuzzing:1.0.0 .
```
_Note: Ensure to include the **.** (dot) at the end of the command._

### Step 2: Save and Load the Docker Image  
Save the image:
```bash
docker save -o image_fuzzing.img image_fuzzing:1.0.0
```
Load the saved image:
```bash
docker load -i path/to/docker_fuzzing/image_fuzzing.img
```

### Step 3: Run the Docker Container  
Run the container while mounting the data directory:
```bash
docker run -v path/to/docker_fuzzing/data:/docker_fuzzing/data --name container_fuzzing -d image_fuzzing:1.0.0
```
_e.g._  
```bash
docker run -v D:/ag/github/fuzzing/docker_fuzzing/data:/docker_fuzzing/data --name container_fuzzing -d image_fuzzing:1.0.0
```

### Step 4: Access the Docker Container  
Attach to the running container for executing bash commands:
```bash
docker exec -it container_fuzzing bash
```

---

## Capturing and Analyzing Network Traffic  

### Capturing Packets with TShark  
```bash
tshark -i [interface_name] -w /path/to/pcap
```
_e.g._  
```bash
tshark -i eth0 -w /docker_fuzzing/data/dump.pcap
```

### Analyzing Packets with JA4  
```bash
python3 /docker_fuzzing/tools/ja4-0.18.4/python/ja4.py [parameters]
```

---

## Running Fuzzers Iteratively  

### Bash Scripts for Iterative Execution  
The following scripts execute each fuzzer iteratively on the APIs:  
- **APIFuzzer**: `/docker_fuzzing/scripts/bash_script_to_run_APIFuzzer_Iteratively.sh`  
- **Kiterunner**: `/docker_fuzzing/scripts/bash_script_to_run_Kiterunner_Iteratively.sh`  
- **RESTler**: `/docker_fuzzing/scripts/bash_script_to_run_RESTler.sh`  
  _Note: RESTler provides an in-built time-setting functionality._  
- **Schemathesis**: `/docker_fuzzing/scripts/bash_script_to_run_Schemathesis_Iteratively.sh`  

---

For questions or issues, please refer to the documentation or contact us through the repository.  

---
