from PySide6.QtWidgets import QMainWindow, QToolBar, QStatusBar
from PySide6.QtCore import Slot, QSize,Qt

class ToolbarClass(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        
        
        """
            ========================   MenuBar   =======================
        """
        
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

        
        """
            ========================   Toolbar   =======================
        """
        
        toolbar = QToolBar('my toolbar')
        toolbar.setIconSize(QSize(30,30))
        self.addToolBar(toolbar)     
        # self.setGeometry(300, 300, 400, 300)
        
        # Apply custom style
        self.setStyleSheet("""
            QToolBar QToolButton {
                background-color: blue; 
                border: 1px solid black;
                padding: 5%;
                border-radius:20px;
                color:white;
            }
            QToolBar QToolButton:hover {
                background-color: orange;
            }
        """)
        exit_toolbar = toolbar.addAction('Exit')
        exit_toolbar.setStatusTip("exit the application")
        exit_toolbar.triggered.connect(self.exit_application_slot)
        toolbar.addSeparator()
        toolbar.insertSeparator(exit_toolbar)
        
        toolbar.addAction('New')   
        toolbar.addAction('Edit')   
        
        """
            ========================   StatusBar   =======================
        """
        self.setStatusBar(QStatusBar())
        
        
        
    @Slot()
    def exit_application_slot(self):
        print('app exit')
        self.statusBar().showMessage('Exit from app')
        self.app.exit()
        