import tkinter as tk

def show_menu():
    root = tk.Tk()
    root.title("Main Menu")
    
    label = tk.Label(root, text="Welcome to the App")
    label.pack()
    
    start_button = tk.Button(root, text="Start", command=start_process)
    start_button.pack()
    
    root.mainloop()

def start_process():
    print("Starting process...")
