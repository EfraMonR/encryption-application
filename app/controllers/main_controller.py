from views.main_view import MainView
from controllers.encryption_controller import EncryptionController
from controllers.decryption_controller import DecryptionController

class MainController:
    def __init__(self):
        self.view = MainView()
        self.encrypt_controller = EncryptionController(self)
        self.decrypt_controller = DecryptionController(self)

        self.view.encrypt_button.clicked.connect(self.show_encrypt_window)
        self.view.decrypt_button.clicked.connect(self.show_decrypt_window)

    def show_encrypt_window(self):
        self.disable_buttons()
        self.encrypt_controller.view.show()

    def show_decrypt_window(self):
        self.disable_buttons()
        self.decrypt_controller.view.show()
        
    def disable_buttons(self):
        self.view.encrypt_button.setEnabled(False)
        self.view.decrypt_button.setEnabled(False)
    
    def enable_buttons(self):   
        self.view.encrypt_button.setEnabled(True)
        self.view.decrypt_button.setEnabled(True)

    def run(self):
        self.view.show()