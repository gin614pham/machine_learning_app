import pandas as pd


class Dataset:

    def __init__(self, df=None, target=None, vector_x=None):
        self.df = df
        self.target = target
        self.vector_x = vector_x

    def get_df(self):
        return self.df

    def get_target(self):
        return self.target

    def get_vector_x(self):
        return self.vector_x

    def read_csv(self, path):
        self.df = pd.read_csv(path)

    def get_list_column(self):
        return self.df.columns.tolist()
