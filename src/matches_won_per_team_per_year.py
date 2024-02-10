import csv
import matplotlib.pyplot as plt

def matches_won_per_team_per_year(path):
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        matches = list(reader)

    matches_won = {}
    for match in matches:
        if(matches_won.get(match['season']) == None):
            matches_won[match['season']] = {}
        if(matches_won[match['season']].get(match['winner']) == None):
            matches_won[match['season']][match['winner']] = 0
        matches_won[match['season']][match['winner']] += 1

    return matches_won

def preparing_data(data):
    sorted_data = dict(sorted(data.items(), key=lambda x: x[0]))
    teams = list(set(winner for season_data in sorted_data.values() for winner in season_data.keys()))
    team_wins = {team: [year_data.get(team, 0) for year_data in sorted_data.values()] for team in teams}
    return teams, team_wins

def plot_bar_chart(teams, team_wins):
    positions = [str(year) for year in range(2008, 2018)]
    plt.figure(figsize=(10, 5))
    bottom = [0] * len(positions)
    for i, team in enumerate(teams):
        plt.bar(positions, team_wins[team], label=team, bottom=bottom)
        bottom = [bottom[j] + team_wins[team][j] for j in range(len(positions))]
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.xlabel('Season',fontsize=25)
    plt.ylabel('Wins',fontsize=25)
    plt.title('IPL Team Wins Over Seasons',fontsize=30)
    plt.tight_layout()
    plt.show()


def main():
    path = 'data/matches.csv'
    teams, team_wins = preparing_data(matches_won_per_team_per_year(path))
    plot_bar_chart(teams, team_wins)

if __name__ == "__main__":
    main()