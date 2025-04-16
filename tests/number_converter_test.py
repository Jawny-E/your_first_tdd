from your_first_tdd.number_converter import *
import unittest

class TestNumberConverter(unittest.TestCase):
    
    def test_zero(self):
        self.assertEqual("zero", NumberConverter().to_words(0))
        
    def test_single_digit(self):
        self.assertEqual("one", NumberConverter().to_words(1))
        self.assertEqual("nine", NumberConverter().to_words(9))
    
    def test_special_double_digits(self):
        self.assertEqual("ten", NumberConverter().to_words(10))
        self.assertEqual("nineteen", NumberConverter().to_words(19))
    
    def test_tens(self):
        self.assertEqual("twenty", NumberConverter().to_words(20))
        self.assertEqual("ninety", NumberConverter().to_words(90))
        
    def test_not_multiple_of_ten_under_100(self):
        self.assertEqual("twenty-four", NumberConverter().to_words(24))    
        self.assertEqual("ninety-nine", NumberConverter().to_words(99))    
        