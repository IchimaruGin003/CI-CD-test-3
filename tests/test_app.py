import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.app import dedupe,add_numbers

def test_dedupe():
    # Test with integers
    assert list(dedupe([1, 2, 2, 3])) == [1, 2, 3]
    
    # Test with strings
    assert list(dedupe(['a', 'b', 'b', 'c'])) == ['a', 'b', 'c']
    
    # Test empty list
    assert list(dedupe([])) == []
    
    # Test no duplicates
    assert list(dedupe([1, 2, 3])) == [1, 2, 3]

def test_add_numbers():
    from app.app import add_numbers
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
