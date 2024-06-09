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
    elif Chart == 'Line Chart':
        return draw_line(a, b, df)
    elif Chart == 'Box Plot':
        return draw_box(a, df)
    elif Chart == 'Scatter Plot':
        return draw_scatter(a, b, df)
    elif Chart == 'Heatmap':
        return draw_heatmap(df)
    elif Chart == 'Violin Plot':
        return draw_violin(a, b, df)
    elif Chart == 'Pair Plot':
        return draw_pairplot(df)
    elif Chart == 'Joint Plot':
        return draw_jointplot(a, b, df)
    elif Chart == 'Swarm Plot':
        return draw_swarmplot(a, b, df)
    elif Chart == 'Boxen Plot':
        return draw_boxenplot(a, b, df)
    elif Chart == 'Rug Plot':
        return draw_rugplot(a, df)

def draw_circle(a, df):
    plt.figure(figsize=(8, 8))
    plt.pie(df[a].value_counts(), autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title('Pie Chart of ' + a)
    plt.show()

def draw_bar(a, b, df):
    df_grouped = df.groupby(a)[b].sum().reset_index().sort_values(by=b, ascending=False)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=a, y=b, data=df_grouped, palette=colors)
    plt.xlabel(a)
    plt.ylabel(b)
    plt.title('Bar Chart of ' + b + ' Grouped by ' + a)
    plt.xticks(rotation=45)
    plt.show()

def draw_hist(a, df):
    plt.figure(figsize=(8, 6))
    plt.hist(df[a], bins=20, color='skyblue', edgecolor='black')
    plt.xlabel(a)
    plt.ylabel('Frequency')
    plt.title('Histogram of ' + a)
    plt.show()

def draw_line(a, b, df):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=a, y=b, data=df, marker='o')
    plt.xlabel(a)
    plt.ylabel(b)
    plt.title('Line Chart of ' + b + ' Over ' + a)
    plt.xticks(rotation=45)
    plt.show()

def draw_box(a, df):
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=a, data=df)
    plt.xlabel(a)
    plt.ylabel('Value')
    plt.title('Box Plot of ' + a)
    plt.xticks(rotation=45)
    plt.show()

def draw_scatter(a, b, df):
    plt.figure(figsize=(10, 6))
    plt.scatter(df[a], df[b], alpha=0.5)
    plt.xlabel(a)
    plt.ylabel(b)
    plt.title('Scatter Plot of ' + a + ' vs ' + b)
    plt.show()

def draw_heatmap(df):
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title('Heatmap of Correlation Matrix')
    plt.show()

def draw_violin(a, b, df):
    plt.figure(figsize=(10, 6))
    sns.violinplot(x=a, y=b, data=df)
    plt.xlabel(a)
    plt.ylabel(b)
    plt.title('Violin Plot of ' + a + ' vs ' + b)
    plt.xticks(rotation=45)
    plt.show()

def draw_pairplot(df):
    sns.pairplot(df)
    plt.title('Pair Plot')
    plt.show()

def draw_jointplot(a, b, df):
    sns.jointplot(x=a, y=b, data=df, kind="scatter")
    plt.xlabel(a)
    plt.ylabel(b)
    plt.title('Joint Plot of ' + a + ' vs ' + b)
    plt.show()

def draw_swarmplot(a, b, df):
    plt.figure(figsize=(10, 6))
    sns.swarmplot(x=a, y=b, data=df)
    plt.xlabel(a)
    plt.ylabel(b)
    plt.title('Swarm Plot of ' + a + ' vs ' + b)
    plt.xticks(rotation=45)
    plt.show()

def draw_boxenplot(a, b, df):
    plt.figure(figsize=(10, 6))
    sns.boxenplot(x=a, y=b, data=df)
    plt.xlabel(a)
    plt.ylabel(b)
    plt.title('Boxen Plot of ' + a + ' vs ' + b)
    plt.xticks(rotation=45)
    plt.show()

def draw_rugplot(a, df):
    plt.figure(figsize=(10, 6))
    sns.rugplot(df[a], height=0.5)
    plt.xlabel(a)
    plt.ylabel('Frequency')
    plt.title('Rug Plot of ' + a)
    plt.show()
