# pytest test fixtures demo
import pytest


@pytest.fixture(params=[1, 2, 3])
def setup(request):
    print("\nSetup")
    ret = request.param * 10
    return ret


def test1(setup):
    print(setup)
    assert True
