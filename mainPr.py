import tkinter as tk
from tkinter import ttk

class FrontPage:
    def __init__(self, root):
        self.root = root
        self.root.title("VirtuVision")

        self.main_frame = ttk.Frame(root)
        self.main_frame.pack()

        self.select_label = ttk.Label(self.main_frame, text="Select Technology:")
        self.select_label.grid(row=0, column=0, padx=5, pady=5)

        self.visualization_combo = ttk.Combobox(self.main_frame, values=["K-Means Clustering", "Decision Tree", "Bayes Classifier", "KNN"])
        self.visualization_combo.grid(row=0, column=1, padx=5, pady=5)

        self.start_button = ttk.Button(self.main_frame, text="Start", command=self.start_visualization)
        self.start_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def start_visualization(self):
        selected_visualization = self.visualization_combo.get()
        if selected_visualization == "K-Means Clustering":
            self.run_kmeans_visualization()
        elif selected_visualization == "Decision Tree":
            self.run_decision_tree_visualization()
        elif selected_visualization == "Bayes Classifier":
            self.run_bayes_classifier_visualization()
        elif selected_visualization == "KNN":
            self.run_knn_visualization()

    def run_kmeans_visualization(self):
        import kmeans_visualization
        self.root.withdraw() 
        root_kmeans = tk.Toplevel()
        app_kmeans = kmeans_visualization.KMeansVisualizer(root_kmeans)

    def run_decision_tree_visualization(self):
        import decision_tree_visualization
        self.root.withdraw()  
        root_decision_tree = tk.Toplevel()
        app_decision_tree = decision_tree_visualization.DecisionTreeVisualizer(root_decision_tree)

    def run_bayes_classifier_visualization(self):
        import bayes_classifier_visualization
        self.root.withdraw()
        root_bayes = tk.Toplevel()
        app_bayes = bayes_classifier_visualization.BayesClassifierVisualization(root_bayes)

    def run_knn_visualization(self):
        import knn_visualization
        self.root.withdraw() 
        root_knn = tk.Toplevel()
        app_knn = knn_visualization.KNNVisualization(root_knn)

def main():
    root = tk.Tk()
    app = FrontPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
