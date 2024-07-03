from PySide6.QtWidgets import QMainWindow, QSlider
from PySide6.QtCore import Slot
from PySide6.QtCore import Qt
class SliderHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('First Desktop App')
        
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(1)
        slider.setMaximum(100)
        slider.setValue(25)
        slider.valueChanged.connect(self.say_hello)
        self.setCentralWidget(slider)
    
    @Slot(int)
    def say_hello(self,data):
        print("Button clicked, Hello!", data)
