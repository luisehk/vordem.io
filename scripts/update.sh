#!/bin/sh
set -e
set -x

git pull origin "$(git rev-parse --abbrev-ref HEAD)"
