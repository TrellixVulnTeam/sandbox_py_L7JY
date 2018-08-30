import json

print(json.loads('[10, 20, 30]')[1])  # deserialize
print(json.loads('["hoge/fuga"]'))
print(json.dumps([5, 4, 3, 2, 1]))  # serialize
print(json.dumps({"ほげ": "ふが", 2: None}))
print(json.dumps('ほげ/ふが'))
print(json.dumps('ほげ/ふが', ensure_ascii=False))
print(json.dumps({'first_name': 'hoge', 'last_name': 'fuga'}, indent=2))
