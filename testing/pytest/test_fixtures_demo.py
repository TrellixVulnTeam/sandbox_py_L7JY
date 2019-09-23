# pytest test fixtures demo
import pytest


@pytest.fixture()
def setup():
    print("Setup")


@pytest.fixture(autouse=True)
def setup_auto():
    print("Auto setup")


def test1(setup):
    assert True


@pytest.mark.usefixtures("setup")
def test2():
    assert True
