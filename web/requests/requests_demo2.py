import requests

base_url = 'https://restcountries.eu/rest/v2/'

print('What information do you want about a country? Choose one.')
print('1. Population')
print('2. Languages')
print('3. Timezone')
option = input()

country = input('What country do you want that information for? ')

params = {'fields': 'population;languages;timezones', 'fullText': 'true'}
r = requests.get(f'{base_url}name/{country}', params=params)
json_response = r.json()

country = None

try:
    country = json_response[0]
except KeyError:
    print('Country Not Found')

if country:
    if option == '1':
        population = country['population']
        print('Population is {}.'.format(population))
    elif option == '2':
        langs = []
        for language in country['languages']:
            langs.append(language['name'])
        print('The languages are: {}.'.format(', '.join(langs)))
    else:
        print('The timezones are: {}.'.format(', '.join(country['timezones'])))
