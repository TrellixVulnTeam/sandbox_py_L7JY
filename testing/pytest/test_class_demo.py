# pytest test class demo
# xUnit style fixtures


class TestHoge:
    @classmethod
    def setup_class(cls):
        print("\nsetup_class")

    @classmethod
    def teardown_class(cls):
        print("teardown_class")

    def setup_method(self):
        print("setup_method")

    def teardown_method(self):
        print("teardown_method")

    def test1(self):
        assert True

    def test2(self):
        assert True


class HogeTest:
    """not discovered"""

    def test_fail(self):
        assert False
