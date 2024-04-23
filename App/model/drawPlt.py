import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
colors = ['blue', 'green', 'red', 'purple', 'orange', 'yellow', 'cyan', 'magenta', 'gray', 'brown', 'pink', 'teal']
def draw(df, a, b, Chart):
    if Chart == 'Pie Chart':
        return draw_circle(a, df)
    elif Chart == 'Bar Chart':
        return draw_bar(a, b, df)
    elif Chart == 'Histogram':
        return draw_hist(a , df)
def draw_circle(a, df):
    plt.pie(df[a].value_counts(), autopct='%1.1f%%', shadow=True, startangle=90)
    plt.show()
def draw_bar(a, b, df):
    plt.bar(df[a], df[b], color=colors)
    plt.xlabel(a)
    plt.ylabel(b)
    plt.show()
def draw_hist(a, df):
    df[a].hist()
    plt.show()
