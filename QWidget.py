from PySide6.QtWidgets import QMainWindow,QWidget, QPushButton, QMdiArea, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Slot

class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('First Desktop App')
        
        button1 = QPushButton('button 1')
        button1.clicked.connect(self.say_hello)
        
        button2 = QPushButton('button 2')
        button2.clicked.connect(self.say_hello)
        
        widgetlayout = QHBoxLayout()
        widgetlayout.addWidget(button1)
        widgetlayout.addWidget(button2)
        self.setLayout(widgetlayout)
        
    
    @Slot()
    def say_hello(self,data):
        print("Button clicked, Hello!", data)
