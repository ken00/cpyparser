import unittest
import cpyparser as cpy
import os
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
        buff = open(TEST_FILE).readlines()
        print buff[0]
        res = self.get_type(cpy.lexer(buff[0]))
        print buff[1]
        self.assertEquals( buff[1].split(), res)


if __name__ == '__main__':
    unittest.main()
