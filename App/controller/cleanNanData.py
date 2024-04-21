import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
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

    replace_type = ["Mean", "Median", "Mode"]

    def __init__(self, dataset, window):
        self.dataset = Data(dataset)
        self.df = dataset
        self.root = tk.Toplevel(window)
        self.root.title("Clean Data")
        # self.root.maxsize(width=1500, height=600)
        window.withdraw()
        self.root.protocol("WM_DELETE_WINDOW", lambda: self.quit(window))

        self.frame_data_info = tk.Frame(self.root)
        self.frame_data_info.pack(side=tk.TOP, padx=10, pady=10)

        self.text_data_info = tk.Text(
            self.frame_data_info, width=100, height=20)
        self.text_data_info.pack(side=tk.LEFT, padx=10, pady=5)

        self.frame_button = tk.Frame(self.frame_data_info)
        self.frame_button.pack(side=tk.RIGHT, padx=10, pady=5)

        self.frame_edit_column = tk.Frame(self.frame_button)
        self.frame_edit_column.pack(side=tk.TOP, padx=10, pady=5)

        self.label_edit_column = tk.Label(
            self.frame_edit_column, text="Edit Column: ")
        self.label_edit_column.grid(row=0, column=0, padx=5, pady=5)
        self.combobox_target = ttk.Combobox(
            self.frame_edit_column, state="readonly", values=self.dataset.get_list_column())
        self.combobox_target.grid(row=0, column=1, padx=5, pady=5)

        self.button_delete_row = tk.Button(
            self.frame_edit_column, text="Delete Row", command=self.delete_nan_row)
        self.button_delete_row.grid(row=1, column=0, padx=5, pady=5)

        self.button_delete_column = tk.Button(
            self.frame_edit_column, text="Delete Column", command=self.delete_nan_column)
        self.button_delete_column.grid(row=1, column=1, padx=5, pady=5)

        self.button_replace_row = tk.Button(
            self.frame_edit_column, text="Replace with: ", command=self.replace_nan)
        self.button_replace_row.grid(row=2, column=0, padx=5, pady=5)

        self.combobox_replace_row = ttk.Combobox(
            self.frame_edit_column, state="readonly", values=self.replace_type)
        self.combobox_replace_row.grid(row=2, column=1, padx=5, pady=5)

        self.show_nan_info()

        # show table data in window

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

        self.combobox_target.configure(values=self.dataset.get_list_column())
        self.combobox_target.current(0)

    def delete_nan_row(self):
        tagert = self.combobox_target.get()
        self.df.dropna(subset=[tagert], inplace=True)
        self.show_nan_info()

    def delete_nan_column(self):
        tagert = self.combobox_target.get()
        self.df.drop(columns=[tagert], inplace=True)
        self.show_nan_info()

    def replace_nan(self):
        tagert = self.combobox_target.get()
        replace = self.combobox_replace_row.get()
        if replace == "Mean":
            self.df[tagert] = self.df[tagert].fillna(self.df[tagert].mean())
        elif replace == "Median":
            self.df[tagert] = self.df[tagert].fillna(self.df[tagert].median())
        elif replace == "Mode":
            self.df[tagert] = self.df[tagert].fillna(self.df[tagert].mode()[0])
        self.show_nan_info()
