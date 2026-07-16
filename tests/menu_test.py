import sys
from PySide6.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Menu Test")

menu = window.menuBar()
file_menu = menu.addMenu("File")
help_menu = menu.addMenu("Help")

window.show()

app.exec()