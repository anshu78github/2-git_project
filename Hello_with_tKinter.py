import tkinter as tk
from tkinter import filedialog, font, colorchooser
from tkinter.messagebox import showinfo


# Create the main application window
root = tk.Tk()
root.title("Basic Tkinter App")
root.geometry("300x200")  # Set the size of the window

# Define the function that will be called when the button is clicked
def on_button_click():
    label.config(text="OOO...Hiii, YOU did it!!")

# Create a label
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=20)

# Create a button
button = tk.Button(root, text="Are you going to press me?", command=on_button_click, font=("Arial", 12))
button.pack(pady=10)

# Run the application
root.mainloop()
