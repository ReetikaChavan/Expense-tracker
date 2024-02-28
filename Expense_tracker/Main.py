import tkinter as tk
from tkinter import messagebox, font as tkFont
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Function to open the next window
def open_next_window():
    new_window()

# Function to create and customize widgets for the next window
def new_window():
    # Create the main application window
    next_window = tk.Toplevel(root)
    next_window.geometry('400x400')
    next_window.title("Next Window")

    # Create a frame within the new window
    frame = tk.Frame(next_window, bg="lightblue")  # Set the background color here

    # Pack the frame to fill the entire window
    frame.pack(fill=tk.BOTH, expand=True)

    # Create and customize widgets using grid in the new window
    label_font = tkFont.Font(family="Arial Black", size=12)  # Create a Font object for labels
    entry_font = tkFont.Font(family="Arial", size=12)  # Create a Font object for entry widgets
    
    L1 = tk.Label(frame, text="Expense name", font=label_font, fg="black")  # Set text color here
    L1.grid(row=0, column=0, padx=10, pady=10)

    L2 = tk.Label(frame, text="Amount", font=label_font, fg="black")  # Set text color here
    L2.grid(row=1, column=0, padx=10, pady=10)

    E1 = tk.Entry(frame, font=entry_font)
    E1.grid(row=0, column=1, padx=10, pady=10)

    E2 = tk.Entry(frame, font=entry_font)
    E2.grid(row=1, column=1, padx=10, pady=10)

    # Button to add expense
    add_button = tk.Button(frame, text="Add Expense", font=label_font, command=lambda: add_expense(E1.get(), E2.get()))
    add_button.grid(row=2, column=0, padx=10, pady=20)

    # Button to generate pie chart
    pie_chart_button = tk.Button(frame, text="Generate Pie Chart", font=label_font, bg='lightgreen', command=generate_pie_chart)
    pie_chart_button.grid(row=2, column=1, padx=10, pady=20)

# Function to add expense
def add_expense(name, amount):
    try:
        amount = float(amount)
        expenses.append((name, amount))
        messagebox.showinfo("Success", "Expense added successfully!")
    except ValueError:
        messagebox.showerror("Error", "Invalid amount entered!")

# Function to generate pie chart
def generate_pie_chart():
    if not expenses:
        messagebox.showwarning("Warning", "No expenses to generate pie chart!")
        return
    
    names = [expense[0] for expense in expenses]
    amounts = [expense[1] for expense in expenses]

    fig = plt.figure(figsize=(6, 6))
    plt.pie(amounts, labels=names, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Expense Distribution')

    pie_chart_window = tk.Toplevel(root)
    pie_chart_window.title("Pie Chart")
    pie_chart_window.geometry('400x400')

    canvas = FigureCanvasTkAgg(fig, master=pie_chart_window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Create the main application window
root = tk.Tk()
root.geometry('300x400')
root.title("Expense Tracker")

# Set background color for the main application window
root.configure(bg="purple")

# Create a frame for the button and text
button_frame = tk.Frame(root)

# Set background color for the button frame
button_frame.configure(bg="purple")

button_frame.pack(expand=True, fill='both')

# Create a label for the text and center it horizontally
text_label = tk.Label(button_frame, text='Expense Tracker', font=('Bold', 25), fg='black')

# Set background color for the label
text_label.configure(bg="purple")

text_label.pack(side='top', pady=(20, 0))

# Create a start button and connect it to open_next_window function
start_button = tk.Button(button_frame, text='Start', font=('Bold', 20), bg='lightblue', command=open_next_window)
start_button.pack(side='bottom', pady=50)

expenses = []  # List to store expenses

root.mainloop()
