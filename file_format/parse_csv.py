import csv


def demo():
    with open('../data/portfolio.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')  # iterator
        for row in reader:
            print(', '.join(row))

    print('---')

    with open('../data/portfolio.csv', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=',')  # Dict(<=3.5), OrderedDict(>=3.6)
        for row in reader:
            print(row)

    print('---')

    with open('../tmp/people.csv', 'w+', newline='', encoding='utf-8') as f:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows([
            {'first_name': 'hoge', 'last_name': 'fuga'},
            {'first_name': 'fefe', 'last_name': 'awawa'}
        ])

        f.seek(0)
        print(f.read(), end='')


# Use the CSV module Sniffer to see what dialect of CSV this is
def use_sniffer(file):
    with open(file, newline='', encoding='utf-8') as f:
        dialect = csv.Sniffer().sniff(f.read(1024))
        f.seek(0)
        has_header = csv.Sniffer().has_header(f.read(1024))
        f.seek(0)
        print("Headers found: " + str(has_header))
        print("delimiter: " + str(dialect.delimiter))
        print("escapechar: " + str(dialect.escapechar))
        print("quotechar: " + str(dialect.quotechar))


if __name__ == '__main__':
    demo()
    print('---')
    use_sniffer("../data/StockQuotes.csv")
    print('---')
    use_sniffer("../data/portfolio.csv")
