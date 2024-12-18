import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from db.database import Database
from ui.menu import create_menu
from ui.steps import StepManager

class ProfileApp:
    def __init__(self, root):
        print("Initializing ProfileApp...")  # Debug print to check initialization
        self.root = root
        self.root.title("Profile Creator")

        self.database = Database()
        self.data = {
            "firstname": tk.StringVar(),
            "middlename": tk.StringVar(),
            "lastname": tk.StringVar(),
            "age": tk.StringVar(),
            "dob_day": tk.StringVar(),
            "dob_month": tk.StringVar(),
            "dob_year": tk.StringVar(),
            "phone_numbers": [],
            "emails": [],
            "cars": []
        }

        self.container = ttk.Frame(self.root, padding=20)
        self.container.pack(fill=tk.BOTH, expand=True)

        self.step_manager = StepManager(
            self.container,
            self.data,
            steps=[
                self.step_landing_page,
                self.step_nameinfo,
                self.step_ageinfo,
                self.step_carinfo,
                self.step_contactinfo,
                # Add other steps here
            ]
        )

        create_menu(self.root, self)

        print("Displaying first step...")  # Debug print to confirm step display
        self.step_manager.show_step()

    def step_landing_page(self):
        ttk.Label(self.container, text="Welcome to the Profile Creator!", font=("Arial", 18, "bold")).pack(pady=10)
        ttk.Button(self.container, text="Create Profile", command=self.create_profile).pack(pady=10)
        ttk.Button(self.container, text="Search Profile by ID", command=self.search_by_id).pack(pady=10)
        ttk.Button(self.container, text="View Database", command=self.view_database).pack(pady=10)

    def step_nameinfo(self):
        ttk.Label(self.container, text="First Name:", font=("Arial", 14)).pack(pady=5)
        ttk.Entry(self.container, textvariable=self.data["firstname"]).pack(pady=5)
        
        ttk.Label(self.container, text="Middle Name:", font=("Arial", 14)).pack(pady=5)
        ttk.Entry(self.container, textvariable=self.data["middlename"]).pack(pady=5)
        
        ttk.Label(self.container, text="Last Name:", font=("Arial", 14)).pack(pady=5)
        ttk.Entry(self.container, textvariable=self.data["lastname"]).pack(pady=5)
        
        ttk.Button(self.container, text="Next", command=self.step_manager.next_step).pack(pady=10)

    def step_ageinfo(self):
        ttk.Label(self.container, text="Enter your age:", font=("Arial", 14)).pack(pady=10)
        ttk.Entry(self.container, textvariable=self.data["age"]).pack(pady=5)

        ttk.Label(self.container, text="Date of Birth (Day):", font=("Arial", 14)).pack(pady=5)
        ttk.Entry(self.container, textvariable=self.data["dob_day"]).pack(pady=5)
        
        ttk.Label(self.container, text="Date of Birth (Month):", font=("Arial", 14)).pack(pady=5)
        ttk.Entry(self.container, textvariable=self.data["dob_month"]).pack(pady=5)
        
        ttk.Label(self.container, text="Date of Birth (Year):", font=("Arial", 14)).pack(pady=5)
        ttk.Entry(self.container, textvariable=self.data["dob_year"]).pack(pady=5)

        ttk.Button(self.container, text="Next", command=self.step_manager.next_step).pack(pady=10)

    def step_carinfo(self):
        ttk.Label(self.container, text="How many cars do you have?", font=("Arial", 14)).pack(pady=10)
        num_cars = tk.IntVar()
        ttk.Entry(self.container, textvariable=num_cars).pack(pady=5)
        
        ttk.Button(self.container, text="Next", command=lambda: self.collect_car_info(num_cars.get())).pack(pady=10)

    def collect_car_info(self, num_cars):
        for i in range(num_cars):
            ttk.Label(self.container, text=f"Car {i+1} Model:", font=("Arial", 14)).pack(pady=5)
            model = tk.StringVar()
            ttk.Entry(self.container, textvariable=model).pack(pady=5)

            ttk.Label(self.container, text=f"Car {i+1} Make:", font=("Arial", 14)).pack(pady=5)
            make = tk.StringVar()
            ttk.Entry(self.container, textvariable=make).pack(pady=5)

            ttk.Label(self.container, text=f"Car {i+1} Plate Number:", font=("Arial", 14)).pack(pady=5)
            plate = tk.StringVar()
            ttk.Entry(self.container, textvariable=plate).pack(pady=5)

            self.data["cars"].append({"model": model, "make": make, "plate": plate})

        ttk.Button(self.container, text="Next", command=self.step_manager.next_step).pack(pady=10)

    def step_contactinfo(self):
        ttk.Label(self.container, text="Enter your phone numbers:", font=("Arial", 14)).pack(pady=10)
        phone = tk.StringVar()
        ttk.Entry(self.container, textvariable=phone).pack(pady=5)
        self.data["phone_numbers"].append(phone)

        ttk.Label(self.container, text="Enter your emails:", font=("Arial", 14)).pack(pady=10)
        email = tk.StringVar()
        ttk.Entry(self.container, textvariable=email).pack(pady=5)
        self.data["emails"].append(email)

        ttk.Button(self.container, text="Next", command=self.step_manager.next_step).pack(pady=10)

    def create_profile(self):
        print("Creating profile...")  # Debug print
        self.step_manager.next_step()  # Move to the next step or page

    def search_by_id(self):
        print("Searching by ID...")  # Debug print
        profile_id = simpledialog.askinteger("Search by ID", "Enter the profile ID:")
        if profile_id is not None:
            profile = self.database.fetch_profile_by_id(profile_id)
            if profile:
                messagebox.showinfo("Profile Found", f"Name: {profile[1]} {profile[2]} {profile[3]}")
            else:
                messagebox.showerror("Error", "Profile not found.")

    def view_database(self):
        print("Viewing database...")  # Debug print
        # Here you can implement the logic to view the list of database entries.
        pass

if __name__ == "__main__":
    print("Starting application...")  # Debug print
    root = tk.Tk()
    app = ProfileApp(root)
    root.mainloop()
