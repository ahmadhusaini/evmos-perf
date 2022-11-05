FROM golang:1.19.3-bullseye

COPY . .

WORKDIR /go/evmos

RUN apt-get update -y
RUN apt-get install git -y

RUN apt-get install jq -y
RUN apt-get install bc -y
RUN sed -i -e 's/\r$//' local_node.sh
#ENTRYPOINT [ "./local_node.sh" ]