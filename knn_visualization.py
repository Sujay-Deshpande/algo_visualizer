import tkinter as tk
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import time

class KNNVisualization:
    def __init__(self, master):
        self.master = master
        self.master.title("KNN Visualization")
        self.canvas = tk.Canvas(master, width=600, height=600)
        self.canvas.pack()
        
        self.summary_label = tk.Label(master, text="")
        self.summary_label.pack()
        
        self.generate_data_button = tk.Button(master, text="Generate Random Data", command=self.generate_and_plot_data)
        self.generate_data_button.pack()

        self.classification_button = tk.Button(master, text="Start Classification", command=self.start_classification)
        self.classification_button.pack()

        self.data_points = None
        self.clf = None

    def generate_random_data(self):
        np.random.seed(int(time.time()))  
        X1 = np.random.rand(50, 2)
        X2 = np.random.rand(50, 2) + np.array([1.5, 1.5])
        X = np.concatenate((X1, X2))
        y = np.array([0] * 50 + [1] * 50)
        return X, y

    def generate_and_plot_data(self):
        self.data_points = self.generate_random_data()
        self.plot_data_points()
        self.clf = None 
        self.classification_button.config(state=tk.NORMAL) 

    def plot_data_points(self):
        self.canvas.delete("all")  
        point_size = 7
        for i, point in enumerate(self.data_points[0]):
            color = 'blue' if self.data_points[1][i] == 0 else 'red'
            x, y = point
            self.canvas.create_oval(x * 500, y * 500, x * 500 + point_size, y * 500 + point_size, fill=color)

    def start_classification(self):
        if self.data_points is None:
            self.generate_and_plot_data()
        self.classification_button.config(state=tk.DISABLED) 
        self.clf = KNeighborsClassifier(n_neighbors=3)
        self.clf.fit(self.data_points[0], self.data_points[1])
        X_test = np.random.rand(20, 2) * 2
        self.plot_classification(X_test)

    def plot_classification(self, X_test):
        if self.clf is None:
            return  
        point_size = 7
        for i, point in enumerate(X_test):
            time.sleep(1)  
            color = 'green' if self.clf.predict([point])[0] == 0 else 'yellow'
            x, y = point
            self.canvas.create_oval(x * 500, y * 500, x * 500 + point_size, y * 500 + point_size, fill=color)
            self.summary_label.config(text=f"Classification: {i+1}/{len(X_test)}")
            self.master.update()
            print(f"Classification {i+1}/{len(X_test)}: Predicted class - {self.clf.predict([point])[0]}")
            print(f"Point: {point}")

        self.classification_button.config(state=tk.NORMAL) 

root = tk.Tk()
app = KNNVisualization(root)
root.mainloop()
