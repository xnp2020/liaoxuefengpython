import pytest


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score > 100 or self.score < 0:
            raise ValueError
        if self.score >= 80:
            return 'B'
        if self.score >= 60:
            return 'B'
        return 'C'


class TestStudent():
    def setUp(self) -> None:
        print('我会在调用每一个测试方法之前执行')

    def tearDown(self) -> None:
        print('我会在调用每一个测试方法之后执行 \r\n')

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        assert s1.get_grade() == 'A'
        assert s2.get_grade() == 'A'

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        assert s1.get_grade() == 'B'
        assert s2.get_grade() == 'B'

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        assert s1.get_grade() == 'C'
        assert s2.get_grade() == 'C'

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with pytest.raises(ValueError):
            s1.get_grade()
        with pytest.raises(ValueError):
            s2.get_grade()
