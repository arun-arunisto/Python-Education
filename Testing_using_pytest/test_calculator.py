from .calculator import Calc


class TestCalc:
    calc = Calc(12, 10)
    def test_add(self):
        assert self.calc.add() == 22, "Add test Failed"

    def test_sub(self):
        assert self.calc.sub() == 2, "Sub test failed"

    def test_mul(self):
        assert self.calc.mul() == 120, "Mul test failed"

    def test_div(self):
        assert self.calc.div() == 1.2, "Div test failed"
        
