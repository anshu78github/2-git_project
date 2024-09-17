import tkinter as tk
from tkinter import filedialog, font, colorchooser
from tkinter.messagebox import showinfo

class TextEditor:

    # def __init__(self, root):
    #     self.root = root
    #     self.root.title("Text Editor - Notebook style")
    #     self.root.geometry("800x600")

    # # now creating text widget
    #     self.text_area=tk.Text(root, wrap='word', font=("Arial" , 14))
    #     self.text_area.pack(fill=tk.BOTH, expand=1)

    # #adding scroll bar to text_area
    #     scrollbar= tk.Scrollbar(self.text_area)
    #     self.text_area.config(yscrollcommand=scrollbar.set)
    #     scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
    #     scrollbar.config(command=self.text_area.yview)
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor - Notebook Style")
        self.root.geometry("800x600")

        # Create the text widget
        self.text_area = tk.Text(root, wrap='word', undo=True, font=("Arial", 14))
        self.text_area.pack(fill=tk.BOTH, expand=1)

        # Scrollbar for the text area
        scrollbar = tk.Scrollbar(self.text_area)
        self.text_area.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar.config(command=self.text_area.yview)

        # Create menu bar
        self.create_menu_bar()

        # Add toolbar for font controls
        self.create_toolbar()

        # Track current file name
        self.current_file = None

    def create_menu_bar(self):
        """Create the menu bar with file handling options."""
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)

        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open...", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As...", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

    def create_toolbar(self):
        """Create toolbar for font size, font weight, color, and other text settings."""
        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        # Font family selector
        font_families = list(font.families())
        self.font_var = tk.StringVar(value="Arial")
        font_menu = tk.OptionMenu(toolbar, self.font_var, *font_families, command=self.change_font_family)
        font_menu.pack(side=tk.LEFT, padx=5)

        # Font size selector
        self.size_var = tk.IntVar(value=14)
        size_menu = tk.OptionMenu(toolbar, self.size_var, *range(8, 73), command=self.change_font_size)
        size_menu.pack(side=tk.LEFT, padx=5)

        # Bold button
        bold_button = tk.Button(toolbar, text="Bold", command=self.toggle_bold)
        bold_button.pack(side=tk.LEFT, padx=5)

        # Underline button
        underline_button = tk.Button(toolbar, text="Underline", command=self.toggle_underline)
        underline_button.pack(side=tk.LEFT, padx=5)

        # Text color button
        color_button = tk.Button(toolbar, text="Text Color", command=self.change_text_color)
        color_button.pack(side=tk.LEFT, padx=5)

    def new_file(self):
        """Create a new file by clearing the text area."""
        self.text_area.delete(1.0, tk.END)
        self.current_file = None
        self.root.title("Text Editor - Notebook Style")

    def open_file(self):
        """Open a file and display its contents in the text editor."""
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.INSERT, content)
            self.current_file = file_path
            self.root.title(f"Text Editor - {file_path}")

    def save_file(self):
        """Save the current file. If no file exists, open save dialog."""
        if self.current_file:
            content = self.text_area.get(1.0, tk.END)
            with open(self.current_file, 'w') as file:
                file.write(content)
        else:
            self.save_as()

    def save_as(self):
        """Save the file as a new file."""
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"),("All files", "*.*")])
        if file_path:
            content = self.text_area.get(1.0, tk.END)
            with open(file_path, 'w') as file:
                file.write(content)
            self.current_file = file_path
            self.root.title(f"Text Editor - {file_path}")

    def change_font_family(self, event=None):
        """Change the font family of the selected text."""
        current_font = font.Font(font=self.text_area['font'])
        current_font.config(family=self.font_var.get())
        self.text_area.config(font=current_font)

    def change_font_size(self, event=None):
        """Change the font size of the selected text."""
        current_font = font.Font(font=self.text_area['font'])
        current_font.config(size=self.size_var.get())
        self.text_area.config(font=current_font)

    def toggle_bold(self):
        """Toggle bold text."""
        current_font = font.Font(font=self.text_area['font'])
        if current_font.actual()['weight'] == 'bold':
            current_font.config(weight='normal')
        else:
            current_font.config(weight='bold')
        self.text_area.config(font=current_font)

    def toggle_underline(self):
        """Toggle underline text."""
        current_font = font.Font(font=self.text_area['font'])
        current_font.config(underline=not current_font.actual()['underline'])
        self.text_area.config(font=current_font)

    def change_text_color(self):
        """Change the text color."""
        color = colorchooser.askcolor()[1]
        if color:
            self.text_area.config(fg=color)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
