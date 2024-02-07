import csv
import matplotlib.pyplot as plt

def top_10_eco_bowler_2015(matches_path, deliveries_path):
    with open(matches_path, 'r') as file:
        reader = csv.DictReader(file)
        matches = list(reader)

    with open(deliveries_path, 'r') as file:
        reader = csv.DictReader(file)
        deliveries = list(reader)

    id_season_map = {}
    for match in matches:
        id_season_map[match['id']] = match['season']

    bowler_runs = {}
    bowler_balls = {}
    for delivery in deliveries:
        if(id_season_map[delivery['match_id']] == '2015'):
            if(bowler_runs.get(delivery['bowler']) == None):
                bowler_runs[delivery['bowler']] = 0
            if(bowler_balls.get(delivery['bowler']) == None):
                bowler_balls[delivery['bowler']] = 0
            bowler_runs[delivery['bowler']] += int(delivery['total_runs'])
            bowler_balls[delivery['bowler']] += 1

    bowler_eco = {}
    for bowler in bowler_runs.keys():
        bowler_eco[bowler] = (bowler_runs[bowler] / bowler_balls[bowler]) * 6

    top_10_eco_bowler = dict(sorted(bowler_eco.items(), key=lambda item: item[1])[:10])

    return top_10_eco_bowler

def plotGraph(top_10_eco_bowler):
    bowlers = list(top_10_eco_bowler.keys())
    economy = list(top_10_eco_bowler.values())

    plt.bar(bowlers, economy)
    plt.xlabel('Bowlers')
    plt.ylabel('Economy')
    plt.title('Top 10 economy bowlers of 2015')
    plt.xticks(rotation=90)
    plt.show()

def main(): 
    matches_path = 'data/matches.csv'
    deliveries_path = 'data/deliveries.csv'
    plotGraph(top_10_eco_bowler_2015(matches_path, deliveries_path))

if __name__ == "__main__":
    main()