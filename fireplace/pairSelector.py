import random
import os.path
from collections import namedtuple
from bisect import bisect
from importlib import import_module
from pkgutil import iter_modules
from typing import List
from xml.etree import ElementTree
from hearthstone.enums import CardClass, CardType

class pairSelector:
	def __init__(self):
		pass

def PrintPlayerCharacters(game: ".game.Game") -> ".game.Game":
	allys = game.player1.characters

	print("\n\n\n\n")

	#	list that holds the pairs for ally-to-enemy decision making
	pairs = []

	#	for each ally in the field...
	for ally in allys:
		#	if the ally is a enemy...
		#print("{}:\t{}\t\t{} HP".format(ally.controller, ally, ally.health))
		#	for each enemy the ally can enemy...
		for enemy in ally.targets:
			#	Calculate a weight for decision making between ally ally and it's enemy
			decisionWeight = GetDecisionWeight(ally, enemy)

			#	Cache a tuple for the ally ally and its enemy and its calculated weight
			AllyToEnemyWeight = (ally, enemy, decisionWeight)

			pairs.append(AllyToEnemyWeight)
			#print("\t\t{}".format(enemy))

	#print(pairs)

	decisionPair = GetDecisionPair(pairs)

	print("{} with {} ATK and {} HP vs {} with {} ATK and {} HP is the best choice.".format(decisionPair[0], decisionPair[0].atk, decisionPair[0].health, decisionPair[1], decisionPair[1].atk, decisionPair[1].health))
	print("weight of {}".format(decisionPair[2]))

	print("\n\n\n\n")

#	Calculates the decision weight (int) between the given ally and the enemy
def GetDecisionWeight(ally, enemy):
	#print(dir(ally))
	weight = 0

	#	if ally can perform lethal attack on enemy hero...  attack hero
	#if ally.atk >= enemy.:
	#	weight += 9999
	if ally.atk >= enemy.health:
		weight += 1
		if enemy.atk >= ally.health:
			weight += enemy.atk

	return weight

#	Return a tuple that contains the pair with the highest decision weight
def GetDecisionPair(pairs):

	highestPair = pairs[0]

	for pair in pairs:
		if pair[2] > highestPair[2]:
			highestPair = pair

	return highestPair
