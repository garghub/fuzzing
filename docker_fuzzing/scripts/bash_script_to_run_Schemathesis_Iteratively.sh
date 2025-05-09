#!/bin/bash
duration=$((60))
# Uncomment below to set duration for 7 * 24 hours (in seconds)
# duration=$((7 * 24 * 60 * 60))
start_time=$(date +%s)

run_count=4843
# Commands to run repeatedly
while [[ $(($(date +%s) - start_time)) -lt $duration ]]; do
    run_count=$((run_count + 1))  # Increment run count
    echo "Running commands..."
    
    cd /docker_fuzzing/data/api_simple_items/Schemathesis
    schemathesis run /docker_fuzzing/data/api_simple_items/api_simple_items.json -c all -D all -t all --validate-schema True -b https://virtserver.swaggerhub.com/AAYUSHGARGBU/api_simple_items/1.0.0 --debug-output-file /docker_fuzzing/data/api_simple_items/Schemathesis/debug_output_file_${run_count}.json --show-trace | tee -a /docker_fuzzing/data/api_simple_items/Schemathesis/logs_all_${run_count}.txt
    
    cd /docker_fuzzing/data/api_iot/Schemathesis
    schemathesis run /docker_fuzzing/data/api_iot/api_iot.json -c all -D all -t all --validate-schema True -b https://virtserver.swaggerhub.com/AAYUSHGARGBU/api_iot/1.0.0 --debug-output-file /docker_fuzzing/data/api_iot/Schemathesis/debug_output_file_${run_count}.json --show-trace | tee -a /docker_fuzzing/data/api_iot/Schemathesis/logs_all_${run_count}.txt
    
    cd /docker_fuzzing/data/api_oauth2_application/Schemathesis
    schemathesis run /docker_fuzzing/data/api_oauth2_application/api_oauth2_application.json -c all -D all -t all --validate-schema True -b https://virtserver.swaggerhub.com/AAYUSHGARGBU/api_oauth2_application/1.0.0 --debug-output-file /docker_fuzzing/data/api_oauth2_application/Schemathesis/debug_output_file_${run_count}.json --show-trace | tee -a /docker_fuzzing/data/api_oauth2_application/Schemathesis/logs_all_${run_count}.txt
    
    cd /docker_fuzzing/data/api_oauth2_password/Schemathesis
    schemathesis run /docker_fuzzing/data/api_oauth2_password/api_oauth2_password.json -c all -D all -t all --validate-schema True -b https://virtserver.swaggerhub.com/AAYUSHGARGBU/api_oauth2_password/1.0.0 --debug-output-file /docker_fuzzing/data/api_oauth2_password/Schemathesis/debug_output_file_${run_count}.json --show-trace | tee -a /docker_fuzzing/data/api_oauth2_password/Schemathesis/logs_all_${run_count}.txt
    
    cd /docker_fuzzing/data/api_petstore/Schemathesis
    schemathesis run /docker_fuzzing/data/api_petstore/api_petstore.json -c all -D all -t all --validate-schema True -b https://virtserver.swaggerhub.com/AAYUSHGARGBU/api_petstore/1.0.0 --debug-output-file /docker_fuzzing/data/api_petstore/Schemathesis/debug_output_file_${run_count}.json --show-trace | tee -a /docker_fuzzing/data/api_petstore/Schemathesis/logs_all_${run_count}.txt
    
    # Add more commands as needed
    echo "Commands completed. Restarting after a short delay..."
    sleep 10  # Sleep for 10 seconds before restarting the commands
done
echo "Timer set has expired. Exiting."
