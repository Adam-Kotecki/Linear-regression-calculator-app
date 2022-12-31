import tkinter as tk
from tkinter import ttk
from tkinter import Entry
from tkinter.messagebox import showinfo

root = tk.Tk()

root.geometry('400x500')
root.resizable(False, False)
root.title('Linear regression calculator')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=8)
root.rowconfigure(4, weight=1)

label1 = tk.Label(root, text="Linear regression")
label1.grid(column=0, row = 0, columnspan = 4)

label1 = tk.Label(root, text="Please provide values:")
label1.grid(column=0, row = 1, columnspan = 2)

x_label = tk.Label(root, text="X")
x_label.grid(column=0, row = 2)
y_label = tk.Label(root, text="Y")
y_label.grid(column=1, row = 2)

root.mainloop()