from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit

class EncryptionView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cifrado de Números")

        layout = QVBoxLayout()
        self.label = QLabel("Ingrese un número entero de 6 dígitos para cifrar:")
        self.input_field = QLineEdit()
        self.encrypt_button = QPushButton("Cifrar")
        self.result_label = QLabel("")

        layout.addWidget(self.label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.encrypt_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)