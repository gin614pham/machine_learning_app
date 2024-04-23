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


class Chart:
    def __init__(self, dataset, window, file_name):
        self.file_name = file_name
        self.dataset = Data(dataset)
        self.df = dataset
        self.root = tk.Toplevel(window)
        self.root.title("Chart")
        window.withdraw()
        self.root.protocol("WM_DELETE_WINDOW", lambda: self.quit(window))

        self.available_columns = self.dataset.get_list_column()

        self.frame_chart = tk.Frame(self.root)
        self.frame_chart.pack(side=tk.TOP, padx=10, pady=10)
        self.label_x = tk.Label(
            self.frame_chart, text="X: ")
        self.label_x.grid(row=0, column=0, padx=5, pady=5)
        self.select_x = ttk.Combobox(
            self.frame_chart, state="readonly", values=self.available_columns)
        self.select_x.grid(row=0, column=1, padx=5, pady=5)
        self.select_x.bind("<<ComboboxSelected>>",
                           lambda event: self.update_y_options())

        self.label_y = tk.Label(
            self.frame_chart, text="Y: ")
        self.label_y.grid(row=1, column=0, padx=5, pady=5)
        self.select_y = ttk.Combobox(
            self.frame_chart, state="readonly", values=self.available_columns)
        self.select_y.grid(row=1, column=1, padx=5, pady=5)
        self.select_y.config(state="disable")

        self.label_type = tk.Label(
            self.frame_chart, text="Type: ")
        self.label_type.grid(row=2, column=0, padx=5, pady=5)
        self.select_type = ttk.Combobox(
            self.frame_chart, state="readonly", values=typeAI().get_name())
        self.select_type.grid(row=2, column=1, padx=5, pady=5)

        self.button_show = tk.Button(
            self.frame_chart, text="Show", command=self.show)
        self.button_show.grid(row=3, column=0, padx=5, pady=5)

        self.button_reset = tk.Button(
            self.frame_chart, text="Reset", command=self.reset)
        self.button_reset.grid(row=3, column=1, padx=5, pady=5)

    def quit(self, window):
        self.root.destroy()
        window.deiconify()

    def show(self):
        print(self.select_x.get(), self.select_y.get(), self.select_type.get())

    def reset(self):
        self.select_x.set("")
        self.select_y.set("")
        self.select_type.set("")
        self.select_y.config(state="disable")

    def update_y_options(self):
        selected_x = self.select_x.get()

        current_options_y = self.available_columns[:]
        if selected_x in current_options_y:
            # Remove selected X from Y options
            current_options_y.remove(selected_x)
        self.select_y.config(values=current_options_y)

        self.select_y.set("")
        self.select_y.config(state="readonly")
