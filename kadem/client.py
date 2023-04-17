import grpc
import hashlib
from protobuf import ping_request_pb2
from protobuf import hash_node_pb2_grpc
from protobuf import store_request_pb2
from routingTable import routingTable

# with grpc.insecure_channel('localhost:50051') as channel:
#     stub = hash_node_pb2_grpc.HashNodeStub(channel)
#     stub.Store(store_request_pb2.StoreRequest(key="asd", value="asdads", node_ip="[::]", node_port=50052, node_id="asdasdasd"))
id = int.from_bytes(hashlib.sha1("gasdasasdfasdfasdfdasdasdasdasdamer".encode()).digest(), "little")
almost =0b011001101110110000001110110111101111100010111110110111000100011000101000000100101010010110000100100111100110101011001111001010101111011000111110011110010100101
print(bin(id), almost)
# almost = ((~id)|0)|((~(1<<160))&id)
# print(bin(almost))
table = routingTable.RoutingTable(id, 3)
table.insertNewNode(almost)
print(table)

# bitMask = 1

# number1 = 1
# number2 = 3
# movement = ~(number1^number2)

# i = 0
# while movement&bitMask:
#     # print(bin(number1), bin(number2))
#     # number2 = number2 >>1
#     # number1 = number1 >>1
#     # print(number1&bitMask, number2&bitMask, "----", i)
#     # i += 1
#     # if i > 5:
#         # break
#     print("sad")
#     movement >>= 1