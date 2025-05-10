import sys
import ctypes
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from controllers.main_controller import MainController

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("efrain.cifrado.app.1.0")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_icon = QIcon("assets/icon.ico")
    app.setWindowIcon(app_icon)
    controller = MainController()
    controller.run()
    sys.exit(app.exec_())   