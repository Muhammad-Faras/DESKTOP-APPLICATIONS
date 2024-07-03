from PySide6.QtWidgets import QApplication
from button_holder import ButtonHolder
from slider import SliderHolder
import sys  

app = QApplication(sys.argv)
window = SliderHolder()
window.show()
app.exec()