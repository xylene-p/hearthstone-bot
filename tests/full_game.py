# !/usr/bin/env python
import sys; sys.path.append("..")
from numpy import exp, array, random, dot
from NeuralNetwork import NeuralNetwork
from NeuronLayer import NeuronLayer
from fireplace import cards # fireplace/fireplace/cards
from fireplace.exceptions import GameOver #fireplace/fireplace/exceptions.py
from fireplace.utils import play_full_game #fireplace/fireplace/utils.py

def test_full_game(game_count):
	try:
		play_full_game()
	except GameOver:
		print("Game {} completed normally.".format(game_count + 1))
	return game_count

def main():
	layer1 = NeuronLayer(4, 4)
	layer2 = NeuronLayer(1, 4)
	neural_network = NeuralNetwork(layer1, layer2)

	neural_network.train(60000)

	cards.db.initialize()
	for x in range(10):
		test_full_game(x)
			# hidden_state, output = neural_network.think(array([0.5, 0.1, 0.1, 0.1]))
			# print ("Considering new situation [0.5, 0.1, 0.1, 0.1] -> ?: ", output)
			# hidden_state, output = neural_network.think(array([0.3, 0.1, 0.1, 0.5]))
			# print ("Considering new situation [0.3, 0.1, 0.1, 0.5] -> ?: ", output)
			# hidden_state, output = neural_network.think(array([0.5, 0.2, 0.1, 0.5]))
			# print ("Considering [0.5, 0.2, 0.1, 0.5]", output)
			# hidden_state, output = neural_network.think(array([0.5, 0.1, 0.2, 0.5]))
			# print ("Considering [0.5, 0.1, 0.2, 0.5]", output)
			# hidden_state, output = neural_network.think(array([0.5, 0.1, 0.5, 0.5]))
			# print ("Considering [0.5, 0.1, 0.5, 0.5]", output)
			# hidden_state, output = neural_network.think(array([1.0, 0.5, 0.5, 0.5]))
			# print ("Considering [1.0, 0.1, 0.5, 0.5]", output)
			# hidden_state, output = neural_network.think(array([0.5, 0.3, 0.3, 0.5]))
			# print ("Considering [0.5, 0.3, 0.3, 0.5]", output)



if __name__ == "__main__":
	main()
