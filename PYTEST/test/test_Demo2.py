import pytest

@pytest.mark.smoke
def test_demo2_sample_one():
    print("Inside the sample one")

@pytest.mark.smoke
def test_demo2_sample_two():
    print("Inside the sample two")
    a=200
    assert a.__eq__(200)

@pytest.mark.smoke
@pytest.mark.regression
def test_demo2_sample_three():
    print("Inside the sample three")