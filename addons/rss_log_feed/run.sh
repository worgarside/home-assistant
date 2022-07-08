#!/usr/bin/with-contenv bashio

LOG_TTL_IN=$(bashio::config 'log_ttl')

if [[ -z "${LOG_TTL-}" ]]
then
  export LOG_TTL=$LOG_TTL_IN
fi


python3 -u main.py
