import unittest
import cpyparser

class TestImport(unittest.TestCase):
    
    def test_basic_import (self):
        res = cpyparser.parse_tree("""
        int function(int a);
        """)
        self.assertTrue (res.functions['function'] != None)

unittest.main()                             
