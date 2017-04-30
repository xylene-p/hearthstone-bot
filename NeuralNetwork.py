from numpy import exp, array, random, dot
class NeuralNetwork():
    def __init__(self):
        random.seed(1)

        self.synaptic_weights = 2 * random.random((4, 1)) - 1

        # based on inputs if ally attack is high attack the face
        # Ally Attack, Ally Health, Enemy Attack, Enemy Health
        self.training_set_inputs = array([[0.1, 0.1, 0.1, 0.1], [0.1, 0.1, 0.2, 0.1], [0.1, 0.1, 0.3, 0.1],
        [0.2, 0.1, 0.1, 0.1], [0.2, 0.1, 0.2, 0.1], [0.2, 0.1, 0.3, 0.1],
        [0.3, 0.1, 0.1, 0.2], [0.3, 0.1, 0.2, 0.1], [0.3, 0.1, 0.1, 0.1],
        [0.1, 0.1, 0.1, 0.2], [0.1, 0.1, 0.1, 0.3],
        [0.2, 0.1, 0.1, 0.2], [0.2, 0.1, 0.1, 0.3],
        [0.3, 0.1, 0.1, 0.2], [0.3, 0.1, 0.1, 0.3],
        [0.1, 0.2, 0.1, 0.1], [0.1, 0.2, 0.2, 0.1], [0.1, 0.2, 0.3, 0.1],
        [0.2, 0.2, 0.1, 0.1], [0.2, 0.2, 0.2, 0.1], [0.2, 0.2, 0.3, 0.1],
        [0.3, 0.2, 0.1, 0.2], [0.3, 0.2, 0.2, 0.1], [0.3, 0.2, 0.1, 0.1],
        [0.1, 0.2, 0.1, 0.2], [0.1, 0.2, 0.1, 0.3],
        [0.2, 0.2, 0.1, 0.2], [0.2, 0.2, 0.1, 0.3],
        [0.3, 0.2, 0.1, 0.2], [0.3, 0.2, 0.1, 0.3],
        [0.1, 0.5, 0.1, 0.1], [0.1, 0.5, 0.2, 0.1], [0.1, 0.5, 0.3, 0.1],
        [0.2, 0.5, 0.1, 0.1], [0.2, 0.5, 0.2, 0.1], [0.2, 0.5, 0.3, 0.1],
        [0.3, 0.5, 0.1, 0.2], [0.3, 0.5, 0.2, 0.1], [0.3, 0.5, 0.1, 0.1],
        [0.1, 0.5, 0.1, 0.2], [0.1, 0.5, 0.1, 0.3],
        [0.2, 0.5, 0.1, 0.2], [0.2, 0.5, 0.1, 0.3],
        [0.3, 0.5, 0.1, 0.2], [0.3, 0.5, 0.1, 0.3],
        [0.1, 0.2, 0.1, 0.5], [0.1, 0.2, 0.2, 0.5], [0.1, 0.2, 0.3, 0.5],
        [0.2, 0.2, 0.1, 0.5], [0.2, 0.2, 0.2, 0.5], [0.2, 0.2, 0.3, 0.5],
        [0.3, 0.2, 0.1, 0.5], [0.3, 0.2, 0.2, 0.5], [0.3, 0.2, 0.3, 0.5],
        [0.5, 0.1, 0.3, 0.5], [0.1, 0.4, 0.2, 0.5],
        [0.2, 0.3, 0.1, 0.5], [0.2, 0.4, 0.2, 0.5],
        [0.5, 0.3, 0.3, 0.5], [0.5, 0.4, 0.3, 0.5]])

        # if output == 0 # do not go for face
        # if output == 1 # attack the face

        self.training_set_outputs = array([[0, 0, 0,
        1, 0, 0,
        1, 1, 1,
        0, 0,
        1, 0,
        1, 0,
        0, 0, 0,
        0, 0, 0,
        0, 0, 1,
        1, 1,
        0, 1,
        1, 1,
        0, 1, 0,
        1, 0, 0,
        0, 0, 1,
        1, 1,
        0, 1,
        1, 1,
        1, 1, 1,
        1, 0, 0,
        1, 1, 0,
        1, 1,
        0, 1,
        1, 1]]).T

    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, number_of_training_iterations):
        training_set_inputs = self.training_set_inputs
        training_set_outputs = self.training_set_outputs
        for iteration in range(number_of_training_iterations):
            output = self.think(training_set_inputs)

            error = training_set_outputs - output

            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))

            self.synaptic_weights += adjustment

    def think(self, inputs):
        # Pass inputs through our neural network (our single neuron).
        return self.__sigmoid(dot(inputs, self.synaptic_weights))

    def set_training_set_inputs(self, inputs):
        self.training_set_inputs = inputs

    # def converter(self, stats):
    #

    # def learnFromPrevGame(input, output):
    #     input
