from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QSystemTrayIcon, QMenu, QAction, QApplication


class MainView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplicación de cifrado y descifrado")
        self.setGeometry(400, 200, 350, 250)

        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)

        self.title_label = QLabel("Cifrado y Descifrado de Números")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
            color: #00529B;
        """)

        self.author_label = QLabel("Autor: Efrain Montealegre Raga")
        self.author_label.setAlignment(Qt.AlignCenter)
        self.author_label.setStyleSheet("""
            color: #333333;
            font-size: 14px;
            font-style: italic;
            font-weight: bold;
        """)

        self.select_option_label = QLabel("Selecciona una opción:")
        self.select_option_label.setAlignment(Qt.AlignCenter)
        self.select_option_label.setStyleSheet("""
            font-size: 15px;
            color: #000000;
        """)

        self.encrypt_button = QPushButton("Cifrar")
        self.decrypt_button = QPushButton("Descifrar")
        self.encrypt_button.setStyleSheet("""
            QPushButton {
                background-color: #007BFF;
                color: white;
                padding: 8px 16px;
                border: none;
                border-radius: 5px;
                font-size: 15px;
            }
            QPushButton:hover {
                background-color: #339CFF;
            }
        """)

        self.decrypt_button.setStyleSheet("""
            QPushButton {
                background-color: #0056b3;
                color: white;
                padding: 8px 16px;
                border: none;
                border-radius: 5px;
                font-size: 15px;
            }
            QPushButton:hover {
                background-color: #337AB7;
            }
        """)

        button_layout = QHBoxLayout()
        button_layout.setSpacing(15)
        button_layout.addWidget(self.encrypt_button)
        button_layout.addWidget(self.decrypt_button)
        button_layout.setAlignment(Qt.AlignCenter)

        inner_container_layout = QVBoxLayout()
        inner_container_layout.setSpacing(10) 
        inner_container_layout.setContentsMargins(20, 30, 20, 30)
        inner_container_layout.addWidget(self.title_label)
        inner_container_layout.addWidget(self.author_label)
        inner_container_layout.addWidget(self.select_option_label)
        inner_container_layout.addLayout(button_layout)

        inner_container = QWidget()
        inner_container.setLayout(inner_container_layout)
        inner_container.setStyleSheet("""
            background-color: #F0F8FF;
            padding: 10px;
            border-radius: 10px;
        """)

        layout.addWidget(inner_container)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.encrypt_button.setCursor(Qt.PointingHandCursor)
        self.decrypt_button.setCursor(Qt.PointingHandCursor)
        
        self.create_system_tray()
        

    def create_system_tray(self):
        self.tray_icon = QSystemTrayIcon(QIcon("assets/icon.ico"), self)

        tray_menu = QMenu()
        
        exit_action = QAction("Salir", self)
        exit_action.triggered.connect(self.close)
        tray_menu.addAction(exit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()
        QTimer.singleShot(1000, self.show_message)

    def show_message(self):
        self.tray_icon.showMessage(
            "Bienvenido",
            "La aplicación de cifrado y descifrado está en ejecución.",
            QIcon("assets/icon.ico")
        )