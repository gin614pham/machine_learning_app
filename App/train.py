# import libraries for Linear Regression, Logistic Regression, and Decision Tree
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix

# fun for Logistic Regression
def train(df, target,columns, AI):
    if AI == 'Linear Regression':
        return Linear_Regression(df, target, columns)
    elif AI == 'Logistic Regression':
        return Logistic_Regression(df, target, columns)
    elif AI == 'KNN':
        return KNN(df, target, columns)

def Logistic_Regression(df, target, columns):
    X = df[columns]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred.round())
    cm = confusion_matrix(y_test, y_pred.round())
    draw_heatmap_plot(accuracy, cm)
    print(mse, r2)
    return mse, r2


def Linear_Regression(df, target, columns):
    X = df[columns]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    plt.scatter(y_test, y_pred)
    plt.xlabel("Giá trị thực tế")
    plt.ylabel("Giá trị dự đoán")
    plt.title("So sánh giá trị thực tế và dự đoán")
    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], linestyle='--', color='red')  # Đường chéo
    plt.text(max(y_test) * 0.7, min(y_test) * 1.1, f'MSE: {mse:.2f}', fontsize=12, color='blue')  # Hiển thị MSE
    plt.show()
    print(mse, r2)
    return mse, r2
def KNN(df, target, columns):
    X = df[columns]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    k = 5
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    plt.scatter(y_test, y_pred)
    plt.xlabel("Giá trị thực tế")
    plt.ylabel("Giá trị dự đoán")
    plt.title("So sánh giá trị thực tế và dự đoán")

# Thêm đường thẳng MSE
    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], linestyle='--', color='red')  # Đường chéo
    plt.text(max(y_test) * 0.7, min(y_test) * 1.1, f'MSE: {mse:.2f}', fontsize=12, color='blue')  # Hiển thị MSE

    plt.show()
    print(mse, r2)
    return mse, r2
def draw_heatmap_plot(accuracy, cm):
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.text(-0.1, 1.05, f"Accuracy: {accuracy:.4f}", ha='left', va='center', transform=plt.gca().transAxes, fontsize=10)
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()