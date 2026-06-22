# test_shieldcore.py
"""
Tests for ShieldCore module.
"""

import unittest
from shieldcore import ShieldCore

class TestShieldCore(unittest.TestCase):
    """Test cases for ShieldCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ShieldCore()
        self.assertIsInstance(instance, ShieldCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ShieldCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
