#!/usr/bin/python
"""Main proxy module."""

DEFAULT_ARCHIVEI_ENDPOINT = getenv('ARCHIVEI_PORT', 'tcp://127.0.0.1:8080').replace('tcp', 'http')
ARCHIVEI_ENDPOINT = getenv('ARCHIVEI_ENDPOINT', DEFAULT_ARCHIVEI_ENDPOINT)
DEFAULT_METADATA_ENDPOINT = getenv('METADATA_PORT', 'tcp://127.0.0.1:8121').replace('tcp', 'http')
METADATA_ENDPOINT = getenv('METADATA_ENDPOINT', DEFAULT_METADATA_ENDPOINT)
METADATA_CONNECT_ATTEMPTS = 40
METADATA_WAIT = 3

DEFAULT_NGINX_X_ACCEL = getenv('NGINX_ACCEL', 'False')
NGINX_X_ACCEL = bool(DEFAULT_NGINX_X_ACCEL)

def try_meta_connect(attempts=0):
    """Try to connect to the metadata service see if its there."""
    try:
        ret = requests.get(METADATA_STATUS_URL.encode('utf-8'))
        if ret.status_code != 200:
            raise Exception('try_meta_connect: {0}\n'.format(ret.status_code))
    # pylint: disable=broad-except
    except Exception as ex:
        # pylint: enable=broad-except
        if attempts < METADATA_CONNECT_ATTEMPTS:
            sleep(METADATA_WAIT)
            attempts += 1
            try_meta_connect(attempts)
        else:
            raise ex
