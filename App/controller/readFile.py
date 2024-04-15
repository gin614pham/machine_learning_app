import pandas as pd
import tkinter.filedialog as fd
import tkinter.messagebox as msg


def browse_csv_file():
    file_path = fd.askopenfilename(filetypes=(
        ("CSV Files", "*.csv"), ("All Files", "*.*")))
    if file_path:
        if not file_path.lower().endswith('.csv'):
            msg.showerror("Error", "Please select a CSV file.")
            return None
        df = pd.read_csv(file_path)
        file_name = file_path.split('/')[-1]
        return df, file_name
    return None
