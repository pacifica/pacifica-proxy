#!/usr/bin/python
"""CherryPy files proxy."""
import requests
import cherrypy
from proxy import METADATA_ENDPOINT, NGINX_X_ACCEL, ARCHIVEI_ENDPOINT


# pylint: disable=too-few-public-methods
class Files(object):
    """
    CherryPy files object class.

    This object proxies requests to the archive interface service
    based on the files hashsum instead of ID.
    """

    exposed = True

    @staticmethod
    def GET(hashtype, hashsum):
        """Create the local objects we need."""
        files = loads(requests.get('{0}/files?hashsum={1}&hashtype={2}'.format(METADATA_ENDPOINT, hashsum, hashtype)).text)
        if len(files) == 0:
            return cherrypy.HTTPError(404)
        file = files[0]
        if NGINX_X_ACCEL:
            cherrypy.response.headers.update({
                'X-Accel-Redirect': '/archivei_accel/{0}'.format(file['_id']),
                'Content-Disposition': 'attachment; filename={0}'.format(file['_id']),
                'Content-Type': 'application/octet-stream'
            })
        else:
            resp = requests.get('%s/%s'.format(ARCHIVEI_ENDPOINT, file['_id']), stream=True)
            mime = 'application/octet-stream'
            return cherrypy.lib.static.serve_fileobj(resp.raw, mime, str(file['_id']))
# pylint: enable=too-few-public-methods
