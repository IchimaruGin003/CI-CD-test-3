import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.app import dedupe

def test_dedupe():
    # Test with integers
    assert list(dedupe([1, 2, 2, 3])) == [1, 2, 3]
    
    # Test with strings
    assert list(dedupe(['a', 'b', 'b', 'c'])) == ['a', 'b', 'c']
    
    # Test empty list
    assert list(dedupe([])) == []
    
    # Test no duplicates
    assert list(dedupe([1, 2, 3])) == [1, 2, 3]
