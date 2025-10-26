import pytest

#Case 1
@pytest.mark.parametrize("username,password",[("QACircle","QAC@123"),
                                              ("BG","bg@123"),
                                              ("QAC","Turn@25"),
                                              ("abc","abc@123")])
def test_login(username,password):
    print(username,"=======",password)

#Case 2
class TestClass:
    @pytest.mark.parametrize('num1,num2',[(1,1),(2,4),(5,5),(10,11)])
    def test_calculation(self,num1,num2):
        assert num1==num2


