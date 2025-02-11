def calculate_distance(point1, point2):
    return sum((point1[i] - point2[i]) ** 2 for i in range(len(point1))) ** 0.5

def knn_classify(data, labels, query, k):
    distances = [(calculate_distance(query, point), label) for point, label in zip(data, labels)]
    distances.sort(key=lambda x: x[0])
    k_nearest_labels = [label for _, label in distances[:k]]
    return max(set(k_nearest_labels), key=k_nearest_labels.count)

# Example dataset
data_points = [
    [2, 3], [3, 3], [3, 4], [5, 8], [6, 8], [7, 9], [10, 2], [10, 3], [11, 3]
]
labels = ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C']

query_point = [4, 4]
k = 3
predicted_label = knn_classify(data_points, labels, query_point, k)

print("Predicted label for", query_point, ":", predicted_label)
