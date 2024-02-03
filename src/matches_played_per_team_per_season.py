import csv

def matches_played_per_team_per_season(path):
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        matches = list(reader)

    matches_played = {}
    for match in matches:
        if(matches_played.get(match['team1']) == None):
            matches_played[match['team1']] = {}
        if(matches_played[match['team1']].get(match['season']) == None):
            matches_played[match['team1']][match['season']] = 0
        matches_played[match['team1']][match['season']] += 1

        if(matches_played.get(match['team2']) == None):
            matches_played[match['team2']] = {}
        if(matches_played[match['team2']].get(match['season']) == None):
            matches_played[match['team2']][match['season']] = 0
        matches_played[match['team2']][match['season']] += 1

    return matches_played

def main():
    path = 'data/matches.csv'
    print(matches_played_per_team_per_season(path))

if __name__ == '__main__':
    main()