import math

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Weights and bias
w1, w2 = 0.5, 0.5
b = 0.1

# Test input
x1, x2 = 1, 1

# Feed Forward
net = x1 * w1 + x2 * w2 + b
output = sigmoid(net)

print("Input:", [x1, x2])
print("Predicted Output:", round(output, 4))
