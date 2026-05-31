import pandas as pd
import numpy as np
import math

data = pd.read_csv("diabetes.csv")

# Train-test split
train = data.sample(frac=0.7, random_state=1)
test = data.drop(train.index)

summary = train.groupby(train.columns[-1]).agg(["mean", "std"])

# Gaussian probability
def gaussian(x, mean, std):
    return (1/(math.sqrt(2*math.pi)*std)) * math.exp(-((x-mean)**2)/(2*std**2))

def predict(row):
    probs = {}

    for c in summary.index:
        prob = 1
        for i in range(len(row)-1):
            mean = summary.iloc[c, i*2]
            std = summary.iloc[c, i*2+1]
            prob *= gaussian(row.iloc[i], mean, std)
        probs[c] = prob

    return max(probs, key=probs.get)

predictions = test.apply(predict, axis=1)

accuracy = (predictions.values == test.iloc[:,-1].values).mean()*100
print("Accuracy:", accuracy)
