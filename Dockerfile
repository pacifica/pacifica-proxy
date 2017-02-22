FROM python:2-onbuild
EXPOSE 8180
CMD [ "python", "./ProxyServer.py" ]
