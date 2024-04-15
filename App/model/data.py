import pandas as pd


class Data:
    def __init__(self, df=None):
        self.df = pd.DataFrame()
        self.df = df

    def get_df(self):
        return self.df

    def get_list_column(self):
        return self.df.columns.tolist()

    def get_info(self):
        info = {
            "Column": [],
            "Non-Null Count": [],
            "Dtype": []
        }

        for col in self.get_list_column():
            info["Column"].append(col)
            info["Non-Null Count"].append(self.df[col].count())
            info["Dtype"].append(self.df[col].dtype)

        return pd.DataFrame(info)

    def get_memory_usage(self):
        memory_usage = self.df.memory_usage(deep=True).sum()
        memory_usage_dict = {'Memory usage': memory_usage}
        for unit in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if memory_usage < 1024.0:
                memory_usage_dict['Memory usage'] = "{:3.1f} {}".format(
                    memory_usage, unit)
                break
            else:
                memory_usage /= 1024.0
        return pd.Series(memory_usage_dict)
