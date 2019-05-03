#Based on the Sebastian Lague Neural Networks YouTube Playlist

import numpy as np 

# Normal comment
#* Bright Comment
#! Fucking Comment
#? Chill digger comment
# TODO Be More Orange




class NeuralNetwork:

    # The class function creates weights and biases for a neural network from
    # a given set of input layer sizes    
    def __init__(self, layer_sizes):
        #! Create Weight Shapes using the input layer sizes
        weight_shapes = [(a,b) for a,b in zip(layer_sizes[1:], layer_sizes[:-1])]
        #! Make the weights, giving each value a random standard devation
        #! before slotting it into its position according to weight_shapes
        self.weights = [np.random.standard_normal(s)/s[1]**.5 for s in weight_shapes]
        #! Create biases and set them to 0
        self.biases = [np.zeros((s,1)) for s in layer_sizes[1:]]

    # the predicter, predictably, predicts
    def predict(self, a):
        #! performs matrix multiplacation between input a and the weights
        #! and adds the bias - then passes it through the activation func
        for w,b in zip(self.weights, self.biases):      
            a = self.activation(np.matmul(w,a) + b)
        return a
    

    # 
    def print_accuracy(self, images, labels):
        predictions = self.predict(images)
        #! This monster iterates through the predictions and labels and gives them a boolean value if they match
        #! if the prediction matches the label it gets a 1, otherwise 0
        #! Then the sum method adds them all up
        num_correct = sum([np.argmax(a) == np.argmax(b) for a,b in zip(predictions,labels)])
        #! Then, print the number that were correct compared to the amount of images there were, and the
        #! percentage that were right.
        print('{0}/{1} accuracy: {2}%'.format(num_correct, len(images), (num_correct/len(images))*100))
    
    @staticmethod
    def activation(x):
        #! sigmoid function for activation
        return 1/ (1 + np.exp(-x))

