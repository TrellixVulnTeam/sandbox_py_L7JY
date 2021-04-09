import json


def demo():
    print(json.loads('[10, 20, 30]')[1])  # deserialize
    print(json.loads('["hoge/fuga"]'))

    print(json.dumps([5, 4, 3, 2, 1]))  # serialize
    print(json.dumps({"ほげ": "ふが", 2: None}))
    print(json.dumps('ほげ/ふが'))
    print(json.dumps('ほげ/ふが', ensure_ascii=False))
    print(json.dumps({'first_name': 'hoge', 'last_name': 'fuga'}, indent=2))


def serialize():
    # define a python dictionary
    data = {
        'sandwich': 'Reuben',
        'toasted': True,
        'toppings': [
            'Thousand Island Dressing',
            'Sauerkraut',
            'Pickles'
        ],
        'price': 8.99
    }

    # serialize to JSON using dumps
    json_str = json.dumps(data, indent=4)
    print(json_str)


def parse():
    # define a string of JSON code
    json_str = '''{
            "sandwich" : "Reuben",
            "toasted" : true,
            "toppings" : [
                "Thousand Island Dressing",
                "Sauerkraut",
                "Pickles"
            ],
            "price" : 8.99
        }'''

    try:
        # parse the JSON data using loads
        data = json.loads(json_str)
        print(data)

        # print information from the data structure
        print("Sandwich: " + data['sandwich'])
        if data['toasted']:
            print("And it's toasted!")
        for topping in data['toppings']:
            print("Topping:", topping)
    except json.JSONDecodeError as err:
        print("Whoops, JSON Decoding error:")
        print(err.msg)
        print(err.lineno, err.colno)


if __name__ == "__main__":
    demo()
    print("---")
    serialize()
    print("---")
    parse()
