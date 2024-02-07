import csv
import matplotlib.pyplot as plt

def extra_runs_conceded_by_team_in_2016(matches_path, deliveries_path):
    with open(matches_path, 'r') as file:
        reader = csv.DictReader(file)
        matches = list(reader)

    with open(deliveries_path, 'r') as file:
        reader = csv.DictReader(file)
        deliveries = list(reader)

    id_season_map = {}
    for match in matches:
        id_season_map[match['id']] = match['season']

    extra_runs_conceded = {}
    for delivery in deliveries:
        if(id_season_map[delivery['match_id']] == '2016'):
            if(extra_runs_conceded.get(delivery['bowling_team']) == None):
                extra_runs_conceded[delivery['bowling_team']] = 0
            extra_runs_conceded[delivery['bowling_team']] += int(delivery['extra_runs'])
    
    return extra_runs_conceded

def plotGraph(extra_runs_conceded_by_team_in_2016):
    teams = list(extra_runs_conceded_by_team_in_2016.keys())
    extra_runs = list(extra_runs_conceded_by_team_in_2016.values())

    plt.bar(teams, extra_runs)
    plt.xlabel('Teams')
    plt.ylabel('Extra Runs')
    plt.title('Extra runs conceded by each team in 2016')
    plt.xticks(rotation=90)
    plt.show()

def main():
    matches_path = 'data/matches.csv'
    deliveries_path = 'data/deliveries.csv'
    plotGraph(extra_runs_conceded_by_team_in_2016(matches_path, deliveries_path))

if __name__ == "__main__":
    main()