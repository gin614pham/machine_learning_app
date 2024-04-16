# import tkinter libraries
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msg
import tkinter.filedialog as fd
import tkinter.simpledialog as sd
import tkinter.colorchooser as cc
import pandas as pd
from model.dataset import Dataset
from model.typeAI import typeAI
from controller import readFile
from controller.cleanData import CleanData
import train


class Main:
    def __init__(self):

        self.dataset = Dataset()
        self.root = tk.Tk()
        self.type_ai = typeAI().get_name()
        self.root.title("App")

        self.frame_input_file = tk.Frame(self.root)
        self.frame_input_file.pack(side=tk.TOP, padx=10, pady=20)
        self.button_input_file = tk.Button(
            self.frame_input_file, text="Choose File CSV", command=self.browse_file)
        self.button_input_file.pack(side=tk.TOP, padx=10, pady=10)
        self.label_file_input = tk.Label(
            self.frame_input_file, text="File Name: No file selected")
        self.label_file_input.pack(side=tk.TOP, padx=10, pady=5)
        self.button_clean_data = tk.Button(
            self.frame_input_file, text="Clean Data", command=self.clean_data)
        self.button_clean_data.pack(side=tk.TOP, padx=10, pady=5)
        self.button_clean_data.configure(state=tk.DISABLED)

        self.label_select = tk.Label(
            self.root, text="Select Column: ")
        self.label_select.pack(side=tk.TOP, padx=10, pady=5)
        self.select_target = ttk.Combobox(
            self.root, state="readonly", values=None)
        self.select_target.pack(side=tk.TOP, padx=10, pady=5)
        self.select_target.bind("<<ComboboxSelected>>",
                                lambda event: self.load_data())

        self.frame_select_x = tk.Frame(self.root)
        self.frame_select_x.pack(side=tk.TOP, padx=10, pady=5)
        self.frame_select_x_left = tk.Frame(self.frame_select_x)
        self.frame_select_x_left.pack(side=tk.LEFT, padx=10, pady=5)
        self.frame_select_x_right = tk.Frame(self.frame_select_x)
        self.frame_select_x_right.pack(side=tk.RIGHT, padx=10, pady=5)

        self.label_select_x_left = tk.Label(
            self.frame_select_x_left, text="Select Column: ")
        self.label_select_x_left.pack(side=tk.TOP, padx=10, pady=5)
        self.list_column_select_x = tk.Listbox(
            self.frame_select_x_left, selectmode=tk.EXTENDED)
        self.list_column_select_x.pack(side=tk.TOP, padx=10, pady=5)

        self.label_select_x_right = tk.Label(
            self.frame_select_x_right, text="Select Column: ")
        self.label_select_x_right.pack(side=tk.TOP, padx=10, pady=5)
        self.list_column_x = tk.Listbox(
            self.frame_select_x_right, selectmode=tk.EXTENDED)
        self.list_column_x.pack(side=tk.TOP, padx=10, pady=5)

        self.frame_button = tk.Frame(self.frame_select_x)
        self.frame_button.pack(side=tk.LEFT, padx=10, pady=5)
        self.button_add = tk.Button(
            self.frame_button, text="Add >>", command=self.join_left)
        self.button_add.pack(side=tk.TOP, padx=5, pady=5)
        self.button_remove = tk.Button(
            self.frame_button, text="<< Remove", command=self.join_right)
        self.button_remove.pack(side=tk.TOP, padx=5, pady=5)

        self.select_AI = ttk.Combobox(
            self.root, state="readonly", values=self.type_ai)
        self.select_AI.pack(side=tk.TOP, padx=10, pady=5)
        self.select_AI.current(0)

        self.button_start = tk.Button(
            self.root, text="Start", command=self.start)
        self.button_start.pack(side=tk.TOP, padx=10, pady=5)

    def run(self):
        self.root.mainloop()

    def quit(self):
        self.root.destroy()

    def browse_file(self):
        try:
            self.dataset.df, self.file_name = readFile.browse_csv_file()
            if self.dataset.df is not None:
                self.label_file_input.config(
                    text="File Name: " + self.file_name)
                self.select_target.config(
                    values=self.dataset.get_list_column())
                self.select_target.current(0)
                self.button_clean_data.configure(state=tk.NORMAL)
                self.load_data()
        except Exception as e:
            msg.showerror("Error", str(e))

    def load_data(self):
        columns = self.dataset.get_list_column()
        self.list_column_select_x.delete(0, tk.END)
        self.list_column_x.delete(0, tk.END)
        for column in columns:
            if column != self.select_target.get():
                self.list_column_select_x.insert(tk.END, column)

    def join_left(self):
        for i in self.list_column_select_x.curselection()[::-1]:
            self.list_column_x.insert(tk.END, self.list_column_select_x.get(i))
            self.list_column_select_x.delete(i)

    def join_right(self):
        for i in self.list_column_x.curselection()[::-1]:
            self.list_column_select_x.insert(tk.END, self.list_column_x.get(i))
            self.list_column_x.delete(i)

    def clean_data(self):
        clean_data = CleanData(self.dataset.df, self.root)
        self.root.wait_window(clean_data.root)

        if clean_data.dataset is not None:
            self.dataset.df = clean_data.df
            self.load_data()

    def start(self):
        print(self.select_target.get())
        print(self.list_column_x.get(0, tk.END))
        print(self.select_AI.get())
        print(self.dataset.df)
        train.train(self.dataset.df, self.select_target.get(),
                    list(self.list_column_x.get(0, tk.END)), self.select_AI.get())
    


if __name__ == "__main__":
    main = Main()
    main.run()
