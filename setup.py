#!/usr/bin/python
"""Setup and install the proxy."""
from pip.req import parse_requirements
from setuptools import setup

# parse_requirements() returns generator of pip.req.InstallRequirement objects
INSTALL_REQS = parse_requirements('requirements.txt', session='hack')

setup(name='PacificaProxy',
      version='1.0',
      description='Pacifica Proxy',
      author='David Brown',
      author_email='david.brown@pnnl.gov',
      packages=['proxy'],
      scripts=['ProxyServer.py'],
      install_requires=[str(ir.req) for ir in INSTALL_REQS])
