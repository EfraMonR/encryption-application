from models.cipher_model import cipher_encrypt
from views.encryption_view import EncryptionView

class EncryptionController:
    def __init__(self, main_controller):
        self.view = EncryptionView(main_controller)
        self.view.encrypt_button.clicked.connect(self.encrypt_data)
        self.view.exit_button.clicked.connect(self.exit_view)
        self.main_controller = main_controller

    def encrypt_data(self):
        number = self.view.input_field.text()

        if not number:
            self.view.error_label.setText("El campo no puede estar vacío.")
            return
        
        if not number.isdigit() or len(number) != 6:
            self.view.error_label.setText("Debe ser un número entero de 6 dígitos.")
            return
        
        encrypted_number = cipher_encrypt(int(number))

        self.view.result_label.setText(f"Numero original: {number}\nNumero cifrado: {encrypted_number}")   
        self.view.error_label.setText("")
        self.view.input_field.clear() 
        
    def exit_view(self):
        self.view.input_field.clear()
        self.view.result_label.setText("")
        self.view.error_label.setText("")
        self.view.close()
        self.main_controller.enable_buttons()