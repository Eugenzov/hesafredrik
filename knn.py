import math

# Sample data
data = open(r"siren_data_train.csv")
data = data.read()
data = data.split("\n")
for i in range(1,len(data)):
    data[i] = data[i].split(",")
    for j in range(len(data[i])):
        data[i][j] = float(data[i][j])

# Function to calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    distance = 0
    temp = 0
    for i in range(6,7):
        if i != 4:
            distance += (point1[i] - point2[i-temp]) ** 2
        else:
            temp = 1
    return math.sqrt(distance)

# Function to get k nearest neighbors
def get_neighbors(train_data, test_instance, k):
    distances = []
    for train_instance in train_data:
        dist = euclidean_distance(train_instance[1:], test_instance[1:])
        distances.append((train_instance, dist))
    distances.sort(key=lambda x: x[1])
    neighbors = []
    for i in range(k):
        neighbors.append(distances[i][0])

    return neighbors

# Function to make prediction based on k nearest neighbors
def predict_classification(neighbors):
    counts = {}
    for neighbor in neighbors:
        response = neighbor[4]
        if response in counts:
            counts[response] += 1
        else:
            counts[response] = 1
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts[0][0]

# Function to predict if the person hears the signal or not
def predict_hearing_signal(train_data, test_instance, k):
    neighbors = get_neighbors(train_data, test_instance, k)
    prediction = predict_classification(neighbors)
    if prediction == test_instance[4]:
        return 1
    else:
        return 0

counter = 0
test_len = 156

for i in range(1,test_len):
    result = predict_hearing_signal(data[test_len:], data[i], k=7)
    if result == 1:
        counter += 1
print(counter / test_len)
