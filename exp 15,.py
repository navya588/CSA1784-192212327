import math

# Dataset: [Feature, Class]
data = [[2,0], [4,0], [6,1], [8,1]]

# Entropy
def entropy(labels):
    p = sum(labels) / len(labels)
    if p == 0 or p == 1:
        return 0
    return -p*math.log2(p) - (1-p)*math.log2(1-p)

# Find best split
labels = [row[1] for row in data]
parent_entropy = entropy(labels)

best_gain = -1
best_threshold = None

for threshold in [3, 5, 7]:
    left = [r[1] for r in data if r[0] <= threshold]
    right = [r[1] for r in data if r[0] > threshold]

    gain = parent_entropy - (
        len(left)/len(labels)*entropy(left) +
        len(right)/len(labels)*entropy(right)
    )

    if gain > best_gain:
        best_gain = gain
        best_threshold = threshold

print("Best Split:", best_threshold)

# Prediction
x = 5
if x <= best_threshold:
    print("Class = 0")
else:
    print("Class = 1")
