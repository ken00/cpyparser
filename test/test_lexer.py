import unittest
import cpyparser as cpy
import os
from itertools import islice
from collections import deque

TEST_FILE = os.path.join( os.path.dirname(__file__), 'c_functions.txt')

class TestLexer (unittest.TestCase):
    
    def test_lexer (self):
        self.assertNotEquals (0, len(cpy.lexer ("void c_function (void);") ) )

    def test_identifier(self):
        res = cpy.lexer ("void c_function (void);")
        self.assertEquals([ t.type for t in res ] , ['VOID',
                                    'IDENTIFIER',
                                    '(',
                                    'VOID',
                                    ')',
                                    ';'])

    def get_type (self, toklist):
        return [ t.type for t in toklist ]

    def test_automata (self):
        full = deque(open(TEST_FILE).readlines())
        while full:
            a = full.popleft()
            b = full.popleft()
            res = self.get_type(cpy.lexer(a))
            self.assertEquals( b.split(), res)

if __name__ == '__main__':
    unittest.main()
