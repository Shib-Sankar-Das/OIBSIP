import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def show_blank_graph():
    fig, ax = plt.subplots()
    ax.set_title("Blank Graph", fontsize=20)
    ax.set_xlabel("X Axis", fontsize=10)
    ax.set_ylabel("Y Axis", fontsize=10)

    canvas = FigureCanvasTkAgg(fig, frame1)
    canvas.draw()
    canvas.get_tk_widget().config(width=frame1['width'], height=frame1['height'])
    canvas.get_tk_widget().pack()

# Create a tkinter window and a frame
root = tk.Tk()
root.geometry("600x400")
frame1 = tk.Frame(root)
frame1.pack(fill=tk.BOTH, expand=True)

# Call the function to show the blank graph
show_blank_graph()

# Run the tkinter event loop
root.mainloop()






from datetime import datetime

def get_month_name(date_str):
    try:
        # Parse the date string to a datetime object
        date_object = datetime.strptime(date_str, '%Y-%m-%d')
        
        # Extract the month from the datetime object
        month_number = date_object.month
        
        # Get the month name as a string
        month_name = date_object.strftime('%B')
        
        return month_name
    except ValueError:
        return "Invalid date format"

# Example usage:
date_str = '2004-5-18'
month_name = get_month_name(date_str)
print("Month Name:", month_name)





# Dictionary with keys as numerical integers in string format
integer_string_dict = {'5': 'apple', '3': 'banana', '10': 'orange', '1': 'grape'}

# Sorting the dictionary by keys and updating the original dictionary
integer_string_dict.clear()  # Clearing the original dictionary
integer_string_dict.update({k: integer_string_dict[k] for k in sorted(sorted_dict.keys(), key=lambda x: int(x))})

print("Sorted dictionary stored in the same dictionary:", integer_string_dict)
