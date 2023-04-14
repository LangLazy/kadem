import grpc
from protobuf import ping_request_pb2
from protobuf import hash_node_pb2_grpc
from protobuf import store_request_pb2

with grpc.insecure_channel('localhost:50051') as channel:
    stub = hash_node_pb2_grpc.HashNodeStub(channel)
    stub.Store(store_request_pb2.StoreRequest(key="asd", value="asdads", node_ip="[::]", node_port=50052, node_id="asdasdasd"))
