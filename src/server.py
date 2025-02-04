from collections import deque

class Server:
    def __init__(self, serverID, serviceTimeFunction):
        self.ID = serverID
        self.serviceTimeFunction = serviceTimeFunction
        self.busy = False
        self.queue = deque()