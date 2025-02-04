from simulation import simulate
from scenarios import scenarios

def main():
    results = [simulate(scenario["name"], scenario["funcs"]) for scenario in scenarios]

    for result in results:
        print(result)

if __name__ == "__main__":
    main()