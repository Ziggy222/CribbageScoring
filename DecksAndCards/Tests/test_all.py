"""
Test suite to run all tests at once.
This file imports and runs all test modules.
"""
import unittest
import sys
import os

# Add project root directory to path to import from DecksAndCards package
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

# Import all test modules
from DecksAndCards.Tests import test_Card, test_Deck, test_Cribbage

def create_test_suite():
    """Create a test suite containing all tests"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Load tests from each test module
    suite.addTests(loader.loadTestsFromModule(test_Card))
    suite.addTests(loader.loadTestsFromModule(test_Deck))
    suite.addTests(loader.loadTestsFromModule(test_Cribbage))
    
    return suite

if __name__ == '__main__':
    # Create and run the test suite
    suite = create_test_suite()
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Exit with appropriate code
    sys.exit(0 if result.wasSuccessful() else 1)

