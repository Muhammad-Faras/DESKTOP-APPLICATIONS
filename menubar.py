from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot

class MenuClass(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        # Create a menu bar
        menu_bar = self.menuBar()

        # Create a file menu
        file_menu = menu_bar.addMenu("&File")
        quit_app = file_menu.addAction('Quit')
        quit_app.triggered.connect(self.exit_application_slot)
        
        
        # Create a file menu
        edit_menu = menu_bar.addMenu("&Edit")
        edit_menu_action = edit_menu.addAction('Copy')
        edit_menu_action = edit_menu.addAction('Cut')
        edit_menu_action = edit_menu.addAction('Paste')
        edit_menu_action = edit_menu.addAction('Undo')
        edit_menu_action = edit_menu.addAction('Redo')
        
        
        file_menu = menu_bar.addMenu("Window")
        file_menu = menu_bar.addMenu("Setting")
        file_menu = menu_bar.addMenu("Help")
        file_menu = menu_bar.addMenu("Faras")
        
    @Slot()
    def exit_application_slot(self):
        print('app exit')
        self.app.exit()
        