# pytest test xUnit style fixtures demo


def setup_module():
    print("\nsetup_module")


def teardown_module():
    print("teardown_module")


def setup_function():
    print("setup_function")


def teardown_function():
    print("teardown_function")


def test1():
    assert True


def test2():
    assert True
