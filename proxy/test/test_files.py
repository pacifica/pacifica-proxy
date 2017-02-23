#!/usr/bin/python
"""Test the files proxy object."""
from cherrypy.test import helper
import proxy
from proxy.test.test_common import CommonCPSetup


class TestFilesObject(helper.CPWebCase, CommonCPSetup):
    """Test the files proxy server."""

    NGINX_X_ACCEL_PORT = 8123
    PORT = 8180
    HOST = '127.0.0.1'
    headers = [('Content-Type', 'application/json')]

    def test_files(self):
        """Test the root object."""
        files = loads(
            requests.get(
                '{0}/files?_id=104'.format(proxy.METADATA_ENDPOINT)
            ).text
        )
        if len(files) == 0:
            self.assertFalse(True)
        the_file = files[0]
        url = '/files/{0}/{1}'.format(the_file['hashtype'], the_file['hashsum'])
        self.getPage(url)
        self.assertStatus('200 OK')
        self.assertTrue(len(self.body) == the_file['size'])
