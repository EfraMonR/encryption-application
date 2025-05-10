from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit

class EncryptionView(QMainWindow):
    def __init__(self, main_controller):        
        super().__init__()
        self.main_controller = main_controller

        self.setWindowTitle("Cifrado")
        self.setGeometry(400, 400, 350, 250)

        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Ingresa un número de 6 dígitos")
        self.input_field.setAlignment(Qt.AlignCenter)
        self.input_field.setStyleSheet("""
            padding: 8px;
            font-size: 14px;
            border: 1px solid #007BFF;
            border-radius: 5px;
        """)

        self.encrypt_button = QPushButton("Cifrar")
        self.encrypt_button.setStyleSheet("""
            QPushButton {
                background-color: #007BFF;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 5px;
                font-size: 15px;
            }
            QPushButton:hover {
                background-color: #339CFF;
            }
            QPushButton:pressed {
                background-color: #0056b3;
            }
        """)
        self.encrypt_button.setCursor(Qt.PointingHandCursor)

        self.exit_button = QPushButton("Salir")
        self.exit_button.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 5px;
                font-size: 15px;
            }
            QPushButton:hover {
                background-color: #868e96;
            }
            QPushButton:pressed {
                background-color: #545b62;
            }
        """)
        self.exit_button.setCursor(Qt.PointingHandCursor)

        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("""
            font-size: 16px;
            font-weight: bold;
            color: #155724;
        """)

        self.error_label = QLabel("")
        self.error_label.setAlignment(Qt.AlignCenter)
        self.error_label.setStyleSheet("""
            font-size: 13px;
            color: red;
        """)

        layout.addWidget(self.input_field)
        layout.addWidget(self.encrypt_button)
        layout.addWidget(self.exit_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.error_label)

        container = QWidget()
        container.setLayout(layout)
        container.setStyleSheet("""
            background-color: #E6F0FF;
            border-radius: 10px;
        """)

        self.setCentralWidget(container)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.encrypt_button.click()

    def closeEvent(self, event):
        self.input_field.clear()
        self.result_label.setText("")
        self.error_label.setText("")
        self.main_controller.enable_buttons()
        event.accept()
