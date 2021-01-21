import pytest


@pytest.mark.usefixtures("setup")

class Testfixture:

    def test_frame(self):
        a = 5
        b = 7
        print("Sum of :", a+b)

    def test_frame1(self):
        print("Testing for fixture")

    def test_frame2(self):
        print("Second test fixture")