from PySide6.QtWidgets import QMainWindow, QPushButton, QMdiArea
from PySide6.QtCore import Slot

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('First Desktop App')
        
        button = QPushButton('Click me')
        self.setCentralWidget(button)
        button.setCheckable(True)
        # Connect button clicked signal to say_hello slot
        button.clicked.connect(self.say_hello)
    
    @Slot()
    def say_hello(self,data):
        print("Button clicked, Hello!", data)
