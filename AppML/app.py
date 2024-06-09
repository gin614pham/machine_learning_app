from app_ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox, QVBoxLayout, QWidget
import pandas as pd
from ModelTrain import train
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mplcanvas import MplCanvas
from sklearn.tree import plot_tree
import seaborn as sns
import numpy as np

ROW = 1
COLUMN = 0


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("AppML")
        # set full screen
        self.showMaximized()
        self.btnQuit.setShortcut("Ctrl+Q")

        self.btnQuit.clicked.connect(self.quit_app)
        self.btnReadFile.clicked.connect(self.read_file)
        # set btnClear to switch page
        self.btnHome.clicked.connect(self.on_click_home)
        self.btnClear.clicked.connect(self.on_click_clear_data)
        self.btnTrain.clicked.connect(self.on_click_train)

        self.btnInfo.clicked.connect(self.check_info_data)
        self.btnNaN.clicked.connect(self.check_null_data)
        self.btnDuplicate.clicked.connect(self.check_duplicate_data)
        self.btnRunEditNull.clicked.connect(self.on_click_run_edit_null)
        self.btnSave.clicked.connect(self.on_click_save)
        self.btnSaveCSV.clicked.connect(self.on_click_save_data)
        self.btnDeleteDuplicate.clicked.connect(self.on_click_del_duplicate)
        self.btnAddColumn.clicked.connect(self.on_click_add_column)
        self.btnDelColumn.clicked.connect(self.on_click_remove_column)
        self.btnTrainModel.clicked.connect(self.on_click_train_model)
        self.btnToNumeric.clicked.connect(self.on_click_convert_numeric)

        self.comboBoxTargetColumn.currentTextChanged.connect(
            self.on_target_column_change)

        # set home page
        self.stackedWidget.setCurrentIndex(0)

        self.plot_layout = QVBoxLayout(self.widgetMatplotlib)
        self.canvas = MplCanvas(self.widgetMatplotlib,
                                width=5, height=4, dpi=100)
        self.plot_layout.addWidget(self.canvas)
        self.plot_sample_data()

    def plot_sample_data(self):
        # Vẽ một biểu đồ mẫu
        t = [0, 1, 2, 3, 4, 5]
        s = [0, 1, 4, 9, 16, 25]

        self.canvas.axes.plot(t, s)
        self.canvas.draw()

    def read_file(self):
        # read file csv
        file_name, _ = QFileDialog.getOpenFileName(
            self.centralwidget, "Open CSV File", "", "CSV Files (*.csv)"
        )

        if file_name:
            self.df_name = file_name.split("/")[-1]
            self.labelReadFile.setText(self.df_name)
            self.labelReadFile.adjustSize()

            self.df = pd.read_csv(file_name)

            # get name column table
            self.set_table_data()

            self.df_copy = self.df
            self.switch_page(0)

    def set_table_data(self):
        self.tableData.setRowCount(0)
        self.tableData.setColumnCount(0)

        column = self.df.columns
        self.tableData.setColumnCount(len(column))
        self.tableData.setHorizontalHeaderLabels(column)

        # set row data table
        self.tableData.setRowCount(len(self.df))

        # set table data
        for i in range(len(self.df)):
            for j in range(len(column)):
                self.tableData.setItem(
                    i, j, QTableWidgetItem(str(self.df.iloc[i, j]))
                )
        self.tableData.resizeColumnsToContents()
        self.tableData.verticalHeader().setVisible(False)

    def on_click_home(self):
        self.switch_page(0)
        self.set_table_data()

    def on_click_chart(self):
        self.switch_page(2)

    def on_click_train(self):
        self.switch_page(3)
        self.load_page_train()

    def switch_page(self, index):
        self.stackedWidget.setCurrentIndex(index)

        if index == 0:
            self.btnHome.setChecked(True)
            self.btnClear.setChecked(False)
        elif index == 1:
            self.btnHome.setChecked(False)
            self.btnClear.setChecked(True)

    def quit_app(self):
        # check if user want to quit
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setText("Do you want to quit?")
        msg.setInformativeText("Are you sure?")
        msg.setWindowTitle("Quit App")
        msg.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        response = msg.exec()

        if response == QMessageBox.StandardButton.Yes:
            self.close()

    def error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText("This is an error message!")
        msg.setInformativeText(message)
        msg.setWindowTitle("Error, please try again")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

    def check_info_data(self):
        if self.tableData.rowCount() == 0:
            self.error_message("No data, please read file")
            return

        info = {
            "Column": [],
            "Non-Null Count": [],
            "Data Type": [],
        }

        for col in self.df_copy.columns.tolist():
            info["Column"].append(col)
            info["Non-Null Count"].append(self.df_copy[col].count())
            info["Data Type"].append(self.df_copy[col].dtype)

        data = pd.DataFrame(info)
        html_table = data.to_html(index=False)

        memory_usage = self.get_memory_usage()
        html_table = html_table + "<br> Memory usage: " + \
            str(memory_usage["Memory usage"])
        self.textInfo.setText(html_table)

    def get_memory_usage(self):
        memory_usage = self.df_copy.memory_usage(deep=True).sum()
        memory_usage_dict = {'Memory usage': memory_usage}
        for unit in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if memory_usage < 1024.0:
                memory_usage_dict['Memory usage'] = "{:3.1f}+ {}".format(
                    memory_usage, unit)
                break
            else:
                memory_usage /= 1024.0
        return memory_usage_dict

    def check_null_data(self):
        if self.tableData.rowCount() == 0:
            self.error_message("No data, please read file")
            return
        info = {
            "Column": [],
            "Sum NaN": [],
            "Percent NaN": [],
            "Data Type": [],
        }

        sum_nan = self.df_copy.isna().sum()
        percent_nan = (self.df_copy.isna().mean() *
                       100).round(2).astype(str) + "%"

        info["Column"] = self.df_copy.columns.tolist()
        info["Sum NaN"] = sum_nan
        info["Percent NaN"] = percent_nan
        info["Data Type"] = self.df_copy.dtypes

        data = pd.DataFrame(info)
        html_table = data.to_html(index=False)
        self.textInfo.setText(html_table)

    def check_duplicate_data(self):
        if self.tableData.rowCount() == 0:
            self.error_message("No data, please read file")
            return
        info = {
            "Column": [],
            "Sum Duplicate": [],
            "Percent Duplicate": [],
            "Data Type": [],
        }

        sum_duplicate = self.df_copy.duplicated().sum()
        percent_duplicate = (self.df_copy.duplicated().mean()
                             * 100).round(2).astype(str) + "%"

        info["Column"] = self.df_copy.columns.tolist()
        info["Sum Duplicate"] = sum_duplicate
        info["Percent Duplicate"] = percent_duplicate
        info["Data Type"] = self.df_copy.dtypes

        data = pd.DataFrame(info)
        html_table = data.to_html(index=False)
        self.textInfo.setText(html_table)

    def on_click_run_edit_null(self):
        edit_in = self.comboBoxEditIn.currentIndex()
        column_select = self.comboBoxSelectColumn.currentText()
        # get button radio choice in QButtonGroup btnGTypeNullEdit
        type_edit = self.btnGTypeNullEdit.checkedButton().text()
        replace_type = self.comboBoxReplace.currentText()

        self.edit_null_data(edit_in, column_select, type_edit, replace_type)

    def on_click_clear_data(self):
        self.switch_page(1)
        self.df_copy = self.df
        self.load_data_combobox_select_column()

    def load_data_combobox_select_column(self):
        self.comboBoxSelectColumn.clear()
        self.comboBoxSelectColumn.addItem("All Columns")
        for col in self.df_copy.columns.tolist():
            self.comboBoxSelectColumn.addItem(col)

    def on_click_save(self):
        self.df = self.df_copy

    def on_click_save_data(self):
        # choses location to save
        name = self.df_name.replace(".csv", "") + "_clean.csv"
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(
            self.centralwidget, "Save File", name, "CSV Files (*.csv)", options=options
        )

        if file_name:
            try:
                self.df.to_csv(file_name, index=False)
                QMessageBox.information(
                    self, "Saved", "Data saved successfully")
            except:
                QMessageBox.warning(self, "Error", "Error saving data")

    def edit_null_data(self, edit_in, column_select, type_edit, replace_type):
        if edit_in == COLUMN:
            if column_select == "All Columns":
                if type_edit == "Replace":
                    if replace_type == "Mean":
                        self.df_copy = self.df_copy.fillna(
                            self.df_copy.mean(numeric_only=True)
                        )
                    elif replace_type == "Median":
                        self.df_copy = self.df_copy.fillna(
                            self.df_copy.median(numeric_only=True)
                        )
                    elif replace_type == "Mode":
                        self.df_copy = self.df_copy.fillna(
                            self.df_copy.mode().loc[0])
                elif type_edit == "Delete":
                    self.df_copy = self.df_copy.dropna(axis=1)
            else:
                if type_edit == "Replace":
                    if replace_type == "Mean":
                        mean = self.df_copy[column_select].mean()
                        self.df_copy[column_select] = self.df_copy[column_select].fillna(
                            mean)
                    elif replace_type == "Median":
                        median = self.df_copy[column_select].median()
                        self.df_copy[column_select] = self.df_copy[column_select].fillna(
                            median
                        )
                    elif replace_type == "Mode":
                        mode = self.df_copy[column_select].mode().loc[0]
                        self.df_copy[column_select] = self.df_copy[column_select].fillna(
                            mode
                        )
                elif type_edit == "Delete":
                    self.df_copy = self.df_copy.drop(columns=[column_select])

        elif edit_in == ROW:
            if column_select == "All Columns":
                if type_edit == "Replace":
                    if replace_type == "Mean":
                        self.df_copy = self.df_copy.fillna(self.df_copy.mean())
                    elif replace_type == "Median":
                        self.df_copy = self.df_copy.fillna(
                            self.df_copy.median())
                    elif replace_type == "Mode":
                        self.df_copy = self.df_copy.fillna(
                            self.df_copy.mode().loc[0])
                elif type_edit == "Delete":
                    self.df_copy = self.df_copy.dropna()
            else:
                if type_edit == "Replace":
                    if replace_type == "Mean":
                        self.df_copy[column_select] = self.df_copy[column_select].fillna(
                            self.df_copy[column_select].mean())
                    elif replace_type == "Median":
                        self.df_copy[column_select] = self.df_copy[column_select].fillna(
                            self.df_copy[column_select].median())
                    elif replace_type == "Mode":
                        self.df_copy[column_select] = self.df_copy[column_select].fillna(
                            self.df_copy[column_select].mode()[0])
                elif type_edit == "Delete":
                    self.df_copy[column_select] = self.df_copy[column_select].dropna(
                    )

    def on_click_del_duplicate(self):
        self.df_copy = self.df_copy.drop_duplicates()

    def on_click_convert_numeric(self):
        columns = self.df_copy.columns
        for col in columns:
            if self.df_copy[col].dtype == 'object':
                try:
                    self.df_copy[col] = self.df_copy[col].astype(
                        'category').cat.codes
                except ValueError:
                    pass

    def load_page_train(self):
        columns = self.df.columns

        # add columns to combobox
        self.comboBoxTargetColumn.clear()
        for col in columns:
            self.comboBoxTargetColumn.addItem(col)

        # add columns to List Widget
        self.listWidgetColumns.clear()
        for col in columns:
            self.listWidgetColumns.addItem(col)
        self.listWidgetColumnSelected.clear()

        self.on_target_column_change()

    def on_target_column_change(self):
        column = self.comboBoxTargetColumn.currentText()
        columns = self.df.columns

        self.listWidgetColumnSelected.clear()
        self.listWidgetColumns.clear()
        for col in columns:
            if col != column:
                self.listWidgetColumns.addItem(col)

    def on_click_add_column(self):
        self.listWidgetColumnSelected.addItem(
            self.listWidgetColumns.currentItem().text())
        self.listWidgetColumns.takeItem(
            self.listWidgetColumns.currentRow())

    def on_click_remove_column(self):
        self.listWidgetColumns.addItem(
            self.listWidgetColumnSelected.currentItem().text())
        self.listWidgetColumnSelected.takeItem(
            self.listWidgetColumnSelected.currentRow())

    def on_click_train_model(self):
        target_column = self.comboBoxTargetColumn.currentText()
        selected_columns = [self.listWidgetColumnSelected.item(
            i).text() for i in range(self.listWidgetColumnSelected.count())]
        model_type = self.comboBoxTypeModel.currentText()
        if model_type == "Linear Regression":
            mse, r2, X_test, y_pred = train(
                self.df, target_column, selected_columns, model_type)
            self.plot_linear_regression(X_test, y_pred)
        elif model_type == "Logistic Regression":
            mse, r2, accuracy, cm = train(
                self.df, target_column, selected_columns, model_type
            )
            self.plot_logistic_regression(cm, accuracy)
        elif model_type == "KNN":
            mse, r2, y_test, y_pred, best_k, accuracy3 = train(
                self.df, target_column, selected_columns, model_type
            )
            self.plot_knn(y_test, y_pred, best_k, accuracy3)
        elif model_type == "Decision Tree":
            mse, r2, model, columns = train(
                self.df, target_column, selected_columns, model_type
            )
            self.plot_decision_tree(model, columns)

    def plot_linear_regression(self, X_test: pd.DataFrame, y_pred: pd.Series):
        self.canvas.axes.clear()  # Clear previous plot
        self.canvas.axes.scatter(
            X_test.iloc[:, 0], y_pred, label='Predicted values')
        self.canvas.axes.plot([min(X_test.iloc[:, 0]), max(X_test.iloc[:, 0])],
                              [min(y_pred), max(y_pred)], color='red', linestyle='--', label='Trend line')
        self.canvas.axes.set_xlabel("X values (first column)")
        self.canvas.axes.set_ylabel("Predicted Y values")
        self.canvas.axes.set_title("Predicted Y values based on X values")
        self.canvas.axes.legend()
        self.canvas.draw()

    def plot_logistic_regression(self, cm: np.ndarray, accuracy: float):
        self.canvas.axes.clear()  # Clear previous plot
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=self.canvas.axes)
        self.canvas.axes.text(-0.1, 1.05, f"Accuracy: {accuracy:.4f}", ha='left',
                              va='center', transform=self.canvas.axes.transAxes, fontsize=10)
        self.canvas.axes.set_title('Confusion Matrix')
        self.canvas.axes.set_xlabel('Predicted')
        self.canvas.axes.set_ylabel('Actual')
        self.canvas.draw()

    def plot_knn(self, y_test: pd.Series, y_pred: pd.Series, best_k: int, accuracy3: float):
        self.canvas.axes.clear()
        self.canvas.axes.scatter(y_test, y_pred)
        self.canvas.axes.set_xlabel("Giá trị thực tế")
        self.canvas.axes.set_ylabel("Giá trị dự đoán")
        self.canvas.axes.set_title("So sánh giá trị thực tế và dự đoán")

        self.canvas.axes.text(-0.1, 1.05, f"k = {best_k}", ha='left',
                              va='center', transform=self.canvas.axes.transAxes, fontsize=10)

        self.canvas.axes.plot([min(y_test), max(y_test)], [min(
            y_test), max(y_test)], linestyle='--', color='red')
        self.canvas.axes.text(max(y_test) * 0.7, min(y_test) * 1.1,
                              f'Accuracy: {accuracy3:.2f}', fontsize=12, color='blue')

        self.canvas.draw()

    def plot_decision_tree(self, model, columns):
        self.canvas.axes.clear()  # Clear previous plot

        plot_tree(model, feature_names=columns, class_names=[str(
            i) for i in model.classes_], filled=True, fontsize=8, impurity=False, rounded=True, max_depth=3, ax=self.canvas.axes)
        self.canvas.draw()
