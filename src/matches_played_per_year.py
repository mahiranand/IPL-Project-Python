import csv

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

def main():
    path = 'data/matches.csv'
    print(matches_played_per_year(path))
    
if __name__ == "__main__":
    main()