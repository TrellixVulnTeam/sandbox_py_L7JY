from importlib import import_module

if __name__ == '__main__':
    try:
        module = import_module('my_package.sub_package1.module1')
        module = import_module('.sub_package1.module1', 'my_package')
        module = import_module('.module1', 'my_package.sub_package1')
    except ImportError as e:
        print(e)
    else:
        print(module.__name__)
