from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget,QMainWindow, QPushButton

import sys


class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('first desktop app')
        button = QPushButton('Click Me')
        self.setCentralWidget(button)
        
app = QApplication(sys.argv)

window = ButtonHolder()
window.show()
app.exec()