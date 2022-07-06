#!/usr/bin/with-contenv bashio

LISTEN_IP_IN=$(bashio::config 'listen_ip')
LISTEN_PORT_IN=$(bashio::config 'listen_port')
SOURCE_PORT_IN=$(bashio::config 'source_port')

if [[ -z "${LISTEN_IP-}" ]]
then
  export LISTEN_IP=$LISTEN_IP_IN
fi

if [[ -z "${LISTEN_PORT-}" ]]
then
  export LISTEN_PORT=$LISTEN_PORT_IN
fi

if [[ -z "${SOURCE_PORT-}" ]]
then
  export SOURCE_PORT=$SOURCE_PORT_IN
fi

python3 -u main.py
