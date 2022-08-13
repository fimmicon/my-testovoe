#!/bin/bash

set -e
if ! [[ $(which docker) && $(which docker-compose) ]]; then
    echo "Installed docker and docker-compose is required"
    exit 1;
fi

docker build -t exporter -f exporter/Dockerfile exporter/src/.
docker-compose -f docker-compose.yml up  -d
