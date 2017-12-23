#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Global static configuration."""
from os import getenv


CHERRYPY_CONFIG = getenv('CHERRYPY_CONFIG', 'server.conf')
DEFAULT_ARCHIVEI_ENDPOINT = getenv(
    'ARCHIVEI_PORT', 'tcp://127.0.0.1:8080').replace('tcp', 'http')
ARCHIVEI_ENDPOINT = getenv('ARCHIVEI_ENDPOINT', DEFAULT_ARCHIVEI_ENDPOINT)
DEFAULT_METADATA_ENDPOINT = getenv(
    'METADATA_PORT', 'tcp://127.0.0.1:8121').replace('tcp', 'http')
METADATA_ENDPOINT = getenv('METADATA_ENDPOINT', DEFAULT_METADATA_ENDPOINT)
METADATA_CONNECT_ATTEMPTS = 40
METADATA_WAIT = 3
METADATA_STATUS_URL = '{0}/groups'.format(METADATA_ENDPOINT)

DEFAULT_NGINX_X_ACCEL = getenv('NGINX_ACCEL', 'False')
NGINX_X_ACCEL = DEFAULT_NGINX_X_ACCEL == 'True'
