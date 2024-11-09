#!/bin/bash
duration=$((60))
# Uncomment below to set duration for 7 * 24 hours (in seconds)
# duration=$((7 * 24 * 60 * 60))
start_time=$(date +%s)
# Initialize run count (i have run it once so initializing accordingly, normally it should be run_count=0)
run_count=0
# Commands to run repeatedly
while [[ $(($(date +%s) - start_time)) -lt $duration ]]; do
    run_count=$((run_count + 1))  # Increment run count
    echo "Running commands..."

    cd /docker_fuzzing/data/api_simple_items/APIFuzzer
    APIFuzzer -s /docker_fuzzing/data/api_simple_items/api_simple_items.json -u https://virtserver.swaggerhub.com/ -r /docker_fuzzing/data/api_simple_items/APIFuzzer/ -t /docker_fuzzing/data/api_simple_items/APIFuzzer/test_results_junit_${run_count}.xml --log debug | tee -a /docker_fuzzing/data/api_simple_items/APIFuzzer/logs_all_${run_count}.txt

    cd /docker_fuzzing/data/api_iot/APIFuzzer
    APIFuzzer -s /docker_fuzzing/data/api_iot/api_iot.json -u https://virtserver.swaggerhub.com/ -r /docker_fuzzing/data/api_iot/APIFuzzer/ -t /docker_fuzzing/data/api_iot/APIFuzzer/test_results_junit_${run_count}.xml --log debug | tee -a /docker_fuzzing/data/api_iot/APIFuzzer/logs_all_${run_count}.txt

    cd /docker_fuzzing/data/api_oauth2_application/APIFuzzer
    APIFuzzer -s /docker_fuzzing/data/api_oauth2_application/api_oauth2_application.json -u https://virtserver.swaggerhub.com/ -r /docker_fuzzing/data/api_oauth2_application/APIFuzzer/ -t /docker_fuzzing/data/api_oauth2_application/APIFuzzer/test_results_junit_${run_count}.xml --log debug | tee -a /docker_fuzzing/data/api_oauth2_application/APIFuzzer/logs_all_${run_count}.txt

    cd /docker_fuzzing/data/api_oauth2_password/APIFuzzer
    APIFuzzer -s /docker_fuzzing/data/api_oauth2_password/api_oauth2_password.json -u https://virtserver.swaggerhub.com/ -r /docker_fuzzing/data/api_oauth2_password/APIFuzzer/ -t /docker_fuzzing/data/api_oauth2_password/APIFuzzer/test_results_junit_${run_count}.xml --log debug | tee -a /docker_fuzzing/data/api_oauth2_password/APIFuzzer/logs_all_${run_count}.txt

    cd /docker_fuzzing/data/api_petstore/APIFuzzer
    APIFuzzer -s /docker_fuzzing/data/api_petstore/api_petstore.json -u https://virtserver.swaggerhub.com/ -r /docker_fuzzing/data/api_petstore/APIFuzzer/ -t /docker_fuzzing/data/api_petstore/APIFuzzer/test_results_junit_${run_count}.xml --log debug | tee -a /docker_fuzzing/data/api_petstore/APIFuzzer/logs_all_${run_count}.txt

    # Add more commands as needed
    echo "Commands completed. Restarting after a short delay..."
    sleep 60  # Sleep for 60 seconds before restarting the commands
done
echo "Timer set has expired. Exiting."
