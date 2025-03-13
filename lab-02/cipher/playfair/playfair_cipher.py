class PlayFairCipher:
    def __init__(self) -> None:
        pass
    
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I")
        key = key.upper()
        key_set = set(key)
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        remaining_letter = [letter for letter in alphabet if letter not in key_set]
        matrix = list(key)
        for letter in remaining_letter:
            matrix.append(letter)
            if len(matrix) == 25:
                break
        playfair_matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
        return playfair_matrix
    
    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
    
    def playfair_encrypt(self, matrix, plaintext):
        plaintext = plaintext.replace("J", "I")
        plaintext = plaintext.upper()
        encrypted_text = ""
        for i in range(0, len(plaintext), 2):
            pair = plaintext[i:i+2]
            if len(pair) == 1:
                pair += "X"
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            if row1 == row2:
                encrypted_text += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
            elif col1 == col2:
                encrypted_text += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
        return encrypted_text
    
    def playfair_decrypt(self, matrix, ciphertext):
        ciphertext = ciphertext.upper()
        decrypted_text = ""
        decrypted_text1 = ""
        
        for i in range(0, len(ciphertext), 2):
            pair = ciphertext[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            
            if row1 == row2:
                decrypted_text += matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5]
            elif col1 == col2:
                decrypted_text += matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]
            
            banro = ""
            
            i = 0
        while i < len(decrypted_text):
            if i < len(decrypted_text) - 1 and decrypted_text[i+1] == 'X' and (i+2 >= len(decrypted_text) or decrypted_text[i] == decrypted_text[i+2]):
                banro += decrypted_text[i]
                i += 2  # Bỏ qua 'X' chèn vào
            else:
                banro += decrypted_text[i]
                i += 1
        return banro
