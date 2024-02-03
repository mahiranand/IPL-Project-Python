import csv

def top_10_batsman_banglore(path):
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        deliveries = list(reader)

    batsman_runs = {}
    for delivery in deliveries:
        if(delivery['batting_team'] == 'Royal Challengers Bangalore'):
            if(batsman_runs.get(delivery['batsman']) == None):
                batsman_runs[delivery['batsman']] = 0
            batsman_runs[delivery['batsman']] += int(delivery['batsman_runs'])

    top_10_batsman = sorted(batsman_runs.items(), key=lambda x: x[1], reverse=True)[:10]
    return top_10_batsman

def main():
    path = 'data/deliveries.csv'
    print(top_10_batsman_banglore(path))

if __name__ == '__main__':
    main()