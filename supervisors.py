import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class InstituteConfigurationApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Institute Configuration App")

        self.building_data = []
        self.room_data = []

        self.notebook = ttk.Notebook(root)
        self.building_tab = ttk.Frame(self.notebook)
        self.room_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.building_tab, text="Buildings")
        self.notebook.add(self.room_tab, text="Rooms")

        self.init_building_tab()
        self.init_room_tab()

        self.notebook.pack(expand=1, fill="both")

        self.center_window()

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_position = (screen_width - self.root.winfo_reqwidth()) / 2
        y_position = (screen_height - self.root.winfo_reqheight()) / 2

        self.root.geometry(f"+{int(x_position)}+{int(y_position)}")

    def init_building_tab(self):
        building_frame = ttk.LabelFrame(self.building_tab, text="Building Information")
        building_frame.grid(row=0, column=0, padx=10, pady=10)

        building_name_label = ttk.Label(building_frame, text="Building Name:")
        building_name_label.grid(row=0, column=0, sticky=tk.W)
        building_name_entry = ttk.Entry(building_frame)
        building_name_entry.grid(row=0, column=1, pady=5)

        add_building_button = ttk.Button(building_frame, text="Add Building", command=lambda: self.add_building(building_name_entry.get()))
        add_building_button.grid(row=1, column=0, columnspan=2, pady=10)

    def init_room_tab(self):
        room_frame = ttk.LabelFrame(self.room_tab, text="Room Information")
        room_frame.grid(row=0, column=0, padx=10, pady=10)

        room_number_label = ttk.Label(room_frame, text="Room Number:")
        room_number_label.grid(row=0, column=0, sticky=tk.W)
        room_number_entry = ttk.Entry(room_frame)
        room_number_entry.grid(row=0, column=1, pady=5)

        building_label = ttk.Label(room_frame, text="Building:")
        building_label.grid(row=1, column=0, sticky=tk.W)
        building_combobox = ttk.Combobox(room_frame, values=self.get_building_names())
        building_combobox.grid(row=1, column=1, pady=5)

        add_room_button = ttk.Button(room_frame, text="Add Room", command=lambda: self.add_room(room_number_entry.get(), building_combobox.get()))
        add_room_button.grid(row=2, column=0, columnspan=2, pady=10)

    def add_building(self, building_name):
        if not building_name:
            messagebox.showerror("Error", "Please enter a building name.")
            return
        self.building_data.append({"Building Name": building_name})
        messagebox.showinfo("Success", "Building added successfully!")

    def get_building_names(self):
        return [building["Building Name"] for building in self.building_data]

    def add_room(self, room_number, building):
        if not all([room_number, building]):
            messagebox.showerror("Error", "Please fill all the required fields.")
            return
        self.room_data.append({"Room Number": room_number, "Building": building})
        messagebox.showinfo("Success", "Room added successfully!")


if _name_ == "_main_":
    root = tk.Tk()
    app = InstituteConfigurationApp(root)
    root.mainloop()
