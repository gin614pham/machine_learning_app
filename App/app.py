import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msg
import tkinter.filedialog as fd
import tkinter.simpledialog as sd
import tkinter.colorchooser as cc
import pandas as pd
# import file train.ipynb
from train import Logistic_Regression, Linear_Regression

# create fun browse_file csv


def browse_file():
    global df
    file_path = fd.askopenfilename(filetypes=(
        ("CSV Files", "*.csv"), ("All Files", "*.*")))
    if file_path:
        # check file extension csv
        if not file_path.lower().endswith('.csv'):
            msg.showerror("Error", "Please select a CSV file.")
            return

        # read csv file
        df = pd.read_csv(file_path)
        # save name csv
        file_name = file_path.split('/')[-1]
        label.configure(text="File Name: " + file_name)
        drop_down['values'] = df.columns.tolist()
        drop_down.current(0)
        load_data()


def load_data():
    global df
    columns = df.columns
    columns = columns.tolist()
    list_column.delete(0, tk.END)
    for column in columns:
        # check column is not selected in drop_down
        selected = drop_down.get()
        if column != selected:
            list_column.insert(tk.END, column)

    list_column_select.delete(0, tk.END)


def join_left():
    selected_items = list_column.curselection()
    for index in selected_items[::-1]:
        item = list_column.get(index)
        if item not in list_column_select.get(0, tk.END):
            list_column_select.insert(tk.END, item)
            list_column.delete(index)


def join_right():
    selected_items = list_column_select.curselection()
    for index in selected_items[::-1]:
        item = list_column_select.get(index)
        if item not in list_column.get(0, tk.END):
            list_column.insert(tk.END, item)
            list_column_select.delete(index)


def start():
    global df
    selected_columns = list_column_select.get(0, tk.END)
    selected_columns = list(selected_columns)
    selected = drop_down.get()
    ai_algorithm = drop_down_ai.get()
    if not selected_columns:
        msg.showerror("Error", "Please select columns for processing.")
    else:
        # switch algorithm
        if ai_algorithm == "Linear Regression":
            print(df.columns)
            Linear_Regression(df, selected, selected_columns)

        elif ai_algorithm == "Logistic Regression":
            Logistic_Regression(df, selected, selected_columns)
        # elif ai_algorithm == "Decision Tree":

        else:
            msg.showerror("Error", "Please select algorithm.")
            return


# call fun main
df = pd.DataFrame()
type_ai = ["Linear Regression", "Logistic Regression", "Decision Tree",]
root = tk.Tk()
root.title("App")
root.geometry("640x680")
root.resizable(False, False)
# create frame for input file csv
frame_input = tk.Frame(root)
frame_input.pack(side=tk.TOP, padx=10, pady=20)
# create button for browse file csv
browse_button = tk.Button(
    frame_input, text="Choose File CSV", command=browse_file)
browse_button.pack(side=tk.TOP, padx=10, pady=10)
# label for file name
label = tk.Label(frame_input, text="File Name: No file selected")
label.pack(side=tk.TOP, padx=10, pady=5)

label_select = tk.Label(root, text="Select Column: ")
label_select.pack(side=tk.TOP, padx=10, pady=5)
drop_down = ttk.Combobox(root, state="readonly")
drop_down.pack(side=tk.TOP, padx=10, pady=10)
drop_down.bind("<<ComboboxSelected>>", lambda event: load_data())
# Tạo Frame để chứa các thành phần
frame_select = tk.Frame(root)
frame_select.pack(side=tk.TOP, padx=10, pady=10)

# Listbox bên trái (chứa các mục chưa được chọn)
frame_left = tk.Frame(frame_select)
frame_left.pack(side=tk.LEFT, padx=10, pady=10)
label_left = tk.Label(frame_left, text="Current Column: ")
label_left.pack(side=tk.TOP, padx=10, pady=10)
list_column = tk.Listbox(frame_left, selectmode="multiple", height=10)
list_column.pack(side=tk.TOP, padx=10, pady=10)

frame_button = tk.Frame(frame_select)
frame_button.pack(side=tk.LEFT, padx=10, pady=10)
# Nút "Add" để di chuyển các mục từ Listbox bên trái sang Listbox bên phải
button_add = tk.Button(frame_button, text="Add >>", command=join_left)
button_add.pack(side=tk.TOP, padx=5, pady=5)

# Nút "Remove" để di chuyển các mục từ Listbox bên phải sang Listbox bên trái
button_remove = tk.Button(frame_button, text="<< Remove", command=join_right)
button_remove.pack(side=tk.TOP, padx=5, pady=5)

# Listbox bên phải (chứa các mục đã được chọn)
frame_right = tk.Frame(frame_select)
frame_right.pack(side=tk.LEFT, padx=10, pady=10)
label_right = tk.Label(frame_right, text="Column Select: ")
label_right.pack(side=tk.TOP, padx=10, pady=10)
list_column_select = tk.Listbox(frame_right, selectmode="multiple", height=10)
list_column_select.pack(side=tk.TOP, padx=10, pady=10)

drop_down_ai = ttk.Combobox(root, state="readonly")
drop_down_ai.pack(side=tk.TOP, padx=10, pady=10)
drop_down_ai['values'] = type_ai
drop_down_ai.current(0)

button_start = tk.Button(root, text="Start", command=start)
button_start.pack(side=tk.TOP, padx=10, pady=10)

root.mainloop()
