#from termcolor import *
from cards import Monster, Spell, Trap, Deck
from input import Input
from field import Field
import pygame
from pygame.locals import *
colour_text = True
graphics_setting = True
class ErrorHandler():
	def __init__(self):
		pass
	def raise_error(self, error_type, string):
		error_string = "default error."
		if error_type == "Import":
			error_string = "%s couldn't be imported." % string
		
		error_output = "%sError: " % error_type + error_string
		cprint(error_output, on_color = "on_red")

if colour_text == True:
    try:
        from termcolor import *
        def eprint(text, on_color):
            cprint(text, on_color = on_color)
    except ImportError:
        def cprint(text, colour):
            print text
        def eprint(text, on_color):
            print text
        eprint("ImportError: termcolor could not be imported.", on_color = "on_red")
else:
    def cprint(text, colour):
        print text
    def eprint(text, on_color):
        print text


