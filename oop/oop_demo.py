import random


class Character:
    def __init__(self, name, **kwargs):
        self.name = name

        # 自由にattributeを追加できる
        for key, value in kwargs.items():
            setattr(self, key, value)


class Thief(Character):
    # Class attribute
    # instanceに同名変数がない場合は、こちらが参照されることに注意
    sneaky = True

    def __init__(self, name, sneaky=True, **kwargs):
        super().__init__(name, **kwargs)
        self.sneaky = sneaky  # instance attribute
        # super().__init__(name, **kwargs)  # Javaと違って後置OKだが、同名変数がある場合は上書きしてしまうので注意

    def pickpocket(self):
        # print("Called by {}".format(self))
        return self.sneaky and bool(random.randint(0, 1))

    def hide(self, light_level):
        return self.sneaky and light_level < 10


def main():
    pass


if __name__ == "__main__":
    main()
