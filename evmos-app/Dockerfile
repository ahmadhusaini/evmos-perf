FROM golang:1.19.3-bullseye

RUN apt-get update -y && apt-get install -y \
  git \
  jq \
  bc


WORKDIR /app

RUN git clone 'https://github.com/evmos/evmos.git'

COPY local_node.sh /app/evmos

WORKDIR /app/evmos

# RUN sed -i '$s/$/ --metrics/' local_node.sh

ENTRYPOINT [ "./local_node.sh" ]