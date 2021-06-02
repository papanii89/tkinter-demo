# Importing tkinter for our interface design
import tkinter as tk # Using the alias tk instead of the normal tkinter
from tkinter import ttk

# Create an instance of tk
window = tk.Tk()

# Giving window a title
window.title( "Our Demo App" )

# Restricting window resizing
window.resizable(True, True) # x,y

# Introducing our first label
# ttk.Label( window, text = "Guess My Name").grid(column = 0, row = 0)
lblName = ttk.Label( window, text = "Guess My name")
lblName.grid(column = 0, row = 0)

# Starting our button up for an event
def reveal_me():
    action.configure( text = "Mystery Solved" ) # Text that replaces "Guess My Name"
    lblName.configure( foreground = "blue" ) # Colour of the text
    lblName.configure( text = "Benjamin Benson" ) # Name  revealed

# Adding our button
action = ttk.Button( window, text = "Open Sesame!", command = reveal_me ) # activating the button
action.grid( column = 1, row = 0)

# Starting the GUI
window.mainloop()
