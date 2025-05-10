from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel, QVBoxLayout, QWidget

class DecryptionView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Descifrado")
        self.setGeometry(400, 400, 320, 220)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Ingresa el número cifrado")
        self.input_field.setAlignment(Qt.AlignCenter)
        self.input_field.setStyleSheet("""
            padding: 6px;
            font-size: 14px;
            border: 1px solid #388e3c;
            border-radius: 5px;
        """)

        self.decrypt_button = QPushButton("Descifrar")
        self.decrypt_button.setStyleSheet("""
            background-color: #28a745;
            color: white;
            padding: 8px;
            font-size: 15px;
            border: none;
            border-radius: 5px;
        """)
        self.decrypt_button.setCursor(Qt.PointingHandCursor)

        self.exit_button = QPushButton("Salir")
        self.exit_button.setStyleSheet("""
            background-color: #6c757d;
            color: white;
            padding: 8px;
            font-size: 15px;
            border: none;
            border-radius: 5px;
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
            color: red;
            font-size: 13px;
        """)

        layout.addWidget(self.input_field)
        layout.addWidget(self.decrypt_button)
        layout.addWidget(self.exit_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.error_label)

        container = QWidget()
        container.setLayout(layout)
        container.setStyleSheet("""
            background-color: #e9f7ef;
            border-radius: 10px;
        """)

        self.setCentralWidget(container)
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.decrypt_button.click()
    
    def closeEvent(self, event):
        self.input_field.clear()
        self.result_label.setText("")
        self.error_label.setText("")
        event.accept()
