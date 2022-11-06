FROM golang:1.19.3-bullseye as build-env

ENV PACKAGES curl make git libc-dev bash gcc jq bc
RUN apt-get update && apt-get upgrade -y && \
  apt-get install -y $PACKAGES

WORKDIR /go/src/github.com/prometheus/

RUN git clone 'https://github.com/prometheus/prometheus.git'

WORKDIR /go/src/github.com/prometheus/prometheus/documentation/examples/remote_storage/remote_storage_adapter

RUN go build

FROM golang:1.19-bullseye as final

WORKDIR /

RUN apt-get update

# Copy over binaries from the build-env
COPY --from=build-env /go/src/github.com/prometheus/prometheus/documentation/examples/remote_storage/remote_storage_adapter/remote_storage_adapter /

COPY ./start.sh ./start.sh

ENTRYPOINT [ "./start.sh" ]