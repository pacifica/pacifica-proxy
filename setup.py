#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Setup and install the proxy."""
from pip.req import parse_requirements
from setuptools import setup

# parse_requirements() returns generator of pip.req.InstallRequirement objects
INSTALL_REQS = parse_requirements('requirements.txt', session='hack')

setup(
    name='PacificaProxy',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description='Pacifica Proxy',
    author='David Brown',
    author_email='david.brown@pnnl.gov',
    packages=['proxy', 'proxy.test'],
    entry_point={
        'console_scripts': ['ProxyServer=proxy:main'],
    },
    scripts=['ProxyServer.py'],
    install_requires=[str(ir.req) for ir in INSTALL_REQS]
)
