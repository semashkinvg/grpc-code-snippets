#!/bin/bash

python -m grpc_tools.protoc -I./protos --python_out=$1 --pyi_out=$1 --grpc_python_out=$1 ./protos/*.proto