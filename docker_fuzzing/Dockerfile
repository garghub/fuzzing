FROM ubuntu:20.04 AS builder

RUN apt-get update && apt-get install -y git

FROM ubuntu:20.04
COPY --from=builder /usr/local /usr/local

RUN mkdir -p /docker_fuzzing/tools
WORKDIR /docker_fuzzing

COPY ./entrypoint.sh /docker_fuzzing/entrypoint.sh
COPY ./scripts /docker_fuzzing/scripts

RUN apt-get update && apt-get install -y wget
RUN wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
RUN dpkg -i packages-microsoft-prod.deb && rm packages-microsoft-prod.deb
RUN apt-get update && apt-get install -y apt-transport-https dotnet-sdk-6.0 unzip dos2unix

# APIFuzzer
RUN apt-get install -y gcc libcurl4-nss-dev python3-pip
RUN pip3 install APIFuzzer

# Kiterunner
RUN apt-get install -y golang-go
RUN wget -O /docker_fuzzing/tools/kiterunner-1.0.2.zip https://github.com/assetnote/kiterunner/archive/refs/tags/v1.0.2.zip && \
    unzip /docker_fuzzing/tools/kiterunner-1.0.2.zip -d /docker_fuzzing/tools && \
    rm /docker_fuzzing/tools/kiterunner-1.0.2.zip
RUN mkdir /docker_fuzzing/tools/kiterunner-1.0.2/kite && \
    wget -O /docker_fuzzing/tools/kiterunner-1.0.2/kite/routes-large.kite.tar.gz https://wordlists-cdn.assetnote.io/data/kiterunner/routes-large.kite.tar.gz && \
    tar -xzf /docker_fuzzing/tools/kiterunner-1.0.2/kite/routes-large.kite.tar.gz -C /docker_fuzzing/tools/kiterunner-1.0.2/kite && \
    rm /docker_fuzzing/tools/kiterunner-1.0.2/kite/routes-large.kite.tar.gz
RUN cd /docker_fuzzing/tools/kiterunner-1.0.2 && make build
RUN ln -s /docker_fuzzing/tools/kiterunner-1.0.2/dist/kr /usr/local/bin/Kiterunner

# RESTler
RUN wget -O /docker_fuzzing/tools/restler-fuzzer-9.2.4.zip https://github.com/microsoft/restler-fuzzer/archive/refs/tags/v9.2.4.zip && \
    unzip /docker_fuzzing/tools/restler-fuzzer-9.2.4.zip -d /docker_fuzzing/tools && \
    rm /docker_fuzzing/tools/restler-fuzzer-9.2.4.zip
RUN mkdir /docker_fuzzing/tools/restler-fuzzer-9.2.4/restler_bin
RUN python3 /docker_fuzzing/tools/restler-fuzzer-9.2.4/build-restler.py --dest_dir /docker_fuzzing/tools/restler-fuzzer-9.2.4/restler_bin
RUN ln -s /docker_fuzzing/tools/restler-fuzzer-9.2.4/restler_bin/restler/Restler /usr/local/bin/Restler

# Schemathesis
RUN pip3 install schemathesis

# tshark
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tshark

# JA4
RUN wget -O /docker_fuzzing/tools/ja4-0.18.4.zip https://github.com/FoxIO-LLC/ja4/archive/refs/tags/v0.18.4.zip && \
unzip /docker_fuzzing/tools/ja4-0.18.4.zip -d /docker_fuzzing/tools && \
rm /docker_fuzzing/tools/ja4-0.18.4.zip

RUN chmod +x /docker_fuzzing/entrypoint.sh
CMD ["./entrypoint.sh"]

# COPY ./requirements.txt /docker_fuzzing/requirements.txt
# RUN pip3 install --no-cache-dir --upgrade -r /docker_fuzzing/requirements.txt
# COPY ./funcs /docker_fuzzing/funcs