#!/usr/bin/with-contenv bashio

LISTEN_IP_IN=$(bashio::config 'listen_ip')
LISTEN_PORT_IN=$(bashio::config 'listen_port')
SOURCE_PORT_IN=$(bashio::config 'source_port')
YAS_209_IP_IN=$(bashio::config 'yas_209_ip')
SFTP_HOSTNAME_IN=$(bashio::config 'sftp_hostname')
SFTP_USERNAME_IN=$(bashio::config 'sftp_username')
SFTP_KEY_FILEPATH_IN=$(bashio::config 'sftp_key_filepath')

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

if [[ -z "${YAS_209_IP-}" ]]
then
  export YAS_209_IP=$YAS_209_IP_IN
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
