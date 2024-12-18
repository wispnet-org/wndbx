import tkinter as tk
import webbrowser

def create_menu(root, app):
    menu = tk.Menu(root)
    root.config(menu=menu)

    profile_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Profile", menu=profile_menu)
    profile_menu.add_command(label="Create Profile", command=app.create_profile)
    profile_menu.add_command(label="Search by ID", command=app.search_by_id)

    help_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="Go to Site", command=lambda: webbrowser.open("http://wisp.wispnet.org/dbx"))
    help_menu.add_command(label="Contact Support", command=lambda: webbrowser.open("mailto:help@wispnet.org"))
