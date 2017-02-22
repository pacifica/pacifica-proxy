#!/bin/bash
pylint --rcfile=pylintrc proxy
pylint --rcfile=pylintrc ProxyServer.py
radon cc proxy
