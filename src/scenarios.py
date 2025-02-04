import random

scenarios = [
    {
        "name": "Deterministic",
        "funcs": [lambda: 0.4, lambda: 0.6, lambda: 0.95],
    },
    {
        "name": "Uniform",
        "funcs": [
            lambda: random.uniform(0.1, 0.7),
            lambda: random.uniform(0.1, 1.1),
            lambda: random.uniform(0.1, 1.8),
        ],
    },
    {
        "name": "Exponential",
        "funcs": [
            lambda: random.expovariate(1/0.4),
            lambda: random.expovariate(1/0.6),
            lambda: random.expovariate(1/0.95),
        ],
    },
]