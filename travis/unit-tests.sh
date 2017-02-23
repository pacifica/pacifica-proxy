#!/bin/bash -xe

docker-compose up -d
MAX_TRIES=60
HTTP_CODE=$(curl -sL -w "%{http_code}\\n" localhost:8121/keys -o /dev/null || true)
while [[ $HTTP_CODE != 200 && $MAX_TRIES > 0 ]] ; do
  sleep 1
  HTTP_CODE=$(curl -sL -w "%{http_code}\\n" localhost:8121/keys -o /dev/null || true)
  MAX_TRIES=$(( MAX_TRIES - 1 ))
done
docker run -it --rm --net=pacificaproxy_default -e METADATA_URL=http://metadataserver:8121 -e PYTHONPATH=/usr/src/app pacifica/metadata python test_files/loadit.py
curl -X PUT -H 'Last-Modified: Sun, 06 Nov 1994 08:49:37 GMT' --upload-file README.md http://127.0.0.1:8080/104
readme_size=$(stat -c '%s' README.md)
readme_sha1=$(sha1sum README.md | awk '{ print $1 }')
echo '{ "hashsum": "'$readme_sha1'", "hashtype": "sha1", "size": '$readme_size'}' | curl -X POST -T - 'http://localhost:8121/files?_id=104'
docker-compose stop proxyserver

export PYTHONPATH=$PWD
coverage run --include='proxy/*' -m pytest -v
coverage report -m --fail-under=100
codeclimate-test-reporter
