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

def GetOptimalDecisionPair(game: ".game.Game") -> ".game.Game":
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

	#	Return a tuple that contains the pair with the highest decision weight
	decisionPair = pairs[0]

	for pair in pairs:
		if pair[2] >= decisionPair[2]:
			decisionPair = pair

	print("{} with {} ATK and {} HP to attack {} with {} ATK and {} HP is a optimal choice given current events.".format(decisionPair[0], decisionPair[0].atk, decisionPair[0].health, decisionPair[1], decisionPair[1].atk, decisionPair[1].health))
	if decisionPair[2] <= 0:
		print("Action has a weight of {}, better to not attack.".format(decisionPair[2]))
	else:
		print("Action has a weight of {}".format(decisionPair[2]))

	print("\n\n\n\n")

	return decisionPair

#	Calculates the decision weight (int) between the given ally and the enemy
def GetDecisionWeight(ally, enemy):
	#print(dir(ally))
	weight = 0

	#print("ally {} has {} ATK and {} HP".format(ally, ally.atk, ally.health))
	#print("enemy {} has {} ATK and {} HP".format(enemy, enemy.atk, enemy.health))

	if int(enemy.atk) <= 0 and int(ally.atk) > 0:
		weight += 9000

	elif int(enemy.atk) >= 0 and int(ally.atk) <= 0:
		weight += -9000

	if ally.atk >= enemy.health:
		weight += ally.atk - enemy.health

	#if enemy.atk >= ally.health:
	#	weight += -(enemy.atk + ally.health)

	#if ally.atk >= enemy.health:
	#	weight += (ally.atk - enemy.health) - (ally.health - enemy.atk)

	#if ally.atk
	#weight += ally.atk - enemy.health
	#if ally.health > enemy.health:
	#weight += -enemy.atk
	#if ally.health >= enemy.atk:
	#	weight += ally.health - enemy.atk

	return weight
