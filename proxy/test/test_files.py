#!/usr/bin/python
"""Test the files proxy object."""
from json import loads
import requests
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
        """Test for a file."""
        files = loads(
            requests.get(
                '{0}/files?_id=104'.format(proxy.METADATA_ENDPOINT)
            ).text
        )
        self.assertTrue(len(files) > 0)
        the_file = files[0]
        url = '/files/{0}/{1}'.format(the_file['hashtype'], the_file['hashsum'])
        self.getPage(url)
        self.assertStatus('200 OK')
        self.assertTrue(len(self.body) == the_file['size'])

    def test_files_not_found(self):
        """Test for a file that doesn't exist."""
        url = '/files/sha256/somethingthatisnotthere'
        self.getPage(url)
        self.assertStatus('404 Not Found')
        self.assertTrue(len(self.body) > -1)
