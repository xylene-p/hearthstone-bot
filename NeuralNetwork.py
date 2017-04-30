from numpy import exp, array, random, dot
import numpy as np
class NeuralNetwork():
    def __init__(self, layer1, layer2):
        self.layer1 = layer1
        self.layer2 = layer2
        random.seed(1)

    # based on inputs if ally attack is high attack the face
    # Ally Attack, Ally Health, Enemy Attack, Enemy Health
        self.training_set_inputs = array([[0.1, 0.1, 0.1, 0.1], [0.1, 0.1, 0.1, 0.3], [0.1, 0.1, 0.1, 0.5], [0.1, 0.1, 0.1, 0.7],
                                 [0.3, 0.1, 0.1, 0.1], [0.3, 0.1, 0.1, 0.2], [0.3, 0.1, 0.1, 0.4], [0.3, 0.1, 0.1, 0.6],
                                 [0.5, 0.1, 0.1, 0.1], [0.5, 0.1, 0.1, 0.3], [0.5, 0.1, 0.1, 0.5], [0.5, 0.1, 0.1, 0.7],
                                 [0.8, 0.1, 0.1, 0.1], [0.8, 0.1, 0.1, 0.2], [0.8, 0.1, 0.1, 0.4], [0.8, 0.1, 0.1, 0.6],
                                 [0.1, 0.3, 0.1, 0.1], [0.1, 0.3, 0.1, 0.3], [0.1, 0.3, 0.1, 0.5], [0.1, 0.3, 0.1, 0.7],
                                 [0.3, 0.3, 0.1, 0.1], [0.3, 0.3, 0.1, 0.3], [0.3, 0.3, 0.1, 0.5], [0.3, 0.3, 0.1, 0.7],
                                 [0.5, 0.3, 0.1, 0.1], [0.5, 0.3, 0.1, 0.3], [0.5, 0.3, 0.1, 0.5], [0.5, 0.3, 0.1, 0.7],
                                 [0.8, 0.3, 0.1, 0.1], [0.8, 0.3, 0.1, 0.3], [0.8, 0.3, 0.1, 0.5], [0.8, 0.3, 0.1, 0.7],
                                 [0.1, 0.1, 0.3, 0.1], [0.1, 0.1, 0.3, 0.3], [0.1, 0.1, 0.3, 0.5], [0.1, 0.1, 0.3, 0.7],
                                 [0.3, 0.1, 0.3, 0.1], [0.3, 0.1, 0.3, 0.3], [0.3, 0.1, 0.3, 0.5], [0.3, 0.1, 0.3, 0.7],
                                 [0.5, 0.1, 0.3, 0.1], [0.5, 0.1, 0.3, 0.3], [0.5, 0.1, 0.3, 0.5], [0.5, 0.1, 0.3, 0.7],
                                 [0.8, 0.1, 0.3, 0.1], [0.8, 0.1, 0.3, 0.3], [0.8, 0.1, 0.3, 0.5], [0.8, 0.1, 0.3, 0.7],
                                 [0.1, 0.3, 0.3, 0.1], [0.1, 0.3, 0.3, 0.3], [0.1, 0.3, 0.3, 0.5], [0.1, 0.3, 0.3, 0.7],
                                 [0.3, 0.3, 0.3, 0.1], [0.3, 0.3, 0.3, 0.3], [0.3, 0.3, 0.3, 0.5], [0.3, 0.3, 0.3, 0.7],
                                 [0.5, 0.3, 0.3, 0.1], [0.5, 0.3, 0.3, 0.3], [0.5, 0.3, 0.3, 0.5], [0.5, 0.3, 0.3, 0.7],
                                 [0.8, 0.3, 0.3, 0.1], [0.8, 0.3, 0.3, 0.3], [0.8, 0.3, 0.3, 0.5], [0.8, 0.3, 0.3, 0.7],
                                 [0.1, 0.5, 0.6, 0.1], [0.1, 0.5, 0.6, 0.3], [0.1, 0.5, 0.6, 0.5], [0.1, 0.5, 0.6, 0.7],
                                 [0.3, 0.5, 0.6, 0.1], [0.3, 0.5, 0.6, 0.3], [0.3, 0.5, 0.6, 0.5], [0.3, 0.5, 0.6, 0.7],
                                 [0.5, 0.5, 0.6, 0.1], [0.5, 0.5, 0.6, 0.3], [0.5, 0.5, 0.6, 0.5], [0.5, 0.5, 0.6, 0.7],
                                 [0.8, 0.5, 0.6, 0.1], [0.8, 0.5, 0.6, 0.3], [0.8, 0.5, 0.6, 0.5], [0.8, 0.5, 0.6, 0.7]])

    # if output == 0 # do not go for face
    # if output == 1 # attack the face
        self.training_set_outputs = array([[0, 1, 1, 1,
                                   1, 1, 1, 1,
                                   1, 1, 1, 1,
                                   1, 1, 1, 1,
                                   0, 1, 1, 1,
                                   0, 0, 1, 1,
                                   1, 0, 0, 1,
                                   1, 1, 1, 0,
                                   0, 1, 1, 1,
                                   0, 0, 1, 1,
                                   0, 0, 0, 1,
                                   1, 1, 1, 0,
                                   0, 1, 1, 1,
                                   1, 0, 1, 1,
                                   1, 1, 0, 1,
                                   1, 1, 0, 0,
                                   0, 1, 1, 1,
                                   0, 0, 1, 1,
                                   1, 1, 0, 1,
                                   1, 1, 1, 1]]).T


    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))
    def __sigmoid_derivative(self, x):
        return x * (1 - x)


    def train(self, number_of_training_iterations):
        training_set_inputs = self.training_set_inputs
        training_set_outputs = self.training_set_outputs
        for iteration in range(number_of_training_iterations):
            output_from_layer_1, output_from_layer_2 = self.think(training_set_inputs)

            layer2_error = training_set_outputs - output_from_layer_2
            layer2_delta = layer2_error * self.__sigmoid_derivative(output_from_layer_2)

            layer1_error = layer2_delta.dot(self.layer2.synaptic_weights.T)
            layer1_delta = layer1_error * self.__sigmoid_derivative(output_from_layer_1)

            layer1_adjustment = training_set_inputs.T.dot(layer1_delta)
            layer2_adjustment = output_from_layer_1.T.dot(layer2_delta)

            self.layer1.synaptic_weights += layer1_adjustment
            self.layer2.synaptic_weights += layer2_adjustment

    def think(self, inputs):
        output_from_layer1 = self.__sigmoid(dot(inputs, self.layer1.synaptic_weights))
        output_from_layer2 = self.__sigmoid(dot(output_from_layer1, self.layer2.synaptic_weights))
        return output_from_layer1, output_from_layer2


    def learnFromPrevGame(self, ninput, noutput):
        self.training_set_inputs = np.vstack((self.training_set_inputs, ninput))
        self.training_set_outputs = np.vstack((self.training_set_outputs, noutput))
