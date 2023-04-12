from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PingResponse(_message.Message):
    __slots__ = ["node_id", "node_ip", "node_port"]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_IP_FIELD_NUMBER: _ClassVar[int]
    NODE_PORT_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    node_ip: str
    node_port: int
    def __init__(self, node_ip: _Optional[str] = ..., node_port: _Optional[int] = ..., node_id: _Optional[str] = ...) -> None: ...
