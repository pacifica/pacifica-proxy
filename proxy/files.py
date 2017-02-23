#!/usr/bin/python
"""CherryPy files proxy."""
from json import loads
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

    # pylint: disable=invalid-name
    @staticmethod
    def GET(hashtype, hashsum):
        """Create the local objects we need."""
        files = loads(
            requests.get(
                '{0}/files?hashsum={1}&hashtype={2}'.format(METADATA_ENDPOINT, hashsum, hashtype)
            ).text
        )
        if len(files) == 0:
            return cherrypy.HTTPError(404, 'Not Found')
        the_file = files[0]
        if NGINX_X_ACCEL:
            cherrypy.response.headers.update({
                'X-Accel-Redirect': '/archivei_accel/{0}'.format(the_file['_id']),
                'Content-Disposition': 'attachment; filename={0}'.format(the_file['name']),
                'Content-Type': 'application/octet-stream'
            })
        else:
            resp = requests.get('{0}/{1}'.format(ARCHIVEI_ENDPOINT, the_file['_id']), stream=True)
            mime = 'application/octet-stream'
            response = cherrypy.serving.response
            response.headers['Content-Type'] = mime
            disposition = 'attachment'
            contentd = '%s; filename="%s"' % (disposition, the_file['name'])
            response.headers['Content-Disposition'] = contentd
            # pylint: disable=protected-access
            return cherrypy.lib.static._serve_fileobj(resp.raw, mime, int(the_file['size']), True)
            # pylint: enable=protected-access
    # pylint: enable=invalid-name
# pylint: enable=too-few-public-methods
