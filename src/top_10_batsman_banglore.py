import csv
import matplotlib.pyplot as plt

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

def plotGraph(top_10_batsman):
    batsman = [x[0] for x in top_10_batsman]
    runs = [x[1] for x in top_10_batsman]

    plt.bar(batsman, runs)
    plt.xlabel('Batsman')
    plt.ylabel('Runs')
    plt.title('Top 10 batsman of Royal Challengers Bangalore')
    plt.xticks(rotation=90)
    plt.show()

def main():
    path = 'data/deliveries.csv'
    plotGraph(top_10_batsman_banglore(path))

if __name__ == '__main__':
    main()