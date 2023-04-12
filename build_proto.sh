#!/bin/bash

# in root dir
python -m grpc_tools.protoc -Iprotobuf/. --python_out=kadem/protobuf/ --pyi_out=kadem/protobuf/ --grpc_python_out=kadem/protobuf/ protobuf/*.proto
cd kadem/protobuf
sed -i -E 's/^import.*_pb2/from . \0/' *.py