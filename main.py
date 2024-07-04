from PySide6.QtWidgets import QApplication
from button_holder import ButtonHolder
from slider import SliderHolder
from QWidget import RockWidget
from menubar import MenuClass
import sys  

app = QApplication(sys.argv)
window = MenuClass(app)
window.show()
app.exec()