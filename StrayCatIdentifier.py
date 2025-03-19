import tkinter as tk
from tkinter import ttk, messagebox

class CatCoat:
    def __init__(self):
        self.coat_colors = ["Calico", "Tortoiseshell", "Tuxedo", "Black", "White", "Gray", "Tabby", "Orange", "Various"]
        self.coat_lengths = ["Shorthair", "Longhair"]

    def get_coat_color(self):
        return self.coat_colors

    def get_coat_length(self):
        return self.coat_lengths

class CatBehavior:
    def __init__(self):
        self.cat_types = ["Stray", "Feral", "Free-Roaming"]
        self.behavior_indicators = {
            "Stray": ["Approaches humans", "May meow", "Moves like a house cat", "Often alone"],
            "Feral": ["Avoids humans", "Less likely to meow", "Crawls or crouches", "Often in colonies"],
            "Free-Roaming": ["Varied behavior"]
        }

    def get_cat_types(self):
        return self.cat_types

    def get_behavior_indicators(self, cat_type):
        return self.behavior_indicators.get(cat_type, [])

class PuspinCharacteristics(CatCoat):
    def __init__(self):
        super().__init__()
        self.puspin_info = "Puspin (Pusang Pinoy): Common house cat in the Philippines."

    def get_puspin_info(self):
        return self.puspin_info

class StrayCatIdentifier(PuspinCharacteristics, CatBehavior):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Stray Cat Identifier")
        self.master.geometry("450x300") # Set window size
        self.master.configure(bg="#f0f0f0") # Set background color
        self.create_widgets()

    def create_widgets(self):
        # Coat Color
        tk.Label(self.master, text="Coat Color:", bg="#f0f0f0").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.color_var = tk.StringVar()
        self.color_combobox = ttk.Combobox(self.master, textvariable=self.color_var, values=self.get_coat_color())
        self.color_combobox.grid(row=0, column=1, padx=10, pady=5)

        # Coat Length
        tk.Label(self.master, text="Coat Length:", bg="#f0f0f0").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.length_var = tk.StringVar()
        self.length_combobox = ttk.Combobox(self.master, textvariable=self.length_var, values=self.get_coat_length())
        self.length_combobox.grid(row=1, column=1, padx=10, pady=5)

        # Cat Type
        tk.Label(self.master, text="Cat Type:", bg="#f0f0f0").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.type_var = tk.StringVar()
        self.type_combobox = ttk.Combobox(self.master, textvariable=self.type_var, values=self.get_cat_types())
        self.type_combobox.grid(row=2, column=1, padx=10, pady=5)
        self.type_combobox.bind("<<ComboboxSelected>>", self.update_behavior_list)

        # Behavior Indicators
        tk.Label(self.master, text="Behavior:", bg="#f0f0f0").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.behavior_listbox = tk.Listbox(self.master, height=5, width=40)
        self.behavior_listbox.grid(row=3, column=1, padx=10, pady=5)

        # Identify Button
        ttk.Button(self.master, text="Identify", command=self.identify_cat).grid(row=4, column=0, columnspan=2, pady=10)

        # Puspin Info
        tk.Label(self.master, text=self.get_puspin_info(), bg="#f0f0f0").grid(row=5, column=0, columnspan=2, pady=5)

    def update_behavior_list(self, event=None):
        self.behavior_listbox.delete(0, tk.END)
        selected_type = self.type_var.get()
        behaviors = self.get_behavior_indicators(selected_type)
        for behavior in behaviors:
            self.behavior_listbox.insert(tk.END, behavior)

    def identify_cat(self):
        color = self.color_var.get()
        length = self.length_var.get()
        cat_type = self.type_var.get()
        behaviors = [self.behavior_listbox.get(idx) for idx in self.behavior_listbox.curselection()]

        message = f"Cat Identification:\n\nCoat Color: {color}\nCoat Length: {length}\nCat Type: {cat_type}\nBehaviors: {', '.join(behaviors)}"
        messagebox.showinfo("Identification Result", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = StrayCatIdentifier(root)
    root.mainloop()
