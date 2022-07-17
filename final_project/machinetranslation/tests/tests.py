import unittest

from translator import e2f_translator, f2e_translator

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(e2f_translator(""), "") 
    def test2(self):   
        self.assertEqual(e2f_translator("Hello"), "Bonjour")  

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(f2e_translator(""), "")
    def test2(self):     
        self.assertEqual(f2e_translator("Bonjour"), "Hello") 
        

unittest.main()