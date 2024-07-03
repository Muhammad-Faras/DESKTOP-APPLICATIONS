from PySide6.QtWidgets import QApplication
from button_holder import ButtonHolder
from slider import SliderHolder
from QWidget import RockWidget
import sys  

app = QApplication(sys.argv)
window = RockWidget()
window.show()
app.exec()