#!/usr/bin/env bash

set -e
set -x

mypy run.py app api
flake8 run.py app api tests
black run.py app api tests --check
isort run.py app api tests --check-only