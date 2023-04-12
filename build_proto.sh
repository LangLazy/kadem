#!/bin/bash

# in root dir
python -m grpc_tools.protoc -Iprotobuf/. --python_out=kadem/protobuf/ --pyi_out=kadem/protobuf/ --grpc_python_out=kadem/protobuf/ protobuf/kadem/proto/*.proto