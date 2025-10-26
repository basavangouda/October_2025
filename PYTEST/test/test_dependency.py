import pytest

from pytest_dependency import depends

class TestClass:

    @pytest.mark.dependency
    def test_openApplication(self):
        assert True

    @pytest.mark.dependency(depends=["TestClass::test_openApplication"])
    #classname::first test method
    def test_login(self):
        assert True

    @pytest.mark.dependency(depends=["TestClass::test_login"])
    def test_search(self):
        assert False

    @pytest.mark.dependency(depends=["TestClass::test_login","TestClass::test_search"])
    def test_advance_search(self):
        assert True

    @pytest.mark.dependency(depends=["TestClass::test_login"])
    def test_logout(self):
        assert True