from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel

class MainView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicación de Cifrado")

        layout = QVBoxLayout()
        self.label = QLabel("Autor: Efrain Montealegre Raga")
        self.encrypt_button = QPushButton("Cifrar")
        self.decrypt_button = QPushButton("Descifrar")

        layout.addWidget(self.label)
        layout.addWidget(self.encrypt_button)
        layout.addWidget(self.decrypt_button)

        self.setLayout(layout)