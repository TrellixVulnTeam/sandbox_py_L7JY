import json

print(json.loads('[10, 20, 30]')[1])  # deserialize
print(json.dumps([5, 4, 3, 2, 1]))  # serialize
print(json.dumps({'first_name': 'hoge', 'last_name': 'fuga'}))
