from PySide6.QtWidgets import QMainWindow, QMessageBox, QPushButton,QHBoxLayout
from PySide6.QtCore import Slot
class QMessageClass(QMainWindow):
    def __init__(self,app):
        super().__init__()
        self.app = app

        # Create a button and set it as the central widget
        button = QPushButton('Click Me', self)
        layout = QHBoxLayout()
        
        layout.addWidget(button)
        self.setLayout(layout)
        

        # Connect button click to a slot method
        button.clicked.connect(self.show_message)

    def show_message(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setText("Button clicked!")
        msg_box.exec()

        
        
