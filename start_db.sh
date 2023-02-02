#!/usr/bin/env bash
docker network inspect project_parser >/dev/null 2>&1 || docker network create --driver bridge project_parser
docker-compose --env-file=backend/.env up -d --build
