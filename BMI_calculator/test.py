import tkinter as tk
from tkinter import ttk

root = tk.Tk()

year_combobox = ttk.Combobox(root, values=["2023", "2024"], state="readonly")
year_combobox.pack()

month1_combobox = None  # Define month1_combobox in the global scope

def on_Year_change(event=None):
    global month1_combobox
    
    selected_year = year_combobox.get()
    if selected_year == "2023" or selected_year == "2024":
        if month1_combobox is None:
            data_label = tk.Label(root, bg='white', text=", ")
            data_label.place(x=870, y=450)
            month1_options = ["All Months", 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
            month1_combobox = ttk.Combobox(root, values=month1_options, style='NoBorder.TCombobox', state="readonly")
            month1_combobox.set("Months")
            month1_combobox.place(x=880, y=450)
            # Bind the combobox change event
            month1_combobox.bind("<<ComboboxSelected>>", on_month1_change)
    else:
        print("Hello")
        if month1_combobox is not None:
            month1_combobox.destroy()
            month1_combobox = None

def on_month1_change(event=None):
    selected_month = month1_combobox.get()
    print("Selected Month:", selected_month)

year_combobox.bind("<<ComboboxSelected>>", on_Year_change)

root.mainloop()
