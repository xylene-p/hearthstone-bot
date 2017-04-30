import random
import os.path
import re
from bisect import bisect

from numpy import exp, array, dot
from NeuralNetwork import NeuralNetwork

from . import pairSelector

from .gamestate import GameState

from importlib import import_module
from pkgutil import iter_modules
from typing import List
from xml.etree import ElementTree
from hearthstone.enums import CardClass, CardType


# Autogenerate the list of cardset modules
_cards_module = os.path.join(os.path.dirname(__file__), "cards")
CARD_SETS = [cs for _, cs, ispkg in iter_modules([_cards_module]) if ispkg]


class CardList(list):
	def __contains__(self, x):
		for item in self:
			if x is item:
				return True
		return False

	def __getitem__(self, key):
		ret = super().__getitem__(key)
		if isinstance(key, slice):
			return self.__class__(ret)
		return ret

	def __int__(self):
		# Used in Kettle to easily serialize CardList to json
		return len(self)

	def contains(self, x):
		"True if list contains any instance of x"
		for item in self:
			if x == item:
				return True
		return False

	def index(self, x):
		for i, item in enumerate(self):
			if x is item:
				return i
		raise ValueError

	def remove(self, x):
		for i, item in enumerate(self):
			if x is item:
				del self[i]
				return
		raise ValueError

	def exclude(self, *args, **kwargs):
		if args:
			return self.__class__(e for e in self for arg in args if e is not arg)
		else:
			return self.__class__(e for k, v in kwargs.items() for e in self if getattr(e, k) != v)

	def filter(self, **kwargs):
		return self.__class__(e for k, v in kwargs.items() for e in self if getattr(e, k, 0) == v)


def mage_deck():
	# arcane missles
	# frostbolt
	# arcane intellect
	# fireball
	# polymorph
	# water elemental
	# flamestrike
	# acidic swamp ooze
	# novice engineer
	# shattered sun cleric
	# chillwind yeti
	# gnomish inventor
	# sen'jin sheildmasta
	# gurabashi berserker
	# boulderfist ogre

	from . import cards
	deck = []
	card_list = ['EX1_277', 'CS2_024', 'CS2_023', 'CS2_029', 'CS2_022', 'CS2_033', 'CS2_032', 'EX1_066', 'EX1_015', 'EX1_019', 'CS2_182', 'CS2_147', 'CS2_179', 'EX1_399', 'CS2_200']
	for card in card_list:
		for i in range(2):
			deck.append(cards.db[card].id)

	return deck


def warrior_deck():
	# cleave
	# execute
	# fiery war axe
	# heroic strike
	# shieldblock
	# warsong commander
	# kor'kron elite
	# arcanite reaper
	# acid swamp ooze
	# bloodfin raptor
	# novice engineer
	# shattered
	# chillwind
	# gnomish
	# boulderfist

	from . import cards
	deck = []
	card_list = ['CS2_114', 'CS2_108', 'CS2_106', 'CS2_105', 'EX1_606', 'EX1_084', 'NEW1_011', 'CS2_112', 'EX1_066', 'CS2_172', 'EX1_015', 'EX1_019', 'CS2_182', 'CS2_147', 'CS2_200']
	for card in card_list:
		for i in range(2):
			deck.append(cards.db[card].id)

	return deck



def random_class():
	return CardClass(random.randint(2, 10))


def get_script_definition(id):
	"""
	Find and return the script definition for card \a id
	"""
	for cardset in CARD_SETS:
		module = import_module("fireplace.cards.%s" % (cardset))
		if hasattr(module, id):
			return getattr(module, id)


def entity_to_xml(entity):
	e = ElementTree.Element("Entity")
	for tag, value in entity.tags.items():
		if value and not isinstance(value, str):
			te = ElementTree.Element("Tag")
			te.attrib["enumID"] = str(int(tag))
			te.attrib["value"] = str(int(value))
			e.append(te)
	return e


def game_state_to_xml(game):
	tree = ElementTree.Element("HSGameState")
	tree.append(entity_to_xml(game))
	for player in game.players:
		tree.append(entity_to_xml(player))
	for entity in game:
		if entity.type in (CardType.GAME, CardType.PLAYER):
			# Serialized those above
			continue
		e = entity_to_xml(entity)
		e.attrib["CardID"] = entity.id
		tree.append(e)

	return ElementTree.tostring(tree)


def weighted_card_choice(source, weights: List[int], card_sets: List[str], count: int):
	"""
	Take a list of weights and a list of card pools and produce
	a random weighted sample without replacement.
	len(weights) == len(card_sets) (one weight per card set)
	"""

	chosen_cards = []

	# sum all the weights
	cum_weights = []
	totalweight = 0
	for i, w in enumerate(weights):
		totalweight += w * len(card_sets[i])
		cum_weights.append(totalweight)

	# for each card
	for i in range(count):
		# choose a set according to weighting
		chosen_set = bisect(cum_weights, random.random() * totalweight)

		# choose a random card from that set
		chosen_card_index = random.randint(0, len(card_sets[chosen_set]) - 1)

		chosen_cards.append(card_sets[chosen_set].pop(chosen_card_index))
		totalweight -= weights[chosen_set]
		cum_weights[chosen_set:] = [x - weights[chosen_set] for x in cum_weights[chosen_set:]]

	return [source.controller.card(card, source=source) for card in chosen_cards]


def setup_game() -> ".game.Game":
	from .game import Game
	from .player import Player

	deck1 = mage_deck()
	deck2 = warrior_deck()
	player1 = Player("Player", deck1, CardClass.MAGE.default_hero)
	player2 = Player("Opponent", deck2, CardClass.WARRIOR.default_hero)

	game = Game(players=(player1, player2))
	game.start()

	return game


def play_turn(game: ".game.Game") -> ".game.Game":
	player = game.current_player

	nn = NeuralNetwork()

	while True:
		heropower = player.hero.power
		if heropower.is_usable() and random.random() < 0.1:
			if heropower.requires_target():
				heropower.use(target=random.choice(heropower.targets))
			else:
				heropower.use()
			continue

		# iterate over our hand and play whatever is playable
		for card in player.hand:
			if card.is_playable() and random.random() < 0.5:
				target = None
				if card.must_choose_one:
					card = random.choice(card.choose_cards)
				if card.requires_target():
					target = random.choice(card.targets)
				print("Playing %r on %r" % (card, target))
				card.play(target=target)

				if player.choice:
					choice = random.choice(player.choice.cards)
					print("Choosing card %r" % (choice))
					player.choice.choose(choice)

				continue

		# Randomly attack with whatever can attack

		for character in player.characters:
			compStr = str(character)
			if 'Jaina' in compStr:
				#Player 1 actions
				for target in character.targets:
					target_attr = dir(target)
					# print (target_attr)
					print("Target: {}\tTarget Health: {}\t Target Attack: {}".format(target, target.health, target.atk))
				if character.can_attack():
					character.attack(random.choice(character.targets))
					print (character.targets)
					# newInput = character.targets
					# newOutput = nn.think(ally.atk, ally.health, target.atk, target.health)
			elif 'Garrosh' in compStr:
				#Player 2 actions
				for target in character.targets:
					target_attr = dir(target)
					# print (target_attr)
					print("Target: {}\tTarget Health: {}\t Target Attack: {}".format(target, target.health, target.atk))
				if character.can_attack():
					character.attack(random.choice(character.targets))

		break

	game.end_turn()
	return game


def play_full_game() -> ".game.Game":
	game = setup_game()
	game_state = GameState(game)

	nn = NeuralNetwork()
	for player in game.players:
		print("Can mulligan %r" % (player.choice.cards))
		mull_count = random.randint(0, len(player.choice.cards))
		cards_to_mulligan = random.sample(player.choice.cards, mull_count)
		player.choice.choose(*cards_to_mulligan)

	while True:
		game_state.update(game)
		pairSelector.PrintPlayerCharacters(game)
		play_turn(game)

	return game
