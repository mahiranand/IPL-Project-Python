import csv
import matplotlib.pyplot as plt

def total_runs_by_each_team(path):
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        deliveries = list(reader)

    total_runs_by_each_team = {}

    for delivery in deliveries:
        if(total_runs_by_each_team.get(delivery['batting_team']) == None):
            total_runs_by_each_team[delivery['batting_team']] = 0
        total_runs_by_each_team[delivery['batting_team']] += int(delivery['total_runs'])

    return total_runs_by_each_team;

def plotGraph(total_runs_by_each_team):
    teams = list(total_runs_by_each_team.keys())
    runs = list(total_runs_by_each_team.values())

    plt.bar(teams, runs)
    plt.xlabel('Teams')
    plt.ylabel('Runs')
    plt.title('Total runs by each team')
    plt.xticks(rotation=90)
    plt.show()

def main():
    path = 'data/deliveries.csv'
    plotGraph(total_runs_by_each_team(path))

if __name__ == '__main__':
    main()