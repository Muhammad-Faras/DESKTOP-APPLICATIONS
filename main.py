from PySide6.QtWidgets import QApplication, QWidget,QMainWindow, QPushButton

import sys
app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle('first pyside6 app')
button = QPushButton()
button.setText('clcik me')
window.setCentralWidget(button)
window.show()
app.exec()