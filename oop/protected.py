class Protected:
    __name = "Security"

    def __method(self):
        return self.__name


prot = Protected()
# print(prot.__name)  # NG
# print(prot.__method())  # NG
print(dir(prot))

# name mangling
print(prot._Protected__name)
print(prot._Protected__method())
