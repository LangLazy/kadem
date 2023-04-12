import grpc
from protobuf import ping_request_pb2
from protobuf import hash_node_pb2_grpc

with grpc.insecure_channel('localhost:50051') as channel:
    stub = hash_node_pb2_grpc.HashNodeStub(channel)
    stub.Ping(ping_request_pb2.PingRequest())
