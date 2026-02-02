# test_craftcast.py
"""
Tests for CraftCast module.
"""

import unittest
from craftcast import CraftCast

class TestCraftCast(unittest.TestCase):
    """Test cases for CraftCast class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CraftCast()
        self.assertIsInstance(instance, CraftCast)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CraftCast()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
