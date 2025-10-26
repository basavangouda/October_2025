import pytest

@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.smoke
def test_demo3_sample_one():
    print("Inside the sample one")

@pytest.mark.regression
def test_demo3_sample_two():
    print("Inside the sample two")

@pytest.mark.regression
def test_demo3_sample_three():
    print("Inside the sample three")
    assert 10==10