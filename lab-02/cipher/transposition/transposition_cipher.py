class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encryptedtext = ""
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encryptedtext += text[pointer]
                pointer += key
        return encryptedtext

    def decrypt(self, text, key):
        num_rows = (len(text) + key - 1) // key  # Số hàng cần thiết
        num_cols = key  # Số cột chính là key
        num_shaded = (num_rows * num_cols) - len(text)  # Ô trống ở hàng cuối

        decryptedtext = [''] * num_rows
        row, col = 0, 0

        for symbol in text:
            decryptedtext[row] += symbol
            row += 1
            if row == num_rows or (row == num_rows - 1 and col >= num_cols - num_shaded):
                row = 0
                col += 1

        return ''.join(decryptedtext)