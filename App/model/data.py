import pandas as pd


class Data:
    def __init__(self, df=None, name=""):
        self.name = name
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
                memory_usage_dict['Memory usage'] = "{:3.1f}+ {}".format(
                    memory_usage, unit)
                break
            else:
                memory_usage /= 1024.0
        return pd.Series(memory_usage_dict)

    def get_all_info_nan(self):
        info_nan = {
            "Sum NaN": [],
            "Percent NaN": [],
            "Dtype": []
        }
        sum_nan = self.df.isna().sum()
        percent_nan = (self.df.isna().mean()*100).round(2).astype(str) + "%"

        info_nan["Sum NaN"] = sum_nan
        info_nan["Percent NaN"] = percent_nan
        info_nan["Dtype"] = self.df.dtypes

        return pd.DataFrame(info_nan)
