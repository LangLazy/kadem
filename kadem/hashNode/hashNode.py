import grpc
from concurrent import futures
from protobuf import (hash_node_pb2_grpc, ping_response_pb2, ping_request_pb2)

class HashNode(hash_node_pb2_grpc.HashNodeServicer):
    def __init__(self, ip, id, port) -> None:
        self.ip = ip
        self.id = id
        self.port = port
        self.__startNode()
    
    def __startNode(self) -> None:
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        hash_node_pb2_grpc.add_HashNodeServicer_to_server(self, server)
        server.add_insecure_port(self.ip+ ':' + str(self.port))
        server.start()
        server.wait_for_termination()

    def Ping(self, request, context) -> None:
        print(f"I({self.id}) WAS PINGED")
        #TODO: should also update buckets
        #Sends a response back with the info of the current node
        return ping_response_pb2.PingResponse(node_ip=self.ip, node_id=self.id, node_port=self.port)

    def sendPing(self, ip, port) -> None:
        with grpc.insecure_channel(ip+ ':' + str(port)) as channel:
            stub = hash_node_pb2_grpc.HashNodeStub(channel)
            stub.Ping(ping_request_pb2.PingRequest(node_ip=self.ip, node_id=self.id, node_port=self.port))
