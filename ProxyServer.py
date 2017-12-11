#!/usr/bin/python
"""Main proxy process."""
import cherrypy
from proxy import error_page_default, main
from proxy.globals import CHERRYPY_CONFIG
from proxy.root import Root


cherrypy.config.update({'error_page.default': error_page_default})
# pylint doesn't realize that application is actually a callable
# pylint: disable=invalid-name
application = cherrypy.Application(Root(), '/', CHERRYPY_CONFIG)
# pylint: enable=invalid-name
if __name__ == '__main__':
    main()
