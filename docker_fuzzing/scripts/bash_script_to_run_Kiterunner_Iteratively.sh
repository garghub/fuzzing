#!/bin/bash
duration=$((60))
# Uncomment below to set duration for 7 * 24 hours (in seconds)
# duration=$((7 * 24 * 60 * 60))
start_time=$(date +%s)

run_count=0
# Commands to run repeatedly
while [[ $(($(date +%s) - start_time)) -lt $duration ]]; do
    run_count=$((run_count + 1))  # Increment run count
    echo "Running commands..."
    
    cd /docker_fuzzing/data/api_simple_items/Kiterunner
    Kiterunner scan https://virtserver.swaggerhub.com/AAYUSHGARGBU/api_simple_items/1.0.0 -w /docker_fuzzing/tools/kiterunner-1.0.2/kite/routes-large.kite -o json -v debug -x 1 --profile-name /docker_fuzzing/data/api_simple_items/Kiterunner/output_kiterunner_${run_count}.json 2>&1 | tee -a /docker_fuzzing/data/api_simple_items/Kiterunner/logs_all_${run_count}.txt
    
    cd /docker_fuzzing/data/api_iot/Kiterunner
    Kiterunner scan https://virtserver.swaggerhub.com/AAYUSHGARGBU/api_iot/1.0.0 -w /docker_fuzzing/tools/kiterunner-1.0.2/kite/routes-large.kite -o json -v debug -x 1 --profile-name /docker_fuzzing/data/api_iot/Kiterunner/output_kiterunner_${run_count}.json 2>&1 | tee -a /docker_fuzzing/data/api_iot/Kiterunner/logs_all_${run_count}.txt
    
    cd /docker_fuzzing/data/api_oauth2_application/Kiterunner
    Kiterunner scan https://virtserver.swaggerhub.com/AAYUSHGARGBU/api_oauth2_application/1.0.0 -w /docker_fuzzing/tools/kiterunner-1.0.2/kite/routes-large.kite -o json -v debug -x 1 --profile-name /docker_fuzzing/data/api_oauth2_application/Kiterunner/output_kiterunner_${run_count}.json 2>&1 | tee -a /docker_fuzzing/data/api_oauth2_application/Kiterunner/logs_all_${run_count}.txt
    
    cd /docker_fuzzing/data/api_oauth2_password/Kiterunner
    Kiterunner scan https://virtserver.swaggerhub.com/AAYUSHGARGBU/api_oauth2_password/1.0.0 -w /docker_fuzzing/tools/kiterunner-1.0.2/kite/routes-large.kite -o json -v debug -x 1 --profile-name /docker_fuzzing/data/api_oauth2_password/Kiterunner/output_kiterunner_${run_count}.json 2>&1 | tee -a /docker_fuzzing/data/api_oauth2_password/Kiterunner/logs_all_${run_count}.txt
    
    cd /docker_fuzzing/data/api_petstore/Kiterunner
    Kiterunner scan https://virtserver.swaggerhub.com/AAYUSHGARGBU/api_petstore/1.0.0 -w /docker_fuzzing/tools/kiterunner-1.0.2/kite/routes-large.kite -o json -v debug -x 1 --profile-name /docker_fuzzing/data/api_petstore/Kiterunner/output_kiterunner_${run_count}.json 2>&1 | tee -a /docker_fuzzing/data/api_petstore/Kiterunner/logs_all_${run_count}.txt
    
    # Add more commands as needed
    echo "Commands completed. Restarting after a short delay..."
    sleep 10  # Sleep for 10 seconds before restarting the commands
done
echo "Timer set has expired. Exiting."
