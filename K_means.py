def calculate_distance(point1, point2):
    return sum((point1[i] - point2[i]) ** 2 for i in range(len(point1))) ** 0.5

def initialize_centroids(data, k):
    return data[:k]

def assign_clusters(data, centroids):
    clusters = [[] for _ in centroids]
    for point in data:
        distances = [calculate_distance(point, centroid) for centroid in centroids]
        cluster_index = distances.index(min(distances))
        clusters[cluster_index].append(point)
    return clusters

def compute_new_centroids(clusters):
    new_centroids = []
    for cluster in clusters:
        if cluster:
            centroid = [sum(dim) / len(cluster) for dim in zip(*cluster)]
        else:
            centroid = [0] * len(clusters[0][0])
        new_centroids.append(centroid)
    return new_centroids

def k_means(data, k, max_iterations=100):
    centroids = initialize_centroids(data, k)
    for _ in range(max_iterations):
        clusters = assign_clusters(data, centroids)
        new_centroids = compute_new_centroids(clusters)
        if new_centroids == centroids:
            break
        centroids = new_centroids
    return centroids, clusters

# Example dataset
data_points = [
    [1, 5], [4, 2], [3, 6], [6, 7], [7, 5], [8, 10], [9, 3], [12, 4], [13, 6]
]

k = 3
final_centroids, final_clusters = k_means(data_points, k)

print("Final centroids:", final_centroids)
for i, cluster in enumerate(final_clusters):
    print(f"Cluster {i + 1}: {cluster}")
