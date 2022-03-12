import csv


def fetch(csvfile):
    with open(csvfile, newline='', encoding="utf-8") as csvfile:
            data = csv.DictReader(csvfile)
            print(data)
            return list(data)


def main():
    data = fetch( '../data/population-by-state.csv')
    state = input('State: ')
    year = input('Year: ')
    for row in data:
        print(row[state], row[year])


if __name__ == '__main__':
    main()
