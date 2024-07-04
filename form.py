from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QWidget, QPushButton, QTextEdit
class FormClass(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Create labels and input fields
        first_name_label = QLabel("First Name")
        self.first_name_input = QLineEdit()

        last_name_label = QLabel("Last Name")
        self.last_name_input = QLineEdit()
        
        bio_label = QLabel("Bio")
        self.bio_input = QTextEdit()
        submit_button = QPushButton('Submit')
        submit_button.clicked.connect(self.button_clicked)
        
        # Create a horizontal layout for first name
        first_name_layout = QHBoxLayout()
        first_name_layout.addWidget(first_name_label)
        first_name_layout.addWidget(self.first_name_input)
        
        # Create a horizontal layout for last name
        last_name_layout = QHBoxLayout()
        last_name_layout.addWidget(last_name_label)
        last_name_layout.addWidget(self.last_name_input)
        
        # Create a vertical layout and add horizontal layouts
        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addLayout(first_name_layout)
        self.vertical_layout.addLayout(last_name_layout)
        self.vertical_layout.addWidget(bio_label)
        self.vertical_layout.addWidget(self.bio_input)
        self.vertical_layout.addWidget(submit_button)
        
        # Labels for displaying results
        self.result_label = QLabel("")
        self.bio_result_label = QLabel("")
        self.vertical_layout.addWidget(self.result_label)
        self.vertical_layout.addWidget(self.bio_result_label)
        
        # Add a vertical stretch to push items to the top
        self.vertical_layout.addStretch(1)
        
        # Create a central widget and set the layout on it
        central_widget = QWidget()
        central_widget.setLayout(self.vertical_layout)
        
        # Set the central widget of the QMainWindow
        self.setCentralWidget(central_widget)

    def button_clicked(self):
        # Update the result labels with the text from the input fields
        self.result_label.setText(f"Full Name: {self.first_name_input.text()} {self.last_name_input.text()}")
        self.bio_result_label.setText(f"bio: {self.bio_input.toPlainText()}")
