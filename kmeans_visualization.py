# Hello Everyone Today we are going to see hoe K-means algo. works in the visulizer......
# We will use the tkinter library and we will perform the operation on the random data points..... 
# So lets get started.......!

import tkinter as tk
import numpy as np
import random
import time

class KMeansVisualizer:
    def __init__(self, root, width=800, height=600, num_clusters=3, num_points=100):
        self.root = root
        self.width = width
        self.height = height
        self.num_clusters = num_clusters
        self.num_points = num_points
        self.canvas = tk.Canvas(root, width=width, height=height, bg="white")
        self.canvas.pack()
        self.points = []
        self.centroids = []
        self.clusters = [[] for _ in range(num_clusters)]
        self.colors = ["red", "green", "blue", "orange", "purple", "cyan", "magenta", "yellow"]
        self.steps = []

        self.start_button = tk.Button(root, text="Start K-Means", command=self.run_kmeans)
        self.start_button.pack()

    def generate_random_points(self):
        self.points = [(random.uniform(50, self.width - 50), random.uniform(50, self.height - 50)) for _ in range(self.num_points)]
        print("Generated Random Points:")
        for point in self.points:
            print(point)

    def initialize_centroids(self):
        self.centroids = [(random.uniform(50, self.width - 50), random.uniform(50, self.height - 50)) for _ in range(self.num_clusters)]
        print("Initialized Centroids:")
        for centroid in self.centroids:
            print(centroid)

    def distance(self, p1, p2):
        dist = np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        print(f"Distance between {p1} and {p2}: {dist}")
        return dist

    def assign_points_to_clusters(self):
        self.clusters = [[] for _ in range(self.num_clusters)]
        for point in self.points:
            min_dist = float('inf')
            closest_cluster = None
            for i, centroid in enumerate(self.centroids):
                dist = self.distance(point, centroid)
                if dist < min_dist:
                    min_dist = dist
                    closest_cluster = i
            self.clusters[closest_cluster].append(point)
        print("Points Assigned to Clusters:")
        self.print_clusters()

    def update_centroids(self):
        for i in range(self.num_clusters):
            if len(self.clusters[i]) > 0:
                new_centroid = (np.mean([point[0] for point in self.clusters[i]]),
                                np.mean([point[1] for point in self.clusters[i]]))
                self.steps.append(f"Moved centroid {i+1} to {new_centroid}")
                self.centroids[i] = new_centroid
        print("Updated Centroids:")
        self.print_centroids()

    def draw_points(self):
        for i in range(self.num_clusters):
            for point in self.clusters[i]:
                self.canvas.create_oval(point[0] - 2, point[1] - 2, point[0] + 2, point[1] + 2, fill=self.colors[i])

    def draw_centroids(self):
        for i, centroid in enumerate(self.centroids):
            self.canvas.create_rectangle(centroid[0] - 4, centroid[1] - 4, centroid[0] + 4, centroid[1] + 4, fill="black")

    def draw_clusters(self):
        for i in range(self.num_clusters):
            for point in self.clusters[i]:
                self.canvas.create_oval(point[0] - 2, point[1] - 2, point[0] + 2, point[1] + 2, fill=self.colors[i])
                self.canvas.create_line(point[0], point[1], self.centroids[i][0], self.centroids[i][1], fill=self.colors[i])

    def run_kmeans(self): # This method will run the actual algorithm in the backend
        self.generate_random_points()
        self.initialize_centroids()
        self.canvas.delete("all")
        self.draw_points()
        self.draw_centroids()
        self.root.update()
        time.sleep(2) # These are the actual view before making any changes...

        for iteration in range(10):
            print(f"Iteration {iteration + 1}:")
            self.assign_points_to_clusters()
            self.draw_points()
            self.draw_centroids()
            self.root.update()
            time.sleep(2)

            self.update_centroids()
            self.canvas.delete("all")
            self.draw_clusters()
            self.draw_centroids()
            self.root.update()
            time.sleep(2)

        self.show_summary()

    def print_clusters(self):
        for i, cluster in enumerate(self.clusters):
            print(f"Cluster {i + 1}: {cluster}")

    def print_centroids(self): # Using this method the centroid will located 
        for i, centroid in enumerate(self.centroids):
            print(f"Centroid {i + 1}: {centroid}")

    def show_summary(self):
        summary_window = tk.Toplevel(self.root)
        summary_window.title("Data Summary")

        summary_canvas = tk.Canvas(summary_window, width=1600, height=900, bg="white")
        summary_canvas.pack()


        summary_canvas.create_text(50, 20, text="Cluster", anchor=tk.W)
        summary_canvas.create_text(200, 20, text="Centroid", anchor=tk.W)
        summary_canvas.create_text(350, 20, text="Points", anchor=tk.W)

        for i in range(self.num_clusters):
            summary_canvas.create_text(50, 40 + 20 * i, text=f"{i+1}", anchor=tk.W)
            summary_canvas.create_text(200, 40 + 20 * i, text=f"({self.centroids[i][0]:.2f}, {self.centroids[i][1]:.2f})", anchor=tk.W)
            summary_canvas.create_text(350, 40 + 20 * i, text=f"{len(self.clusters[i])}", anchor=tk.W)

        summary_canvas.create_text(50, 40 + 20 * self.num_clusters, text="Total:", anchor=tk.W)
        summary_canvas.create_text(350, 40 + 20 * self.num_clusters, text=f"{sum(len(cluster) for cluster in self.clusters)}", anchor=tk.W)

        summary_canvas.create_text(50, 100 + 20 * self.num_clusters, text="Steps:", anchor=tk.W)
        for i, step in enumerate(self.steps):
            summary_canvas.create_text(50, 120 + 20 * (self.num_clusters + i), text=f"{i + 1}. {step}", anchor=tk.W)

def main():
    root = tk.Tk()
    root.title("K-Means Clustering Visualizer")
    app = KMeansVisualizer(root)
    root.mainloop() 

if __name__ == "__main__":
    main()
