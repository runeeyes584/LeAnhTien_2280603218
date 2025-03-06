class VigenereCipher:
    def __init__(self):
        pass
    
    def vigenere_encrypt(self, plain_text, key):
        encrypted_text = ""
        key_index = 0
        for letter in plain_text:
            if letter.isalpha():
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')
                if letter.isupper():
                    encrypted_text += chr((ord(letter) - ord('A') + key_shift) % 26 + ord('A'))
                else:
                    encrypted_text += chr((ord(letter) - ord('a') + key_shift) % 26 + ord('a'))
                key_index += 1
            else:
                encrypted_text += letter
        return encrypted_text
    
    def vigenere_decrypt(self, cipher_text, key):
        decrypted_text = ""
        key_index = 0
        for letter in cipher_text:
            if letter.isalpha():
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')
                if letter.isupper():
                    decrypted_text += chr((ord(letter) - ord('A') - key_shift) % 26 + ord('A'))
                else:
                    decrypted_text += chr((ord(letter) - ord('a') - key_shift) % 26 + ord('a'))
                key_index += 1
            else:
                decrypted_text += letter
        return decrypted_text
    