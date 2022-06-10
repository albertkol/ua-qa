# syntax=docker/dockerfile:1
FROM golang:1.18-alpine

RUN apk update && apk upgrade && apk add --no-cache bash git openssh make python3 py3-pip

#Accept input argument from docker-compose.yml
ARG SSH_PRIVATE_KEY

#Pass the content of the private key into the container
RUN mkdir /root/.ssh/
RUN echo "${SSH_PRIVATE_KEY}" > /root/.ssh/id_rsa

#Github requires a private key with strict permission settings
RUN chmod 600 /root/.ssh/id_rsa

#Add Github to known hosts
RUN touch /root/.ssh/known_hosts
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts


WORKDIR /Code
RUN git config --global --add url."git@github.com:".insteadOf "https://github.com/"
RUN git clone git@github.com:canonical/ua-contracts.git


WORKDIR /Code/ua-contracts
RUN make install

ENV CONTRACTS_URL="https://contracts.staging.canonical.com/"

WORKDIR /Code/ua_qa

RUN pip install pyyaml

COPY ./src /Code/ua_qa
COPY ./payloads /Code/ua_qa/payloads

CMD [ "python3", "app.py" ]