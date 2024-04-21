import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msg
import tkinter.filedialog as fd
import tkinter.simpledialog as sd
import tkinter.colorchooser as cc
import pandas as pd
from tkinter import filedialog
from model.dataset import Dataset
from model.typeAI import typeAI
from controller import readFile
from controller.cleanNanData import CleanNanData
from model.data import Data
from tabulate import tabulate


class CleanData:
    def __init__(self, dataset, window, file_name):
        self.file_name = file_name
        self.dataset = Data(dataset)
        self.df = dataset
        self.root = tk.Toplevel(window)
        self.root.title("Clean Data")
        self.root.maxsize(width=1400, height=800)
        window.withdraw()
        self.root.protocol("WM_DELETE_WINDOW", lambda: self.quit(window))

        self.frame_data = tk.Frame(self.root)
        self.frame_data.pack(side=tk.TOP, padx=10, pady=10)

        self.table = ttk.Treeview(
            self.frame_data, show="headings", columns=[])

        self.hscrollbar = ttk.Scrollbar(
            self.frame_data, orient="horizontal", command=self.table.xview
        )
        self.table.configure(xscrollcommand=self.hscrollbar.set)
        self.hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        self.vscrollbar = ttk.Scrollbar(
            self.frame_data, orient="vertical", command=self.table.yview
        )
        self.table.configure(yscrollcommand=self.vscrollbar.set)
        self.vscrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.table.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.show_data()

        self.frame_data_info = tk.Frame(self.root)
        self.frame_data_info.pack(side=tk.TOP, padx=10, pady=10)

        self.text_data_info = tk.Text(
            self.frame_data_info, width=100, height=20)
        self.text_data_info.pack(side=tk.LEFT, padx=10, pady=5)

        self.frame_button = tk.Frame(self.frame_data_info)
        self.frame_button.pack(side=tk.RIGHT, padx=10, pady=5)

        self.button_info = tk.Button(
            self.frame_button, text="Info", command=self.show_data_info)
        self.button_info.grid(row=0, column=0, padx=5, pady=5)

        self.button_check_nan = tk.Button(
            self.frame_button, text="Check NaN", command=self.check_nan)
        self.button_check_nan.grid(row=1, column=0, padx=5, pady=5)

        self.button_check_duplicate = tk.Button(
            self.frame_button, text="Check Duplicate", command=self.check_duplicate)
        self.button_check_duplicate.grid(row=2, column=0, padx=5, pady=5)

        self.button_delete_duplicate = tk.Button(
            self.frame_button, text="Delete Duplicate", command=self.delete_duplicate)
        self.button_delete_duplicate.grid(row=2, column=1, padx=5, pady=5)
        self.button_delete_duplicate.config(state=tk.DISABLED)

        self.button_save = tk.Button(
            self.frame_button, text="Save", command=self.save)
        self.button_save.grid(row=3, column=1, padx=5, pady=5)

        self.button_ok = tk.Button(
            self.frame_button, text="OK", command=lambda: self.quit(window))
        self.button_ok.grid(row=3, column=0, padx=5, pady=5)

        # show table data in window
        self.show_data_info()

    def show_data(self):

        self.table['columns'] = self.dataset.get_list_column()

        for item in self.table.get_children():
            self.table.delete(item)

        for col in self.dataset.get_list_column():
            self.table.heading(col, text=col)
            self.table.column(col, width=150, stretch=tk.NO)

        for row in self.dataset.df.itertuples():
            self.table.insert("", tk.END, values=list(row[1:]))

    def show_data_info(self):
        data_info = tabulate(self.dataset.get_info(),
                             headers='keys', tablefmt='fancy_grid')
        data_memory = self.dataset.get_memory_usage()

        self.text_data_info.configure(state=tk.NORMAL)
        self.text_data_info.delete("1.0", tk.END)
        self.text_data_info.insert(tk.END, data_info)
        self.text_data_info.insert(tk.END, "\n\n")
        self.text_data_info.insert(tk.END, data_memory)
        self.text_data_info.configure(state=tk.DISABLED)

    def check_nan(self):
        clean_nan = CleanNanData(self.dataset.df, self.root)
        self.root.wait_window(clean_nan.root)

        if clean_nan.df is not None:
            self.dataset.df = clean_nan.df
            self.show_data_info()
            self.show_data()

    def check_duplicate(self):
        dup = self.dataset.df.duplicated()
        # check if have duplicate value
        if dup.any():
            self.button_delete_duplicate.config(state=tk.NORMAL)
        self.text_data_info.configure(state=tk.NORMAL)
        self.text_data_info.delete("1.0", tk.END)
        self.text_data_info.insert(tk.END, dup)
        self.text_data_info.configure(state=tk.DISABLED)

    def delete_duplicate(self):
        self.dataset.df = self.dataset.df.drop_duplicates()
        self.button_delete_duplicate.config(state=tk.DISABLED)
        self.show_data_info()
        self.show_data()

    def save(self):
        # delete ".csv" in file name and add "_clean"
        name = self.file_name.replace(".csv", "") + "_clean.csv"
        # choses location to save
        file_path = filedialog.asksaveasfilename(
            initialfile=name,
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx"),
                       ("Text files", "*.txt"), ("All files", "*.*")],
            title="Save File",
        )

        if file_path:
            try:
                self.dataset.df.to_csv(file_path, index=False)
                msg.showinfo("Success", "File saved successfully!")
            except Exception as e:
                msg.showerror("Success", "Error:" +
                              str(e) + " Is successfully!")

    def quit(self, window):
        self.df = self.dataset.df
        self.root.destroy()
        window.deiconify()
