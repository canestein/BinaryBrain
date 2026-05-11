# test_binarybrain.py
"""
Tests for BinaryBrain module.
"""

import unittest
from binarybrain import BinaryBrain

class TestBinaryBrain(unittest.TestCase):
    """Test cases for BinaryBrain class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BinaryBrain()
        self.assertIsInstance(instance, BinaryBrain)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BinaryBrain()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
