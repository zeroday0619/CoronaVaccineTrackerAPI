#!/bin/sh -e
set -x

isort run.py app api tests --force-single-line-imports
autoflake --remove-all-unused-imports --recursive --remove-unused-variables run.py app api tests --exclude=__init__.py
black run.py app api tests
isort run.py app api tests