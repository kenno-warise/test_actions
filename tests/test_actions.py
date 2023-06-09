import unittest

from actions import judgement


class JudgeTest(unittest.TestCase):

    def test_judgement(self):
        typecode = judgement('a')
        #  データ型の判定
        self.assertIsInstance(typecode, int)


if __name__ == '__main__':
    unittest.main()
