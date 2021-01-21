import pytest


@pytest.mark.usefixtures("dataLoad")
class Testfixtures:
    def test_userdataprofile(self, dataLoad):
        print(dataLoad[0])
        print(dataLoad[2])

    def test_fixture(self, setup):
        print(setup)