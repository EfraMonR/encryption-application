from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit

class DecryptionView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Descifrado")

        layout = QVBoxLayout()
        self.label = QLabel("Ingrese el número cifrado de 6 dígitos para descifrar:")
        self.input_field = QLineEdit()
        self.decrypt_button = QPushButton("Descifrar")
        self.result_label = QLabel("")

        layout.addWidget(self.label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.decrypt_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)