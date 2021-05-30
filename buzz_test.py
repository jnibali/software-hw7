import unittest
import buzz

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertIn(buzz.fizz(), 'Fizz')
        self.assertIn(buzz.fizz(), 'Buzz')
        self.assertIn(buzz.fizz(), 'FizzBuzz')

if __name__ == '__main__':
    unittest.main()
