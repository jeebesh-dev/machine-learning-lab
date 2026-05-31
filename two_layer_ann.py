import random
import math

# Sigmoid activation
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Derivative of sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)

# Initialize weights randomly
def initialize_weights(n_inputs, n_hidden, n_outputs):
    hidden_weights = [[random.uniform(-1, 1) for _ in range(n_inputs)] for _ in range(n_hidden)]
    output_weights = [[random.uniform(-1, 1) for _ in range(n_hidden)] for _ in range(n_outputs)]
    return hidden_weights, output_weights

def forward_pass(inputs, hidden_weights, output_weights):
    # Hidden layer activations
    hidden_net = []
    hidden_out = []
    for h in hidden_weights:
        net = sum(i*w for i, w in zip(inputs, h))
        hidden_net.append(net)
        hidden_out.append(sigmoid(net))
    
    # Output layer activations
    output_net = []
    output_out = []
    for o in output_weights:
        net = sum(h*w for h, w in zip(hidden_out, o))
        output_net.append(net)
        output_out.append(sigmoid(net))
    
    return hidden_out, output_out

def backpropagation(inputs, targets, hidden_out, output_out, hidden_weights, output_weights, eta):
    # Output layer deltas
    output_deltas = []
    for t, o in zip(targets, output_out):
        delta = (t - o) * sigmoid_derivative(o)   # (t_j - o_j) o_j (1 - o_j)
        output_deltas.append(delta)
    
    # Hidden layer deltas
    hidden_deltas = []
    for j, h in enumerate(hidden_out):
        downstream = sum(output_deltas[k] * output_weights[k][j] for k in range(len(output_deltas)))
        delta = sigmoid_derivative(h) * downstream
        hidden_deltas.append(delta)
    
    # Update output weights
    for k in range(len(output_weights)):
        for j in range(len(output_weights[k])):
            output_weights[k][j] += eta * output_deltas[k] * hidden_out[j]
    
    # Update hidden weights
    for j in range(len(hidden_weights)):
        for i in range(len(hidden_weights[j])):
            hidden_weights[j][i] += eta * hidden_deltas[j] * inputs[i]
    
    return hidden_weights, output_weights

def train(X, Y, n_hidden=2, n_outputs=1, eta=0.5, epochs=10000):
    n_inputs = len(X[0])
    hidden_weights, output_weights = initialize_weights(n_inputs, n_hidden, n_outputs)
    
    for epoch in range(epochs):
        total_error = 0
        for inputs, targets in zip(X, Y):
            hidden_out, output_out = forward_pass(inputs, hidden_weights, output_weights)
            hidden_weights, output_weights = backpropagation(inputs, targets, hidden_out, output_out, hidden_weights, output_weights, eta)
            total_error += sum((t - o)**2 for t, o in zip(targets, output_out))
        
        if epoch % 1000 == 0:
            print(f"Epoch {epoch}, Error: {total_error}")
    
    return hidden_weights, output_weights

# XOR dataset
X = [[0,0],[0,1],[1,0],[1,1]]
Y = [[0],[1],[1],[0]]

hidden_weights, output_weights = train(X, Y, n_hidden=4, n_outputs=1, eta=0.3, epochs=10000)

# Test
for x in X:
    h_out, o_out = forward_pass(x, hidden_weights, output_weights)
    print(f"Input: {x}, Output: {o_out}")           




