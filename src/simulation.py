import heapq
import random
from config import ARRIVAL_RATE, NUM_JOBS, WARM_UP, Event
from server import Server
from events import systemArrival, serverArrival, serverDeparture

def simulate(scenario, serviceTimeFunctions):
    servers = {
        1: Server(1, serviceTimeFunctions[0]),
        2: Server(2, serviceTimeFunctions[1]),
        3: Server(3, serviceTimeFunctions[2])
    }

    eventQueue = []
    heapq.heapify(eventQueue)

    completedJobs = {}
    jobTimes = {}

    currentTime = 0

    for jobID in range(1, NUM_JOBS + 1):
        interarrivalTime = random.expovariate(ARRIVAL_RATE)
        currentTime += interarrivalTime
        heapq.heappush(eventQueue, Event(currentTime, "ARRIVAL", jobID, None))
    
    while eventQueue:
        event = heapq.heappop(eventQueue)
        currentTime = event.time

        if event.type == "ARRIVAL":
            systemArrival(event, currentTime, servers, eventQueue, jobTimes)
        elif event.type == "SERVER ARRIVAL":
            serverArrival(event, currentTime, servers, eventQueue)
        elif event.type == "SERVER DEPARTURE":
            serverDeparture(event, currentTime, servers, eventQueue, completedJobs, jobTimes)
        
    collectedTimes = list(completedJobs.values())[WARM_UP:]
    if not collectedTimes:
        raise RuntimeError("Insufficient jobs processed after warm-up phase.")

    averageTime = sum(collectedTimes) / len(collectedTimes)
    standardDeviation =  (sum((time - averageTime) **2 for time in collectedTimes) / len(collectedTimes)) ** 0.5

    return {"Scenario": scenario, "Average time": averageTime, "Standard Deviation": standardDeviation}