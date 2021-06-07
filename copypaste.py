#importing tkinter for our interface design

import tkinter as tk #using the alias tk instead of the normal tkinter
from tkinter import ttk

win = tk.Tk()

#Giving the window a title
win.title('             App title')
ttk.Label(win).grid( column=3 , row = 0)

#creating an empty space
ttk.Label(win).grid( row=0)

#Setting our FNAME labels and input boxes
lblFNAME = ttk.Label (win, text = "FNAME:")
lblFNAME.grid(column=1 , row= 1)

#creating an empty space
ttk.Label(win).grid (row=2)

#setting or FNAME textbox
FName=tk.StringVar()
txtFNAME = ttk.Entry(win, width= 16, textvariable=FName) 
txtFNAME.grid(column =3, row =1)

#setting our LNAME labels and input boxes
lblLNAME = ttk.Label(win,text = "LNAME: ")
lblLNAME.grid(column=1, row=3)

#creating an empty space
ttk.Label(win).grid (row=4)

#setting our LNAME textbox
Lname = tk.StringVar()
txtLNAME = ttk.Entry(win, width=16, textvariable= Lname)
txtLNAME.grid(column=3, row=3)

#setting our EMAIL labels and input boxes
lblEMAIL = ttk.Label(win,text = "EMAIL: ")
lblEMAIL.grid(column=1, row=5)

#creating an empty space
ttk.Label(win).grid (row=6)

#setting our EMAIL textbox
Email = tk.StringVar()
txtEMAIL = ttk.Entry(win, width=16, textvariable= Email)
txtEMAIL.grid(column=3, row=5)


#setting our PASSD labels and input boxes
lblPASSD = tk.Label(win, text ="PASSD:")
lblPASSD.grid(column=1, row=7)

#creating an empty space
ttk.Label(win).grid (row=8)

#setting our PASSD text box
Passd = tk.StringVar()
txtPASSD =ttk.Entry(win, width=16, textvariable=Passd)
txtPASSD.grid(column=3, row=7)

#Creating an empty space
tk.Label(win).grid(row=9)

#setting up our SUBMIT button
btnSUBMIT =ttk.Button(win, width= 10, text="SUBMIT")
btnSUBMIT.grid(column=1, row=10)

#setting up our RESET button
btnRESET =ttk.Button(win, width= 15, text="RESET")
btnRESET.grid(column=3, row=10)

#Invoking our GUI loop
win.mainloop()