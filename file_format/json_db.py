import json


def load_db():
    with open("../data/db.json", encoding="utf-8") as f:
        return json.load(f)


def save_db():
    with open("../tmp/db.json", 'w', encoding="utf-8") as f:
        return json.dump(db, f, ensure_ascii=False)


db = load_db()

print(db)

save_db()
