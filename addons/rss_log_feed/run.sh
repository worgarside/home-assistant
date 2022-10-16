#!/usr/bin/with-contenv bashio

LOG_TTL_IN=$(bashio::config 'log_ttl')
SFTP_HOSTNAME_IN=$(bashio::config 'sftp_hostname')
SFTP_USERNAME_IN=$(bashio::config 'sftp_username')
SFTP_KEY_FILEPATH_IN=$(bashio::config 'sftp_key_filepath')

if [[ -z "${LOG_TTL-}" ]]
then
  export LOG_TTL=$LOG_TTL_IN
fi

if [[ -z "${SFTP_HOSTNAME-}" ]]
then
  export SFTP_HOSTNAME=$SFTP_HOSTNAME_IN
fi

if [[ -z "${SFTP_USERNAME-}" ]]
then
  export SFTP_USERNAME=$SFTP_USERNAME_IN
fi

if [[ -z "${SFTP_KEY_FILEPATH-}" ]]
then
  export SFTP_KEY_FILEPATH=$SFTP_KEY_FILEPATH_IN
fi

python3 -u main.py
