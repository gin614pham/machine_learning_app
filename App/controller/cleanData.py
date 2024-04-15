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
from model.data import Data
from tabulate import tabulate


class CleanData:
    def __init__(self, dataset, window):
        self.dataset = Data(dataset)
        self.df = dataset
        self.root = tk.Toplevel(window)
        self.root.title("Clean Data")
        self.root.maxsize(width=1200, height=600)
        window.withdraw()
        self.root.protocol("WM_DELETE_WINDOW", lambda: self.quit(window))
        # show table data in window
        self.show_data()
        self.show_data_info()

    def show_data(self):
        frame_data = tk.Frame(self.root)
        frame_data.pack(side=tk.TOP, padx=10, pady=10)

        table = ttk.Treeview(frame_data, show="headings",
                             columns=self.dataset.get_list_column())

        for col in self.dataset.get_list_column():
            table.heading(col, text=col)
            table.column(col, width=150, stretch=tk.NO)

        for row in self.dataset.df.itertuples():
            table.insert("", tk.END, values=list(row[1:]))

        hscrollbar = ttk.Scrollbar(
            frame_data, orient="horizontal", command=table.xview
        )
        table.configure(xscrollcommand=hscrollbar.set)
        hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        vscrollbar = ttk.Scrollbar(
            frame_data, orient="vertical", command=table.yview
        )
        table.configure(yscrollcommand=vscrollbar.set)
        vscrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        table.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def show_data_info(self):
        data_info = tabulate(self.dataset.get_info(),
                             headers='keys', tablefmt='github')
        data_memory = self.dataset.get_memory_usage()

        self.frame_data_info = tk.Frame(self.root)
        self.frame_data_info.pack(side=tk.TOP, padx=10, pady=10)
        self.label_data_info = tk.Label(
            self.frame_data_info, text="Data Info: ")
        self.label_data_info.pack(side=tk.TOP, padx=10, pady=5)

        self.text_data_info = tk.Text(
            self.frame_data_info, width=100, height=20)
        self.text_data_info.pack(side=tk.TOP, padx=10, pady=5)
        self.text_data_info.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.text_data_info.configure(state=tk.NORMAL)
        self.text_data_info.insert(tk.INSERT, data_info)
        self.text_data_info.insert(tk.INSERT, "\n\n")
        self.text_data_info.insert(tk.END, data_memory)
        self.text_data_info.configure(state=tk.DISABLED)

    def quit(self, window):
        self.root.destroy()
        window.deiconify()
