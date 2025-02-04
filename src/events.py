import heapq
import random
from config import Event

def systemArrival(event, currentTime, servers, eventQueue, jobTimes):
    jobTimes[event.jobID] = currentTime
    heapq.heappush(eventQueue, Event(currentTime, "SERVER ARRIVAL", event.jobID, 1))

def serverArrival(event, currentTime, servers, eventQueue):
    server = servers[event.serverID]

    if server.busy:
        server.queue.append(event.jobID)
    else:
        server.busy = True
        serviceTime = server.serviceTimeFunction()
        heapq.heappush(eventQueue, Event(currentTime + serviceTime, "SERVER DEPARTURE", event.jobID, server.ID))

def serverDeparture(event, currentTime, servers, eventQueue, completedJobs, jobTimes):
    server = servers[event.serverID]

    if event.serverID == 1:
        nextServer = 2 if random.random() < 0.5 else 3
        heapq.heappush(eventQueue, Event(currentTime, "SERVER ARRIVAL", event.jobID, nextServer))

    elif event.serverID == 2:
        if random.random() < 0.2:
            heapq.heappush(eventQueue, Event(currentTime, "SERVER ARRIVAL", event.jobID, 2))
        else:
            completedJobs[event.jobID] = currentTime - jobTimes[event.jobID]
    
    elif event.serverID == 3:
        completedJobs[event.jobID] = currentTime - jobTimes[event.jobID]
    
    if server.queue:
        nextJob = server.queue.popleft()
        serviceTime = server.serviceTimeFunction()
        heapq.heappush(eventQueue, Event(currentTime + serviceTime, "SERVER DEPARTURE", nextJob, server.ID))
    else:
        server.busy = False