import random

import os.path

from bisect import bisect

from importlib import import_module

from pkgutil import iter_modules

from typing import List

from xml.etree import ElementTree

from hearthstone.enums import CardClass, CardType

class pairSelector:
	def __init__(self):
		pass

def PrintPlayerCharacters(player):

	print("\n\n\n\n\n")
	for character in player.characters:
		print("Ally: {}\t {} HP".format(character, character.health))
