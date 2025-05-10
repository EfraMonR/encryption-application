def encrypt(number: int) -> str:
    digits = [int(d) for d in str(number)]
    encrypted_digits = [(d + 7) % 10 for d in digits]

    encrypted_digits[0], encrypted_digits[2] = encrypted_digits[2], encrypted_digits[0]
    encrypted_digits[1], encrypted_digits[3] = encrypted_digits[3], encrypted_digits[1]
    encrypted_digits[4], encrypted_digits[5] = encrypted_digits[5], encrypted_digits[4]

    return ''.join(str(d) for d in encrypted_digits)

def decrypt(encrypted: str) -> str:
    digits = [int(d) for d in encrypted]

    digits[0], digits[2] = digits[2], digits[0]
    digits[1], digits[3] = digits[3], digits[1]
    digits[4], digits[5] = digits[5], digits[4]

    original_digits = [(d - 7 + 10) % 10 for d in digits]

    return ''.join(str(d) for d in original_digits)