import unittest
import buzz

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertIn(buzz.fizz(), 'Fizz')

if __name__ == '__main__':
    unittest.main()
