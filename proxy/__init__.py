#!/usr/bin/python
"""Main proxy module."""
from __future__ import print_function
from argparse import ArgumentParser
from json import dumps
from time import sleep
import cherrypy
import requests
from proxy.root import Root
from proxy.globals import METADATA_STATUS_URL, METADATA_CONNECT_ATTEMPTS, METADATA_WAIT, CHERRYPY_CONFIG


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


def error_page_default(**kwargs):
    """The default error page should always enforce json."""
    cherrypy.response.headers['Content-Type'] = 'application/json'
    return dumps({
        'status': kwargs['status'],
        'message': kwargs['message'],
        'traceback': kwargs['traceback'],
        'version': kwargs['version']
    })


def main():
    """Main method for running the server."""
    parser = ArgumentParser(description='Run the proxy server.')
    parser.add_argument('-c', '--config', metavar='CONFIG', type=str,
                        default=CHERRYPY_CONFIG, dest='config',
                        help='cherrypy config file')
    parser.add_argument('-p', '--port', metavar='PORT', type=int,
                        default=8180, dest='port',
                        help='port to listen on')
    parser.add_argument('-a', '--address', metavar='ADDRESS',
                        default='localhost', dest='address',
                        help='address to listen on')
    args = parser.parse_args()
    cherrypy.config.update({
        'server.socket_host': args.address,
        'server.socket_port': args.port
    })
    cherrypy.quickstart(Root(), '/', args.config)
