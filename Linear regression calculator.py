import tkinter as tk
from tkinter import ttk
from tkinter import Entry
from tkinter.messagebox import showinfo
from tkinter import filedialog
import numpy as np
import openpyxl
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

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
    globals()[f"x{i + 1}"] = ttk.Entry(frame)
    globals()[f"x{i + 1}"].grid(row = r, column = 0)
    globals()[f"y{i + 1}"] = ttk.Entry(frame)
    globals()[f"y{i + 1}"].grid(row = r, column = 1)
    r += 1

frame.grid(column = 0, row = 3, columnspan = 2, sticky = "N")

more = tk.Button(root, text="I have more values", command=lambda: more())
more.grid(column=0, row = 4, columnspan = 2, sticky = "N")

calculate = tk.Button(root, text="Calculate", command=lambda: get_data_from_widgets())
calculate.grid(column=0, row = 5, columnspan = 2)

learn = tk.Button(root, text="Learn about linear regression", command=lambda: learn())
learn.grid(column=0, row = 6, columnspan = 2)


def get_data_from_widgets():
    x_list = []
    y_list = []
    for i in range(10):
        if (globals()[f"x{i + 1}"].get() != "") and (globals()[f"y{i + 1}"].get() != ""):
            x_list.append(globals()[f"x{i + 1}"].get())
            y_list.append(globals()[f"y{i + 1}"].get())
    
    x_list = np.array(x_list).reshape((-1, 1))
    y_list = np.array(y_list)
    calculate(x_list, y_list)


def more():
    root2 = tk.Tk()
    root2.geometry('300x200')
    root2.resizable(False, False)
    root2.title('Get data from Excel')
    root2.rowconfigure(0, weight=2)
    root2.rowconfigure(1, weight=1)
    info = tk.Label(root2, text="Please select file with format xlsx or xlsm. X values should be in the first column, and Y values in the second column. Do not use column headers. All data should be numeric", wraplength = 300, justify = tk.CENTER)
    info.grid(column=0, row = 0)
    select_file = tk.Button(root2, text="Select Excel file", command=lambda: [get_data_from_xlsx(), root2.destroy()])
    select_file.grid(column=0, row = 1)
    root2.mainloop()


def get_data_from_xlsx():
    path = filedialog.askopenfilename()
    try:
        workbook = openpyxl.load_workbook(path)
    except:
       tk.messagebox.showinfo(message="File with wrong format selected. Please select xlsx or xlsm.")
       return
    
    x_list = []
    y_list = []
    sheet = workbook.active
    
    try:
        r = 1
        for cell in sheet['A']:
            if (cell.value != None) and sheet.cell(row=r, column=2).value != None:
                x_list.append(cell.value)
                y_list.append(sheet.cell(row=r, column=2).value)
                r += 1
            else:
                break
    except:
        tk.messagebox.showinfo(message="Something went wrong")
        return
    
    x_list = np.array(x_list).reshape((-1, 1))
    y_list = np.array(y_list)
    calculate(x_list, y_list)
    
    
def calculate(x, y):
    model = LinearRegression()
    model.fit(x, y)
    r_sq = model.score(x, y)
    b0 = model.intercept_
    b1 = model.coef_
    y_pred = b0 + b1 * x
    
    for widgets in root.winfo_children():
      widgets.destroy()
      
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=6)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)
    root.rowconfigure(5, weight=1)
    root.rowconfigure(6, weight=1)
    
    label_title = tk.Label(root, text="Calculated results:")
    label_title.grid(row = 0)
    
    fig = Figure(figsize = (4, 4))
    a = fig.add_subplot(111)
    a.scatter(x, y) 
    canvas = FigureCanvasTkAgg(fig, master = root)  
    canvas.get_tk_widget().grid(row = 1)
    canvas.draw()
    
    label_R2 = tk.Label(root, text="Coefficient of determination: " + str(r_sq))
    label_R2.grid(row = 2)
    
    label_b0 = tk.Label(root, text="Intercept: " + str(b0))
    label_b0.grid(row = 3)
    
    label_b1 = tk.Label(root, text="Intercept: " + str(b1))
    label_b1.grid(row = 4)
    
    back = tk.Button(root, text="Go back", command=lambda: back())
    back.grid(row = 6)
    
    def back():
        pass
    
    print("r_sq: " + str(r_sq))
    print("b0: " + str(b0))
    print("b1: " + str(b1))
    print("y_pred: " + str(y_pred))

def learn():
    pass

root.mainloop()