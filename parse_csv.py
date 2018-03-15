import csv

with open('portfolio.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')  # iterator
    rows = list(reader)
    for row in rows[:10]:
        print(', '.join(row))

print('---')

with open('portfolio.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')  # Dict(<=3.5), OrderedDict(>=3.6)
    rows = list(reader)
    for row in rows[:10]:
        print(row)

print('---')

with open('people.csv', 'a', encoding='utf-8') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows([
        {'first_name': 'hoge', 'last_name': 'fuga'},
        {'first_name': 'fefe', 'last_name': 'awawa'}
    ])
