import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_CaesarCipher
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CaesarCipher()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
    
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        plain_text = self.ui.plaintext.toPlainText().strip()
        key = self.ui.key.toPlainText().strip()
        if not plain_text:
            QMessageBox.warning(self, "Error", "Plaintext is empty!")
            return
        if not key:
            QMessageBox.warning(self, "Error", "Key is empty!")
            return

        payload = {"plain_text": plain_text, "key": key}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.ciphertext.setText(data.get("encrypted_message", ""))
                QMessageBox.information(self, "Success", "Encrypted Successfully!")
            else:
                QMessageBox.warning(self, "Error", f"API error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Request Error", str(e))

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        cipher_text = self.ui.ciphertext.toPlainText().strip()
        key = self.ui.key.toPlainText().strip()


        if not cipher_text:
            QMessageBox.warning(self, "Error", "Ciphertext is empty!")
            return
        if not key:
            QMessageBox.warning(self, "Error", "Key is empty!")
            return

        payload = {"cipher_text": cipher_text, "key": key}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.plaintext.setText(data.get("decrypted_message", ""))
                QMessageBox.information(self, "Success", "Decrypted Successfully!")
            else:
                QMessageBox.warning(self, "Error", f"API error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Request Error", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
