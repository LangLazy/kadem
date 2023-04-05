import hashlib

class Node:

    ipAddress: str
    port: int
    id: str

    def __init__(self, ip: str, port: int):
        self.ipAddress = ip
        self.port = port
        self.id = haslib.new(ip + ":" + port)
