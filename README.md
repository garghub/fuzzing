(Below are the commands to execute)

`cd path/to/docker_fuzzing`

`docker buildx build --platform linux/amd64 -t image_fuzzing:1.0.0 .`

(Please note that above command has a . (dot) in the end, which is also to be included)

(Below command will save the docker image in the current directory)
`docker save -o image_fuzzing.img image_fuzzing:1.0.0`

(Below command loads the saved image)

`docker load -i path/to/docker_fuzzing/image_fuzzing.img`

(Below command will run the docker container and will keep it running)

`docker run -v path/to/docker_fuzzing/data:/docker_fuzzing/data --name container_fuzzing -d image_fuzzing:1.0.0`

(e.g.)

`docker run -v D:/ag/github/fuzzing/docker_fuzzing/data:/docker_fuzzing/data --name container_fuzzing -d image_fuzzing:1.0.0`

---

(Below command is to be attached to the running docker container and enables execution of bash commands which are followed)
`docker exec -it container_fuzzing bash`

---

(Below command is to be execute tshark, capture packets and generate pcap file)

`tshark -i [interface_name] -w /path/to/pcap`

(e.g.)

`tshark -i eth0 -w /docker_fuzzing/data/dump.pcap`

(Below command is to be execute JA4 to analyze further)

`python3 /docker_fuzzing/tools/ja4-0.18.4/python/ja4.py [parameters]`

---

(Below scripts are to execute the fuzzers iteratively)

(Please note that RESTler (different from other fuzzers) provides an in-built functionality to set the time)

(RESTler will continue to execute till the set time expires)

`/docker_fuzzing/scripts/bash_script_to_run_APIFuzzer_Iteratively.sh`

`/docker_fuzzing/scripts/bash_script_to_run_Kiterunner_Iteratively.sh`

`/docker_fuzzing/scripts/bash_script_to_run_RESTler.sh`

`/docker_fuzzing/scripts/bash_script_to_run_Schemathesis_Iteratively.sh`
