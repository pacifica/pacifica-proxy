#!/usr/bin/python
"""Main proxy process."""
from __future__ import print_function


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
    print('to be written')


if __name__ == '__main__':
    main()
