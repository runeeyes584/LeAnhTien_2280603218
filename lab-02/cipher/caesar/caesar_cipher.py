from cipher.caesar import ALPHABET

class caesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET
        
    def encrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        encrypted_text = []
        for letter in text:
            letter_index = self.alphabet.index(letter)
            ouput_index = (letter_index + key) % alphabet_len
            output_letter = self.alphabet[ouput_index]
            encrypted_text.append(output_letter)
        return "".join(encrypted_text)
    def decrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        decrypted_text = []
        for letter in text:
            letter_index = self.alphabet.index(letter)
            ouput_index = (letter_index - key) % alphabet_len
            output_letter = self.alphabet[ouput_index]
            decrypted_text.append(output_letter)
        return "".join(decrypted_text)
                