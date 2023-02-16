#!/bin/bash

python setup.py install

for var in "$@"; do
  hw=$(echo "$var" | tr '[:lower:]' '[:upper:]')
  cd "$hw/src"
  python main.py -g all
  cd ../..
done
