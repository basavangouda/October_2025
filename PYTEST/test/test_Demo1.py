import pytest

@pytest.mark.xfail
@pytest.mark.smoke
def test_demo1_sample_one():
    print("Inside the sample one")
    assert 20==20

@pytest.mark.sanity
def test_demo1_sample_two():
    print("Inside the sample two")

@pytest.mark.regression
def test_demo1_sample_three():
    print("Inside the sample three")