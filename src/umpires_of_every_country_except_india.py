import csv 

def get_umpires_of_every_country_except_india(umpires_path, matches_path):
    with open(umpires_path, 'r') as file:
        umpires = list(csv.DictReader(file))
    
    with open(matches_path, 'r') as file:
        matches = list(csv.DictReader(file))

    umpire_country_map = {}

    for umpire in umpires:
        umpire_country_map[umpire['umpire']] = umpire['country']

    return umpire_country_map

def main():
    umpires_path = "data/umpires.csv"
    matches_path = "data/matches.csv"
    print(get_umpires_of_every_country_except_india(umpires_path, matches_path))

if __name__ == "__main__":
    main()