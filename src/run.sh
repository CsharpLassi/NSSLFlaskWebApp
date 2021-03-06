#!/usr/bin/env bash

[[ -z "$HOST" ]] && HOST="0.0.0.0"
[[ -z "$PORT" ]] && PORT=5000
[[ -z "$SECRET_KEY" ]] && SECRET_KEY=$(openssl rand -hex 16)

gunicorn --bind ${HOST}:${PORT} wsgi:application
