from collections import namedtuple

ARRIVAL_RATE = 2
NUM_JOBS = 20000
WARM_UP = 10000

Event = namedtuple("Event", ["time", "type", "jobID", "serverID"])