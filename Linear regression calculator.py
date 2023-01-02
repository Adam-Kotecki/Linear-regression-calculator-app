import tkinter as tk
from tkinter import ttk
from tkinter import Entry
from tkinter.messagebox import showinfo

root = tk.Tk()

root.geometry('400x500')
root.resizable(False, False)
root.title('Linear regression calculator')

# 4 columns:
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=4)

frame = ttk.Frame(root)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

label1 = tk.Label(root, text="Linear regression")
label1.grid(column=0, row = 0, columnspan = 4)

label1 = tk.Label(root, text="Please provide numeric values:")
label1.grid(column=0, row = 1, columnspan = 2)

x_label = tk.Label(root, text="X")
x_label.grid(column=0, row = 2)
y_label = tk.Label(root, text="Y")
y_label.grid(column=1, row = 2)

r = 0
for i in range(10):
    frame.rowconfigure(r, weight=1)
    ttk.Entry(frame).grid(row = r, column = 0)
    ttk.Entry(frame).grid(row = r, column = 1)
    r += 1

frame.grid(column = 0, row = 3, columnspan = 2, sticky = "N")

more = tk.Button(root, text="I have more values", command=lambda: more())
more.grid(column=0, row = 4, columnspan = 2, sticky = "N")

calculate = tk.Button(root, text="Calculate", command=lambda: calculate())
calculate.grid(column=0, row = 5, columnspan = 2)

learn = tk.Button(root, text="Learn about linear regression", command=lambda: learn())
learn.grid(column=0, row = 6, columnspan = 2)

def more():
    pass

def calculate():
    pass

def learn():
    pass

root.mainloop()