#!/bin/sh

if [ "$1" = 'robot' ]; then
    exec robot -P tests --outputdir results tests/tests.robot
fi

if [ "$1" = 'multiples' ]; then
    exec multiples results/input.txt results/output.txt
fi

exec "$@"
