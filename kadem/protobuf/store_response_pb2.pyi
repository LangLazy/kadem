import store_response_enum_pb2 as _store_response_enum_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StoreResponse(_message.Message):
    __slots__ = ["message", "result"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    message: str
    result: _store_response_enum_pb2.StoreResult
    def __init__(self, result: _Optional[_Union[_store_response_enum_pb2.StoreResult, str]] = ..., message: _Optional[str] = ...) -> None: ...
