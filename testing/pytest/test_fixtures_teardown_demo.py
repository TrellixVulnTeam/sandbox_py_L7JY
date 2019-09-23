# pytest test fixtures demo
import pytest


@pytest.fixture()
def setup1():
    print("\nSetup 1")
    yield
    print("Teardown 1")


@pytest.fixture()
def setup2(request):
    print("\nSetup 2")

    def teardown_a():
        print("teardown_a")

    def teardown_b():
        print("teardown_b")

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)


def test1(setup1):
    assert True


def test2(setup2):
    assert True
