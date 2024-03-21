import tkinter as tk
import random
import time

class BayesClassifierVisualization:
    def __init__(self, master):
        self.master = master
        self.master.title("Bayes Classifier Visualization")
        self.canvas = tk.Canvas(master, width=600, height=400)
        self.canvas.pack()
        self.points = []
        self.colors = ['red', 'blue', 'green']
        self.summary_label = tk.Label(master, text="Summary:")
        self.summary_label.pack()
        self.summary_text = tk.Text(master, height=4, width=50)
        self.summary_text.pack()
        self.start_button = tk.Button(master, text="Start Bayes Classification", command=self.start_classification)
        self.start_button.pack()

    def generate_random_points(self, num_points):
        self.points = []
        for _ in range(num_points):
            x = random.randint(50, 550)
            y = random.randint(50, 350)
            self.points.append((x, y))

    def visualize_point(self, point, color):
        x, y = point
        self.canvas.create_oval(x-3, y-3, x+3, y+3, fill=color)

    def classify_points(self):
        self.summary_text.delete(1.0, tk.END)
        classifications = []
        for point in self.points:
            classification = random.choice(self.colors)
            classifications.append((point, classification))
        for point, classification in classifications:
            self.visualize_point(point, classification)
            time.sleep(0.5)
            self.canvas.update()
            self.summary_text.insert(tk.END, f"Point at {point} is classified as {classification}\n")
            self.summary_text.see(tk.END)

    def start_classification(self):
        self.canvas.delete("all")
        self.generate_random_points(20)
        for point in self.points:
            self.visualize_point(point, 'black')  # Visualize points in black initially
        self.canvas.update()
        self.classify_points()

def main():
    root = tk.Tk()
    app = BayesClassifierVisualization(root)
    root.mainloop()

if __name__ == "__main__":
    main()
