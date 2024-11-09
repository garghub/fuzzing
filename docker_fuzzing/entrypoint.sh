#!/bin/bash
set -e

dos2unix /docker_fuzzing/scripts/bash_script_to_run_APIFuzzer_Iteratively.sh
chmod +x /docker_fuzzing/scripts/bash_script_to_run_APIFuzzer_Iteratively.sh

dos2unix /docker_fuzzing/scripts/bash_script_to_run_Kiterunner_Iteratively.sh
chmod +x /docker_fuzzing/scripts/bash_script_to_run_Kiterunner_Iteratively.sh

dos2unix /docker_fuzzing/scripts/bash_script_to_run_RESTler.sh
chmod +x /docker_fuzzing/scripts/bash_script_to_run_RESTler.sh

dos2unix /docker_fuzzing/scripts/bash_script_to_run_Schemathesis_Iteratively.sh
chmod +x /docker_fuzzing/scripts/bash_script_to_run_Schemathesis_Iteratively.sh

# Prevent the container from exiting
while true; do
    sleep 3600 # Sleeps for 1 hour
done