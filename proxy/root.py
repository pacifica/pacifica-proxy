#!/usr/bin/python
# -*- coding: utf-8 -*-
"""CherryPy root object."""
from proxy.files import Files


# pylint: disable=too-few-public-methods
class Root(object):
    """
    CherryPy root object class.

    not exposed by default the base objects are exposed
    """

    exposed = False

    def __init__(self):
        """Create the local objects we need."""
        self.files = Files()
# pylint: enable=too-few-public-methods
