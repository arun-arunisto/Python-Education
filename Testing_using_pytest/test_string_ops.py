from .string_operators import str_operations

class TestStringOperations:
    str_op = str_operations("Arunisto")
    msg = "Test Failed"
    reverse_str = str_op.reverse_str()
    upper_str = str_op.upper_str()
    lower_str = str_op.lower_str()

    def test_reverse_str(self):
        assert self.reverse_str == "otsinurA", self.msg

    def test_upper_str(self):
        assert self.upper_str == "ARUNISTO", self.msg

    def test_lower_str(self):
        assert self.lower_str == "arunisto", self.msg
        
