# import libraries for Linear Regression, Logistic Regression, and Decision Tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, mean_squared_error, r2_score, accuracy_score, confusion_matrix

# fun for Logistic Regression


def train(df, target, columns, AI):
    if AI == 'Linear Regression':
        return Linear_Regression(df, target, columns)
    elif AI == 'Logistic Regression':
        return Logistic_Regression(df, target, columns)
    elif AI == 'KNN':
        return KNN(df, target, columns)
    elif AI == 'Decision Tree':
        return Decision_Tree(df, target, columns)
    elif AI == 'Random Forest':
        return Random_Forest(df, target, columns)


def Logistic_Regression(df, target, columns):
    X = df[columns]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    return accuracy, report, cm


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
    return mse, r2, X_test, y_pred


def KNN(df, target, columns):
    X = df[columns]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    k_values = [1, 3, 5, 7, 9, 11]

    best_accuracy = 0
    best_k = None
    for k in k_values:
        knn_model = KNeighborsClassifier(n_neighbors=k)
        knn_model.fit(X_train, y_train)
        y_pred = knn_model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_k = k
    model = KNeighborsClassifier(n_neighbors=best_k)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    accuracy_final = accuracy_score(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mse, r2, y_test, y_pred, best_k, accuracy_final


def Decision_Tree(df, target, columns):
    X = df[columns]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    return accuracy, report, model, columns


def Random_Forest(df, target, columns):
    X = df[columns]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    return accuracy, report, cm
