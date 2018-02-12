import os
import unittest

def analyze_text(filename):
    """Calculate the number of lines and characters in a file.
    
    Args:
        filename: The name of the file to analyze.
        
    Raises:
        IOError: If ``filename`` does not exist or can't be read.
        
    Returns: The number of lines in the file.
    """
    lines = 0
    chars = 0
    with open(filename, mode='rt', encoding='utf-8') as f:
        for line in f:
            lines += 1
            chars += len(line)
    return lines, chars

class TextAnalysisTests(unittest.TestCase):
    """Test for the ``analyze_text()`` function."""
    
    # The names of "setUp" and "tearDown" doesn't follow the convention 
    # specified by PEP 8 because they predates PEP 8.
    def setUp(self):
        """Fixture that creates a file for the text methods to use."""
        self._filename = 'text_analysis_test_file.txt'
        with open(self._filename, mode='wt', encoding='utf-8') as f:
            f.write('Now we are engaged in a great civil war.\n'
                    'testing whether that nation,\n'
                    'or any nation so conceived and so dedicated.\n'
                    'can long endure.')
        
    def tearDown(self):
        """Fixture that deletes the files used by the test methods."""
        try:
            os.removeo(self._filename)
        except:
            pass
    
    def test_function_runs(self):
        """Basic smoke test: does the function run."""
        analyze_text(self._filename)
        
    def test_line_count(self):
        """Check that the line count is correct."""
        self.assertEqual(analyze_text(self._filename)[0], 4)
        
    def test_char_count(self):
        """Check that the character count is correct."""
        self.assertEqual(analyze_text(self._filename)[1], 131)
        
    def test_no_such_file(self):
        """Check the proper exception is thrown for a missing file."""
        with self.assertRaises(IOError):
            analyze_text('foobar')
            
    def test_no_deletion(self):
        """Check that the function doesn't delete the input file."""
        analyze_text(self._filename)
        self.assertTrue(os.path.exists(self._filename))
        
if __name__ == '__main__':
    unittest.main()
