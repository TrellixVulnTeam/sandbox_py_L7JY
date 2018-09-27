class MixIn1:
    def method(self):
        print("MixIn1")
        super().method()  # 直上のクラスに存在しなくても、mroが空でない限りerrorにはならない


class MixIn2:
    def method(self):
        print("MixIn2")


class Sub(MixIn1, MixIn2):
    def method(self):
        super().method()


if __name__ == '__main__':
    s = Sub()
    s.method()
