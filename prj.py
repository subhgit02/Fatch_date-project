# Import Required Library
from tkinter import *
from tkcalendar import *

# Create Object
root = Tk()
#create title
root.title('Print Date App')
#create fevicon
root.iconbitmap('fev.png')
# Set geometry
root.geometry("400x400")
# Create label
l = Label(root, text = "Subh Calender")
l.config(font = ("Comic Sans MS", 20, "bold"))
l.pack()
root.configure(background='#0096DC')

# Add Calendar
cal = Calendar(root, selectmode = 'day', year = 2023, month = 8, day = 1)

cal.pack(pady = 20)

def grad_date(): date.config(text = "Your selected Date is: " + cal.get_date())

# Add Button and Label
Button(root, text = "Fatch date", command = grad_date).pack(pady = 20)

date = Label(root, text = "")
date.pack(pady = 20)

# Execute Tkinter
root.mainloop()
