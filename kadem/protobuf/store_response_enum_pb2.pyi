from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor
STORE_FAILED: StoreResult
STORE_SUCCESSFUL: StoreResult

class StoreResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
