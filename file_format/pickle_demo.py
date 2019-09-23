# object serializing by pickle
import pickle
from pprint import pprint as pp

# Creating data dictionary
data = {}
data['employee'] = []

data['employee'].append({
    'name': 'Satya',
    'website': 'microsoft.com',
    'from': 'India'
})
data['employee'].append({
    'name': 'Jorden',
    'website': 'IBM.com',
    'from': 'New york'
})
data['employee'].append({
    'name': 'Luther',
    'website': 'oracle.com',
    'from': 'California'
})

# For printing the info
pp(data)

# Saving file as pickle Format
with open('../tmp/employee.bin', 'wb') as handle:
    pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

# Retreiving the Pickle file back
with open('../tmp/employee.bin', 'rb') as handle:
    loaded = pickle.load(handle)
    print(type(loaded))
    pp(loaded)
    print(data == loaded)
