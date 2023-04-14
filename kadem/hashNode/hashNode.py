import grpc
import hashlib
from concurrent import futures
from protobuf import (hash_node_pb2_grpc, ping_response_pb2, ping_request_pb2,
                      store_request_pb2, store_response_pb2, store_response_enum_pb2)

class HashNode(hash_node_pb2_grpc.HashNodeServicer):
    def __init__(self, ip : str, id : str, port : int) -> None:
        self.ip = ip
        self.id = hashlib.sha1(id.encode())
        self.port = port
        self.store = {}
        self.__startNode()
    
    def __startNode(self) -> None:
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        hash_node_pb2_grpc.add_HashNodeServicer_to_server(self, server)
        server.add_insecure_port(self.ip+ ':' + str(self.port))
        server.start()
        server.wait_for_termination()

    def Ping(self, request : ping_request_pb2.PingRequest, context) -> None:
        print(f"I ({self.id.hexdigest()}) WAS PINGED")
        #TODO: should also update buckets
        #Sends a response back with the info of the current node
        return ping_response_pb2.PingResponse(node_ip=self.ip, node_id=self.id, node_port=self.port)

    def Store(self, request : store_request_pb2.StoreRequest, context) -> None:
        print(f"I({self.id.hexdigest()}) WAS REQUESTED TO STORE")
        #TODO Doesnt protobuf always encode to utf-8?
        key, value = request.key.encode(), request.value
        hashedKey = hashlib.sha1(key).hexdigest()
        if hashedKey in self.store:
            return store_response_pb2.StoreResponse(result=store_response_enum_pb2.STORE_FAILED, message="Key already in store")
        self.store[hashedKey] = value
        return store_response_pb2.StoreResponse(result=store_response_enum_pb2.STORE_SUCCESSFUL)

    def sendPing(self, ip : str, port : int) -> None:
        with grpc.insecure_channel(ip+ ':' + str(port)) as channel:
            stub = hash_node_pb2_grpc.HashNodeStub(channel)
            stub.Ping(ping_request_pb2.PingRequest(node_ip=self.ip, node_id=self.id, node_port=self.port))
