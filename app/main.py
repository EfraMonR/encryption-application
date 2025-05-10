import sys
import os
import ctypes
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from controllers.main_controller import MainController

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("efrain.cifrado.app.1.0")

base_path = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(base_path, "assets", "icon.ico")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(icon_path))
    controller = MainController()
    controller.run()
    sys.exit(app.exec_())   