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
from controller.cleanNanData import CleanNanData
from model.data import Data
from tabulate import tabulate


class CleanData:
    def __init__(self, dataset, window):
        self.dataset = Data(dataset)
        self.df = dataset
        self.root = tk.Toplevel(window)
        self.root.title("Clean Data")
        self.root.maxsize(width=1400, height=800)
        window.withdraw()
        self.root.protocol("WM_DELETE_WINDOW", lambda: self.quit(window))
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

        # show table data in window
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

    def quit(self, window):
        self.root.destroy()
        window.deiconify()
