import tkinter as tk
from tkinter import ttk
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
import time

def train_and_visualize_decision_tree(dataset_name):
    # Load dataset
    if dataset_name == "Iris":
        dataset = datasets.load_iris()
    elif dataset_name == "Digits":
        dataset = datasets.load_digits()
    elif dataset_name == "Wine":
        dataset = datasets.load_wine()
    elif dataset_name == "Breast Cancer":
        dataset = datasets.load_breast_cancer()
    else:
        return
    
    # Train decision tree
    clf = DecisionTreeClassifier()
    clf.fit(dataset.data, dataset.target)
    
    # Plot decision tree step by step
    plt.figure(figsize=(10, 7))
    for i in range(1, len(clf.tree_.children_left)):
        plot_tree(clf, filled=True, max_depth=i)
        plt.draw()
        plt.pause(0.5)  # Pause for 1 second after each step
        time.sleep(1)  
        plt.clf() 

def on_button_click():
    dataset_name = dataset_combobox.get()
    train_and_visualize_decision_tree(dataset_name)

root = tk.Tk()
root.title("Decision Tree Visualization")

# First page
first_page = ttk.Frame(root)
first_page.grid(row=0, column=0)

ttk.Label(first_page, text="Select Dataset:").grid(row=0, column=0)
datasets_list = ["Iris", "Digits", "Breast Cancer"]
dataset_combobox = ttk.Combobox(first_page, values=datasets_list)
dataset_combobox.grid(row=0, column=1)

next_button = ttk.Button(first_page, text="Next", command=on_button_click)
next_button.grid(row=1, column=0, columnspan=2)

root.mainloop()
