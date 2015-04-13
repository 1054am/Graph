__author__ = 'brothertonjd'

import tkFileDialog

from Tkinter import *

def callback():

    file_path = tkFileDialog.askopenfilename()

root = Tk()

# create a menu
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=callback)
filemenu.add_command(label="Open...", command=callback)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=callback)

mainloop()

