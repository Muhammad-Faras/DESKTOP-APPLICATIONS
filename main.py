from PySide6.QtWidgets import QApplication
from button_holder import ButtonHolder
from slider import SliderHolder
from QWidget import RockWidget
from menubar import MenuClass
from toolbar import ToolbarClass
from QMessageBox import QMessageClass
from form import FormClass
import sys  

app = QApplication(sys.argv)
window = FormClass()
window.setWindowTitle('https://github.com/Muhammad-Faras')
# window.setGeometry(0, 0, 900, 900)
window.show()
app.exec()