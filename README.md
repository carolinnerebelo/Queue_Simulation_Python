# Queue Simulation

## Project Overview
This project is a queue simulation designed for the course "Modeling and Performance Evaluation" in the Computer Science program at Federal University of Rio de Janeiro. The simulation models a system with three servers (S1, S2, and S3) and evaluates metrics such as:

- **Average time in the system**
- **Standard deviation of time in the system**

The simulation runs in different scenarios, each with varying service time distributions.

## System Description
The system consists of three servers, each with an unlimited queue:

- Every job must first be processed by **Server S1**.
- After completing service at **S1**, the job proceeds:
  - With **50% probability** to **Server S2**.
  - With **50% probability** to **Server S3**.
- A job leaving **S2** has a **20% probability** of returning to **S2** for another service.
- Jobs leave the system upon completing service at **S3** or after the final departure from **S2**.

## Job Arrival Process
- Job arrivals follow a **Poisson process** with rate **λ = 2 jobs per second**.
- The interarrival time is an **exponential random variable** with mean **1/λ = 0.5 seconds**.

## Simulation Scenarios
The simulation is conducted in three different scenarios:

1. **Deterministic Service Times**
   - Fixed service times: **0.4s, 0.6s, and 0.95s** for **S1, S2, and S3**, respectively.

2. **Uniformly Distributed Service Times**
   - Service times are **uniformly distributed** in the intervals:
     - **(0.1, 0.7) for S1**
     - **(0.1, 1.1) for S2**
     - **(0.1, 1.8) for S3**

3. **Exponentially Distributed Service Times**
   - Service times follow an **exponential distribution** with means:
     - **0.4s for S1**
     - **0.6s for S2**
     - **0.95s for S3**

## Warm-Up Period and Metrics Collection
- The first **10,000 jobs** are discarded as a **warm-up phase** to allow the system to reach a steady state.
- Metrics are collected from the **next 10,000 jobs**.

## Project Structure
```
queue_simulation/
│-- src/
│   │-- main.py         # Entry point for running the simulation
│   │-- server.py       # Server class
│   │-- event.py        # Event handling
│   │-- simulation.py   # Core simulation logic
│   │-- scenarios.py    # Different scenarios configurations
│   │-- config.py       # Global variables
│-- README.md           # Project documentation
```

## Expected Output
The program prints the average time in the system and the standard deviation for each scenario:

```
{'Scenario': 'Deterministic', 'Average time': X.XX, 'Standard Deviation': Y.YY}
{'Scenario': 'Uniform', 'Average time': X.XX, 'Standard Deviation': Y.YY}
{'Scenario': 'Exponential', 'Average time': X.XX, 'Standard Deviation': Y.YY}
```


