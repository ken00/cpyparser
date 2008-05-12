import unittest
import cpyparser as cpy

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

if __name__ == '__main__':
    unittest.main()
