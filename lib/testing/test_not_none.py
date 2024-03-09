# testing/test_not_none.py

from not_none_functions import return_not_none

def test_return_not_none():
    '''in not_none_functions, function "return_not_none" returns a value that is not None.'''
    result = return_not_none()
    assert result is None, "Expected a None value"
