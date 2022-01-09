import abc
from opengsq.socket_async import SocketAsync


class ProtocolBase(abc.ABC):
    @property
    @abc.abstractmethod
    def full_name(self):
        pass

    def __init__(self, address: str, query_port: int, timeout: float = 5.0):
        self._sock = None
        self._address = address
        self._query_port = query_port
        self._timeout = timeout
