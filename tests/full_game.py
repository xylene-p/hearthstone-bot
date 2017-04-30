# !/usr/bin/env python
import sys; sys.path.append("..")
from numpy import exp, array, random, dot
from NeuralNetwork import NeuralNetwork
from fireplace import cards # fireplace/fireplace/cards
from fireplace.exceptions import GameOver #fireplace/fireplace/exceptions.py
from fireplace.utils import play_full_game #fireplace/fireplace/utils.py

def test_full_game():
	try:
		play_full_game()
	except GameOver:
		print("Game completed normally.")

		# class GameOver(Exception):
		# 	pass

def foo():
	foo.counter += 1
	print(foo.counter)
	print("\n\n\n\n\n\n\n")
foo.counter = 0

def main():
	neural_network = NeuralNetwork()

	print("Random starting synaptic weights: {}".format(neural_network.synaptic_weights))

	neural_network.train(60000)

	cards.db.initialize()
	if len(sys.argv) > 1:
		numgames = sys.argv[1]
		if not numgames.isdigit():
			sys.stderr.write("Usage: %s [NUMGAMES]\n" % (sys.argv[0]))
			exit(1)
		for i in range(int(numgames)):
				test_full_game()
				foo()
	else:
		test_full_game()
		foo()


	print ("New synaptic weights after training: ")
	# print (neural_network.synaptic_weights)
	print ("Considering new situation [0.5, 0.1, 0.1, 0.1] -> ?: ", neural_network.think(array([0.5, 0.1, 0.1, 0.1])))
	print ("Considering new situation [0.3, 0.1, 0.1, 0.5] -> ?: ", neural_network.think(array([0.3, 0.1, 0.1, 0.5])))
	print ("Considering [0.5, 0.2, 0.1, 0.5]", neural_network.think(array([0.5, 0.2, 0.1, 0.5])))
	print ("Considering [0.5, 0.1, 0.2, 0.5]", neural_network.think(array([0.5, 0.1, 0.2, 0.5])))
	print ("Considering [0.5, 0.1, 0.5, 0.5]", neural_network.think(array([0.5, 0.1, 0.5, 0.5])))
	print ("Considering [1.0, 0.1, 0.5, 0.5]", neural_network.think(array([1.0, 0.5, 0.5, 0.5])))
	print ("Considering [0.5, 0.3, 0.3, 0.5]", neural_network.think(array([0.5, 0.3, 0.3, 0.5])))


if __name__ == "__main__":
	main()
