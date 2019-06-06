#!/bin/bash

set -e
set -x

DIRECTORY=`dirname $0`

for (( ; ; ))
do
    sh -c "cd $DIRECTORY/../ && ./scripts/static.sh"
    inotifywait -r -e modify,move,create,delete $DIRECTORY/../static
done
