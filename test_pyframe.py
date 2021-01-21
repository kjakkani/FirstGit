# Any python test(pytest) file should start with test_
# pytest name should start with test
# Any code should be wrapped in method only
# Method name should have sense
# -k Stands for method names execution
# -s stands for logs in output
# -v stands for more info metadata
# you can run specific file with py.test <filename>
# you can mark(tag) test @pytest.mark.smoke and then run with -m
# you can skip the test with @pytest.mark.skip
# you can run the test but not to give on report using with @pytest.mark.xfail
# you can use the @pytest.fixture() to use the pre-requisite setup tests.
# fixtures are used as setup and tear down methods for test cases
# conftest file to generalize fixture and make it available for all test cases
# Datadriven and Parameterization can be done with return statement in tuple format
# When define fixture scope to class only,  it will run once before class initiated and at the end.

import pytest

@pytest.mark.skip
def test_firstprog():
    print("Hello! world")

@pytest.mark.smoke
def test_second():
    print("Good Morning! Kishore")


def test_crossBrowser(CrossBrowser):
    print(CrossBrowser)
