# pytest test fixtures demo
import pytest


@pytest.fixture(scope="session", autouse=True)
def setup_s():
    print("Setup session")


@pytest.fixture(scope="module", autouse=True)
def setup_m():
    print("Setup module")


@pytest.fixture(scope="class", autouse=True)
def setup_c():
    print("Setup class")


@pytest.fixture(scope="function", autouse=True)
def setup_f():
    print("Setup function")


class TestHoge:
    def test1(self):
        print("Hoge.test1")
        assert True

    def test2(self):
        print("Hoge.test2")
        assert True


def test1():
    print("test1")
    assert True


def test2():
    print("test2")
    assert True
