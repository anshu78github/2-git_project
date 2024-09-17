import tkinter as tk
from tkinter import filedialog, font, colorchooser
from tkinter.messagebox import showinfo


# class helloFromGUI:
#     def __init__(self,root):
#         self.root=root
#         self.root.geometry("400x400")
#         self.root.title("Greetings")

#         self.button=tk.Button(self.root,text="Greet",command="buttonpressed",font=("Arial", 14))
#         self.button.pack()

#     def buttonpressed():
#         sayHello=tk.Text(root,text="Hello from ANSHU, this is tkinter in python",font=("Arial", 14))
#         sayHello.pack(fill="both",expand=1)


# if __name__ == "main":
#     root=tk.Tk()
#     instance1=helloFromGUI(root)
#     root.mainloop()



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
