import pytest

#Approcach 2
class TestClass:

    @pytest.mark.run(order=3)
    def test_methodC(self):
        print("Running Method C")

    @pytest.mark.run(order=1)
    def test_methodA(self):
        print("Running Method A")
        assert 10==100

    @pytest.mark.run(order=5)
    def test_methodE(self):
        print("Running Method E")

    @pytest.mark.run(order=4)
    def test_methodD(self):
        print("Running Method D")

    @pytest.mark.run(order=2)
    def test_methodB(self):
        print("Running Method B")