from nose.tools import *
from yugioh.errors import ErrorHandler

error_handler = ErrorHandler()

def test_raise_error():
	error_handler.raise_error("ImportError", "Testing Error")