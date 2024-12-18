import tkinter as tk
from tkinter import ttk

class StepManager:
    def __init__(self, container, data, steps):
        self.container = container
        self.data = data
        self.steps = steps
        self.current_step = 0

    def clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def show_step(self):
        if self.current_step < len(self.steps):
            self.clear_container()
            self.steps[self.current_step]()
        else:
            self.complete_steps()

    def next_step(self):
        if self.current_step < len(self.steps) - 1:
            self.current_step += 1
            self.show_step()

    def prev_step(self):
        if self.current_step > 0:
            self.current_step -= 1
            self.show_step()

    def reset_steps(self):
        self.current_step = 0
        self.show_step()

    def complete_steps(self):
        ttk.Label(self.container, text="Profile Creation Completed!", font=("Arial", 18, "bold")).pack(pady=10)
