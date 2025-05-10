from core.cipher_logic import encrypt, decrypt

def cipher_encrypt(number: int) -> str:
    return encrypt(number)

def cipher_decrypt(encrypted: str) -> str:
    return decrypt(encrypted)