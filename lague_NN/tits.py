import fucking_argh as nn
import numpy as np 



# loading the data from npz file d/l from lague github
# https://github.com/SebLague/Mnist-data-numpy-format.git
# it's jsut the standard mnist that he repackaged for the tut

with np.load('mnist.npz') as data:
    training_images = data['training_images']
    training_labels = data['training_labels']


# if you print(training_images.shape) you get
# (50000, 784, 1)
# so you put the second bit in # ? why tho 

layer_sizes = (784,5,10)


net = nn.NeuralNetwork(layer_sizes)
net.print_accuracy(training_images,training_labels)

