import pytest

@pytest.fixture(autouse=True,scope="session")
def setup_and_teardown():
    print("Launching a browser")
    print("Open the application")
    yield
    print("close browser")