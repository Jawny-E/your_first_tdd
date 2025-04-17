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
    
    def test_hundreds(self):
        self.assertEqual("one-hundred", NumberConverter().to_words(100))
        self.assertEqual("one-hundred and twenty-four", NumberConverter().to_words(124))    
    
    def test_thouands(self):
        self.assertEqual("one thousand and three-hundred", NumberConverter().to_words(1_300))
        self.assertEqual("nine thousand and ninety-nine", NumberConverter().to_words(9_099)) 

    def test_millions(self):
        self.assertEqual("three million and twenty", NumberConverter().to_words(3_000_020))
        self.assertEqual("one-hundred million and three", NumberConverter().to_words(100_000_003)) 
        