"""
THIS IS A MINI-CALCULATOR APP THAT IS MEANT TO REGISTER MOUSE CLICKS AND KEYBOARD HITS
"""

# Importing the tkinter module
from tkinter import *

class OurWindow:
    def __init__(self, win):
        self.lblFnum = Label( win, text = "First Number" )
        self.lblFnum.place(x=50, y=50) # Setting the position for First Number Label
        self.lblSnum = Label( win, text = "Second Number ")
        self.lblSnum.place(x=50, y=100) # Setting the position for Second Number Label
        self.lblResult = Label( win, text = "Result" )
        self.lblResult.place(x=50, y=200) # Setting the position for First Number Label

        # Setting up our Textboxes (Entry fields)
        self.txtFnum = Entry()
        self.txtFnum.place(x=200, y=50) # Setting the position for the First Number Entry field
        self.txtSnum = Entry()
        self.txtSnum.place(x=200, y=100) # Setting the position for the Second Number Entry field
        self.txtResult = Entry( bd=3 ) # Giving the result textbox a border of width 3
        self.txtResult.place(x=200, y=200) # Setting the position for the Result Entry field

        # Setting up our Buttons
        self.btnAdd = Button( win, text = "Add", command = self.add )
        self.btnAdd.place(x=50, y=150) # Setting the position for the Add button
        self.btnSubtract = Button( win, text = "Subtract", command = self.sub )
        self.btnSubtract.bind( "<Button-2>", self.sub )
        self.btnSubtract.place(x=110, y=150) # Setting the position for the Subtract button
        self.btnMultiply = Button( win, text = "Multiply", command = self.multiple )
        self.btnMultiply.place(x=200, y=150) # Setting the position for the Add button
        self.btnDivide = Button( win, text = "Divide", command = self.divide )
        self.btnDivide.place(x=280, y=150) # Setting the position for the Add button
    
    # Defining our addition event
    def add(self):
        self.txtResult.delete( 0, 'end' )
        firstNumber = int( self.txtFnum.get() ) # grabbing the input from the first number entry field
        secondNumber = int( self.txtSnum.get() ) # grabbing the input from the first number entry field

        result = firstNumber + secondNumber # Performing the addition

        self.txtResult.insert( END, str( result ) )

    # Defining our subtraction event
    def sub(self):
        self.txtResult.delete( 0, 'end' )
        firstNumber = int( self.txtFnum.get() ) # grabbing the input from the first number entry field
        secondNumber = int( self.txtSnum.get() ) # grabbing the input from the first number entry field

        result = firstNumber - secondNumber # Performing the subtraction

        self.txtResult.insert( END, str( result ) )
    
    # Defining our multiplication event
    def multiple(self):
        self.txtResult.delete( 0, 'end' )
        firstNumber = int( self.txtFnum.get() ) # grabbing the input from the first number entry field
        secondNumber = int( self.txtSnum.get() ) # grabbing the input from the first number entry field

        result = firstNumber * secondNumber # Performing the multiplication

        self.txtResult.insert( END, str( result ) )
    
    # Defining our division event
    def divide(self):
        self.txtResult.delete( 0, 'end' )
        firstNumber = int( self.txtFnum.get() ) # grabbing the input from the first number entry field
        secondNumber = int( self.txtSnum.get() ) # grabbing the input from the first number entry field

        result = firstNumber / secondNumber # Performing the division

        self.txtResult.insert( END, str( result ) )

# Setting up the window
container = Tk()
myContainer = OurWindow( container )
container.title( "Mini-Calculator" )
container.geometry("400x300+10+10")
container.mainloop()