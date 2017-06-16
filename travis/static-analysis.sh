#!/bin/bash
pylint --rcfile=pylintrc proxy
pylint --rcfile=pylintrc ProxyServer.py setup.py
radon cc proxy
