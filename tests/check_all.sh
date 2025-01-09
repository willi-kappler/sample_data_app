#!/usr/bin/env bash

reset

export PYTHONPATH=$PYTHONPATH:"src/"
SRC_DIR="src/green_moon_2d"

echo "ruff:"
ruff check $SRC_DIR
ruff check tests/

echo -e "\n\n-------------------------------------------\n\n"

echo "mypy:"
mypy --check-untyped-defs $SRC_DIR
mypy --check-untyped-defs tests/

echo -e "\n\n-------------------------------------------\n\n"

echo "flake8:"
flake8 $SRC_DIR
flake8 tests/

echo -e "\n\n-------------------------------------------\n\n"

echo "pyright:"
pyright $SRC_DIR
pyright tests/
