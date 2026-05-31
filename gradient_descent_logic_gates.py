import numpy as np

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y_and = np.array([[0],[0],[0],[1]])
y_or  = np.array([[0],[1],[1],[1]])

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def train(X, y, epochs=5000, lr=0.3):
    w = np.random.rand(2,1)
    b = np.random.rand(1)
    for epoch in range(epochs):
        z = np.dot(X, w) + b
        out = sigmoid(z)
        error = y - out
        w += lr * np.dot(X.T, error * out * (1 - out))
        b += lr * np.sum(error * out * (1 - out))
    return w, b

w_and, b_and = train(X, y_and)
w_or, b_or   = train(X, y_or)

print("Final predictions (AND vs OR):")
for i in range(len(X)):
    out_and = sigmoid(np.dot(X[i], w_and) + b_and)[0]
    out_or  = sigmoid(np.dot(X[i], w_or) + b_or)[0]
    print(f"{X[i]} -> AND: {out_and:.3f} (target {y_and[i][0]}), OR: {out_or:.3f} (target {y_or[i][0]})")
    