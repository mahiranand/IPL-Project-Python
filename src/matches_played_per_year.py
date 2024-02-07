import csv
import matplotlib.pyplot as plt

def matches_played_per_year(path):
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        matches = list(reader)

    matches_played = {}
    for match in matches:
        if(matches_played.get(match['season']) == None):
            matches_played[match['season']] = 0
        matches_played[match['season']] += 1

    return matches_played

def plotGraph(matches_played_per_year):
    years = list(matches_played_per_year.keys())
    matches = list(matches_played_per_year.values())

    plt.bar(years, matches, color='orange')
    plt.xlabel('Years')
    plt.ylabel('Matches Played')
    plt.title('Matches played per year')
    plt.show()

def main():
    path = 'data/matches.csv'
    plotGraph(matches_played_per_year(path))
    
if __name__ == "__main__":
    main()