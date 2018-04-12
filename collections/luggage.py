# packing, unpacking


def packer(name=None, **kwargs):
    print(kwargs)


def unpacker(first_name=None, last_name=None):
    if first_name and last_name:
        print("Hi {} {}!".format(first_name, last_name))
    else:
        print("Hi Nanasi!")


packer(name="hoge", num="12", special=True)

unpacker(**{"first_name": "Hoge", "last_name": "Fuga"})
