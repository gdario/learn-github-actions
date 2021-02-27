import unittest
import utils


class TestDecreasedSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(utils.decreased_sum(10, 5, 3), 12)

    def test_assertion(self):
        with self.assertRaises(AssertionError):
            utils.decreased_sum(10, 5, '3')


class TestSpaceToUnderscores(unittest.TestCase):

    def test_underscore(self):
        self.assertEqual(utils.space_to_underscore('Ciao bubu'),
                         'Ciao_bubu')


if __name__ == '__main__':
    unittest.main()
