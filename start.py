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

#Starting up our textield event
def click_me():
    text_action.configure( text = "Hello " + name.get() ) # Displaying the user's name

# Setting our text label
lblText = ttk.Label( window, text = "Please enter a name", padding = 3)
lblText.grid( column = 0, row = 2)

# Assing the textbox widget
name = tk.StringVar()
user_name = ttk.Entry( window, width = 14, textvariable = name)
user_name.grid( column = 0, row = 3)

# Adding our button
action = ttk.Button( window, text = "Open Sesame!", command = reveal_me ) # activating the button
action.grid( column = 1, row = 0)

text_action = ttk.Button( window, text = "Click to Greet", command = click_me )
text_action.grid( column = 1, row = 3)

# Starting the GUI
window.mainloop()
