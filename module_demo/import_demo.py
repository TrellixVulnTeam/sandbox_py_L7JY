import my_module

print(my_module)
print(dir(my_module))
print('{}, {}'.format(my_module.VAR1, my_module.VAR2))


from init import hoge
print(hoge.HOGE)


from no_init import hoge
print(hoge.HOGE)
