import csv

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

def main():
    path = 'data/matches.csv'
    print(matches_won_per_team_per_year(path))

if __name__ == "__main__":
    main()