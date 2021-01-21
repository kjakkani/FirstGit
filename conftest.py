import pytest


@pytest.fixture(scope="class")
def setup():
    print("This test will execute first")
    yield
    print("This test will execute last")


@pytest.fixture()
def dataLoad():
    print("These are data to load in runtime")
    return ["Kishore", "Kumar", "Kishorejakkani.com"]


@pytest.fixture(params=["Chrome","Firefox","IE"])
def CrossBrowser(request):
    return request.param
