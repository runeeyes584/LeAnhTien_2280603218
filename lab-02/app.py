from flask import Flask, render_template, request, json
from cipher.caesar import caesarCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar_cipher():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = caesarCipher()
    encrypted_message = Caesar.encrypt_text(text, key)
    return f"text: {text} <br/> key: {key} <br/> encrypted_message: {encrypted_message}"

@app.route("/decrypt", methods=['POST'])
def decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = caesarCipher()
    decrypted_message = Caesar.decrypt_text(text, key)
    return f"text: {text} <br/> key: {key} <br/> decrypted_message: {decrypted_message}"

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= 5050, debug=True)