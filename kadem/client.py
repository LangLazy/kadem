import grpc
import hashlib
from protobuf import ping_request_pb2
from protobuf import hash_node_pb2_grpc
from protobuf import store_request_pb2
from routingTable import routingTable

# with grpc.insecure_channel('localhost:50051') as channel:
#     stub = hash_node_pb2_grpc.HashNodeStub(channel)
#     stub.Store(store_request_pb2.StoreRequest(key="asd", value="asdads", node_ip="[::]", node_port=50052, node_id="asdasdasd"))
# id = int.from_bytes(hashlib.sha1("gamer".encode()).digest(), "little")
# newId = int.from_bytes(hashlib.sha1("large".encode()).digest(), "little")
# print((0>>160)^((1<<160)>>160))
table = routingTable.RoutingTable(0, 3)
table.insertNewNode(1<<160)