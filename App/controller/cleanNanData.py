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


class CleanNanData:
    def __init__(self, dataset, window):
        self.dataset = Data(dataset)
        self.df = dataset
        self.root = tk.Toplevel(window)
        self.root.title("Clean Data")
        self.root.maxsize(width=1200, height=600)
        window.withdraw()
        self.root.protocol("WM_DELETE_WINDOW", lambda: self.quit(window))

        self.frame_data_info = tk.Frame(self.root)
        self.frame_data_info.pack(side=tk.TOP, padx=10, pady=10)

        self.text_data_info = tk.Text(
            self.frame_data_info, width=100, height=20)
        self.text_data_info.pack(side=tk.LEFT, padx=10, pady=5)
        self.show_nan_info()

        self.frame_button = tk.Frame(self.frame_data_info)
        self.frame_button.pack(side=tk.RIGHT, padx=10, pady=5)
        self.button_delete_nan = tk.Button(
            self.frame_button, text="Delete NaN", command=self.delete_nan)
        self.button_delete_nan.grid(row=0, column=0, padx=5, pady=5)
        self.button_replace_nan = tk.Button(
            self.frame_button, text="Replace NaN", command=self.replace_nan)
        self.button_replace_nan.grid(row=1, column=0, padx=5, pady=5)

    def quit(self, window):
        self.root.destroy()
        window.deiconify()

    def show_nan_info(self):
        info_nan = tabulate(self.dataset.get_all_info_nan(),
                            headers='keys', tablefmt='fancy_grid')
        self.text_data_info.configure(state=tk.NORMAL)
        self.text_data_info.delete("1.0", tk.END)
        self.text_data_info.insert(tk.END, info_nan)
        self.text_data_info.configure(state=tk.DISABLED)

    def delete_nan(self):
        pass

    def replace_nan(self):
        pass
