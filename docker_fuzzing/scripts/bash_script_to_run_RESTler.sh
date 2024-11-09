#!/bin/bash

# NOTE: Different from other fuzzers, RESTler provides an in-built functionality to set the time, and will continue to execute till the time expires
duration=$((1))
# Uncomment below to set duration for 7 * 24 hours (in hours)
# duration=$((7 * 24))

cd /docker_fuzzing/data/api_simple_items/RESTler
Restler compile --api_spec /docker_fuzzing/data/api_simple_items/api_simple_items.json
Restler fuzz --grammar_file /docker_fuzzing/data/api_simple_items/RESTler/Compile/grammar.py --dictionary_file /docker_fuzzing/data/api_simple_items/RESTler/Compile/dict.json --settings /docker_fuzzing/data/api_simple_items/RESTler/Compile/engine_settings.json --no_ssl --time_budget $duration

cd /docker_fuzzing/data/api_iot/RESTler
Restler compile --api_spec /docker_fuzzing/data/api_iot/api_iot.json
Restler fuzz --grammar_file /docker_fuzzing/data/api_iot/RESTler/Compile/grammar.py --dictionary_file /docker_fuzzing/data/api_iot/RESTler/Compile/dict.json --settings /docker_fuzzing/data/api_iot/RESTler/Compile/engine_settings.json --no_ssl --time_budget $duration

cd /docker_fuzzing/data/api_oauth2_application/RESTler
Restler compile --api_spec /docker_fuzzing/data/api_oauth2_application/api_oauth2_application.json
Restler fuzz --grammar_file /docker_fuzzing/data/api_oauth2_application/RESTler/Compile/grammar.py --dictionary_file /docker_fuzzing/data/api_oauth2_application/RESTler/Compile/dict.json --settings /docker_fuzzing/data/api_oauth2_application/RESTler/Compile/engine_settings.json --no_ssl --time_budget $duration

cd /docker_fuzzing/data/api_oauth2_password/RESTler
Restler compile --api_spec /docker_fuzzing/data/api_oauth2_password/api_oauth2_password.json
Restler fuzz --grammar_file /docker_fuzzing/data/api_oauth2_password/RESTler/Compile/grammar.py --dictionary_file /docker_fuzzing/data/api_oauth2_password/RESTler/Compile/dict.json --settings /docker_fuzzing/data/api_oauth2_password/RESTler/Compile/engine_settings.json --no_ssl --time_budget $duration

cd /docker_fuzzing/data/api_petstore/RESTler
Restler compile --api_spec /docker_fuzzing/data/api_oauth2_password/api_oauth2_password.json
Restler fuzz --grammar_file /docker_fuzzing/data/api_petstore/RESTler/Compile/grammar.py --dictionary_file /docker_fuzzing/data/api_petstore/RESTler/Compile/dict.json --settings /docker_fuzzing/data/api_petstore/RESTler/Compile/engine_settings.json --no_ssl --time_budget $duration

echo "Timer set has expired. Exiting."
