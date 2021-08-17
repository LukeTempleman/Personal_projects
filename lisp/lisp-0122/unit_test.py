import unittest
import lisp
from io import StringIO


#write all unit tests here
class MyTestCase(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(lisp.parser('(+ 3 7)') , '10')



if __name__ == '__main__':
    unittest.main()