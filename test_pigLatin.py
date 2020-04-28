#This is the unit test for problem 2, the pig latin conversion problem
#This program uses python 3.8 standard library

import unittest
import pigLatin

class TestPigLatin(unittest.TestCase):

    def test_pigLatin(self):
        self.assertEqual(pigLatin.pigLatin("This is test 1."), "hisTay siay esttay 1.")
        self.assertEqual(pigLatin.pigLatin("This is test 2. It has 3 sentences?! The last 300, what;"), "hisTay siay esttay 2. tIay ashay 3 entencessay?! heTay astlay 300, hatway;")
        self.assertEqual(pigLatin.pigLatin("It's over 9,000!!!"), "t'sIay veroay 9,000!!!")

if __name__ == '__main__':
    unittest.main()

