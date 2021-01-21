# Any python test(pytest) file should start with test_
# pytest name should start with test
# Any code should be wrapped in method only
import pytest


@pytest.mark.smoke
@pytest.mark.xfail
def test_assertprog():
    mesg = "Hello Kishore!"
    assert "Kishore" == mesg,  'This test fails because the string is not matched'

def test_calculationprog():
    a = 6
    b = 10
    assert a+4 == b, 'This test will fail becuase the addition not match'



