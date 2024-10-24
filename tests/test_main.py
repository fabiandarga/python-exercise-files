import unittest
import src.main as main


class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertIsNotNone(main.test_1, msg="Die Funktion xxx gibt es noch nicht.")

    def test_add_numbers_pass(self):
        self.assertEqual(main.add_numbers(2, 3), 5)


if __name__ == '__main__':
    unittest.main()
