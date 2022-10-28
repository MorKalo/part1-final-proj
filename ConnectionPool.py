import threading
import time
from db.DbRepo import DbRepo, local_session


class ConnectionPool(object):
    _instance = None
    _lock = threading.Lock()
    _lock_pool = threading.Lock()
    _max_connections = 20

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def get_instance(cls):
        if cls._instance:
            return cls._instance
        with cls._lock:
            if cls._instance is None: #t1 + t2
                cls._instance = cls.__new__(cls)
                cls._instance.connections = [DbRepo(local_session) for i in range(cls._max_connections)]
            return cls._instance

    def get_free_count(self):
        return len(self.connections)

    def get_max_possible_connections(self):
        return ConnectionPoolSingleton._max_connections

    def get_connection(self):
        # will return a connection and remove it from the list
        # return self.connections ...
        # lock
        while True:
            if len(self.connections) == 0:
                time.sleep(1/2)
                continue
            with self._lock_pool:
                if len(self.connections) > 0:
                    return self.connections.pop(0)

    def return_connection(self, conn):
        # will take the connection and add it to the list
        # self.connections --> append
        # lock
        # tt
        with self._lock_pool:
            self.connections.append(conn) # list python is thread safe

