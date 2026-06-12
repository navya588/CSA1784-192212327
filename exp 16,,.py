import math
import random

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Derivative of sigmoid
def sigmoid_derivative(y):
    return y * (1 - y)

# Training data (OR gate)
X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

Y = [0, 1, 1, 1]

# Initialize weights and biases
random.seed(1)

w1 = random.random()
w2 = random.random()
w3 = random.random()
w4 = random.random()

b1 = random.random()
b2 = random.random()

w5 = random.random()
w6 = random.random()
b3 = random.random()

learning_rate = 0.5

# Training
for epoch in range(10000):

    for i in range(len(X)):
        x1, x2 = X[i]
        target = Y[i]

        # Forward Pass
        h1 = sigmoid(x1 * w1 + x2 * w2 + b1)
        h2 = sigmoid(x1 * w3 + x2 * w4 + b2)

        output = sigmoid(h1 * w5 + h2 * w6 + b3)

        # Error
        error = target - output

        # Backpropagation
        d_output = error * sigmoid_derivative(output)

        d_h1 = d_output * w5 * sigmoid_derivative(h1)
        d_h2 = d_output * w6 * sigmoid_derivative(h2)

        # Update output layer weights
        w5 += learning_rate * d_output * h1
        w6 += learning_rate * d_output * h2
        b3 += learning_rate * d_output

        # Update hidden layer weights
        w1 += learning_rate * d_h1 * x1
        w2 += learning_rate * d_h1 * x2
        b1 += learning_rate * d_h1

        w3 += learning_rate * d_h2 * x1
        w4 += learning_rate * d_h2 * x2
        b2 += learning_rate * d_h2

# Testing
print("Feed Forward Neural Network Output:")

for i in range(len(X)):
    x1, x2 = X[i]

    h1 = sigmoid(x1 * w1 + x2 * w2 + b1)
    h2 = sigmoid(x1 * w3 + x2 * w4 + b2)

    output = sigmoid(h1 * w5 + h2 * w6 + b3)

    print(X[i], "->", round(output, 4))
