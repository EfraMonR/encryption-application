from models.cipher_model import cipher_decrypt
from views.decryption_view import DecryptionView

class DecryptionController:
    def __init__(self, main_controller):
        self.view = DecryptionView(main_controller)
        self.view.decrypt_button.clicked.connect(self.decrypt_data)
        self.view.exit_button.clicked.connect(self.exit_view)
        self.main_controller = main_controller

    def decrypt_data(self):
        encrypted_number = self.view.input_field.text()
        
        if not encrypted_number:
            self.view.error_label.setText("El campo no puede estar vacío.")
            return

        if not encrypted_number.isdigit() or len(encrypted_number) != 6:
            self.view.error_label.setText("Debe ser un número entero cifrado de 6 dígitos.")
            return
        
        original_number = cipher_decrypt(encrypted_number)
        
        self.view.result_label.setText(f"Numero cifrado:{encrypted_number}\nNumero original: {original_number}")
        self.view.error_label.setText("")
        self.view.input_field.clear() 
        
    def exit_view(self):
        self.view.input_field.clear()
        self.view.result_label.setText("")
        self.view.error_label.setText("")
        self.view.close()
        self.main_controller.enable_buttons()