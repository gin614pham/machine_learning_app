from PySide6.QtWidgets import QApplication
import sys
from app import MainWindow

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
