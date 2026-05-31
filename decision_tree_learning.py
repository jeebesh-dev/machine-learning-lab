import math

data = [[ 'Sunny', 'Hot', 'High', 'Weak', 'No'],
        [ 'Sunny', 'Hot', 'High', 'Strong', 'No'],
        [ 'Overcast', 'Hot', 'High', 'Weak', 'Yes'],
        [ 'Rain', 'Mild', 'High', 'Weak', 'Yes'],
        [ 'Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
        [ 'Rain', 'Cool', 'Normal', 'Strong', 'No'],
        [ 'Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
        [ 'Sunny', 'Mild', 'High', 'Weak', 'No'],
        [ 'Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
        [ 'Rain', 'Mild', 'Normal', 'Weak', 'Yes'],
        [ 'Sunny', 'Mild', 'Normal', 'Strong', 'Yes'],
        [ 'Overcast', 'Mild', 'High', 'Strong', 'Yes'],
        [ 'Overcast', 'Hot', 'Normal', 'Weak', 'Yes'],
        [ 'Rain', 'Mild', 'High', 'Strong', 'No']]

attributes = ['Outlook', 'Temperature', 'Humidity', 'Wind']

def entropy(data):
    total = len(data)
   
    positive = sum(1 for row in data if row[-1] == 'Yes')
    negative = total - positive

    p_positive = positive / total
    p_negative = negative / total

    if p_positive == 0 or p_negative == 0:
        return 0

    return -p_positive * math.log2(p_positive) - p_negative * math.log2(p_negative)

def information_gain(data, attribute_index):
    total_entropy = entropy(data)
    subsets = {}
    
    for row in data:
        key = row[attribute_index]
        if key not in subsets:
            subsets[key] = []
        subsets[key].append(row)

    weighted_entropy = sum((len(subset) / len(data)) * entropy(subset) for subset in subsets.values())
    
    return total_entropy - weighted_entropy

def best_attribute(data):
    gains = [information_gain(data, i) for i in range(len(attributes))]
    best_index = gains.index(max(gains))
    return best_index, attributes[best_index]

best_index, best_attr = best_attribute(data)
print(f"Best attribute to split on: {best_attr})") 

def build_tree(data, attributes):
    if all(row[-1] == 'Yes' for row in data):
        return 'Yes'
    if all(row[-1] == 'No' for row in data):
        return 'No'
    
    best_index, best_attr = best_attribute(data)
    tree = {best_attr: {}}
    
    subsets = {}
    for row in data:
        key = row[best_index]
        if key not in subsets:
            subsets[key] = []
        subsets[key].append(row)

    for key, subset in subsets.items():
        tree[best_attr][key] = build_tree(subset, attributes)
    
    return tree

decision_tree = build_tree(data, attributes)
print("Decision Tree:", decision_tree)








