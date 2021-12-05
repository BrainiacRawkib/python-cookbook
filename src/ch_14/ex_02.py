# Patching objects in unit tests
from unittest.mock import patch
import example


# using patch as a decorator
@patch('example.func')
def test1(x, mock_func):
    example.func(x)  # Uses patched example.func
    mock_func.assert_called_with(x)


# using patch as a context manager
with patch('example.func') as mock_func:
    x = ''
    example.func(x)  # Uses patched example.func
    mock_func.assert_called_with(x)
