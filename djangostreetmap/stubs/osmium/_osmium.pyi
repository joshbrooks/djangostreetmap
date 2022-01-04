from typing import overload

class BaseHandler:
    def __init__(self, *args, **kwargs) -> None: ...

class InvalidLocationError(Exception): ...

class MergeInputReader:
    def __init__(self) -> None: ...
    def add_buffer(self, buffer: bytes, format: str) -> int: ...
    def add_file(self, file: str) -> int: ...
    def apply(self, handler: BaseHandler, idx: str = ..., simplify: bool = ...) -> None: ...
    def apply_to_reader(self, reader, writer, with_history: bool = ...) -> None: ...

class NodeLocationsForWays:
    def __init__(self, arg0, osmium) -> None: ...
    def ignore_errors(self) -> None: ...

class SimpleHandler(BaseHandler):
    def __init__(self) -> None: ...
    def apply_buffer(self, buffer: bytes, format: str, locations: bool = ..., idx: str = ...) -> None: ...
    def apply_file(self, filename: str, locations: bool = ..., idx: str = ...) -> None: ...

class SimpleWriter:
    @overload
    def __init__(self, arg0: str, arg1: int) -> None: ...
    @overload
    def __init__(self, arg0: str) -> None: ...
    def add_node(self, node: object) -> None: ...
    def add_relation(self, relation: object) -> None: ...
    def add_way(self, way: object) -> None: ...
    def close(self) -> None: ...

class WriteHandler(BaseHandler):
    @overload
    def __init__(self, arg0: str, arg1: int, arg2: str) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: int) -> None: ...
    @overload
    def __init__(self, arg0: str) -> None: ...
    def close(self) -> None: ...

@overload
def apply(reader, handler: BaseHandler) -> None: ...
@overload
def apply(reader, handler: NodeLocationsForWays) -> None: ...
@overload
def apply(reader, node_handler: NodeLocationsForWays, handler: BaseHandler) -> None: ...