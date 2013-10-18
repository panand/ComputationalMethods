import unittest

def swapCharacters(word):
    """swap the first and last chars of the word
    
    Arguments:
       word: (string)
    
    Returns
        val: (string)
    
    Raises:
    
    """
    l = list(word)
    temp = word[-1]
    l[-1] = l[0]
    l[0] = temp
    return ''.join(l)

class TestSwap(unittest.TestCase):
    """a testing class for swapCharacters"""
    
    #these first two methods control what happens at the start and end of each test
    def setUp(self):
        pass
    def tearDown(self):
        pass
    #every test must be preceded by "test_"
    def test_NumberInput(self):
        input = 7
        self.assertRaises(TypeError, swapCharacters, 7)

if __name__ == "__main__":
    unittest.main()
