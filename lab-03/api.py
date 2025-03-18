from flask import Flask, request, jsonify
from cipher.rsa import RSACipher
from cipher.ecc import ECCCipher

app = Flask(__name__)

rsa_cipher = RSACipher()
ecc_cipher = ECCCipher()

@app.route("/api/rsa/generate_keys", methods=["GET"])
def generate_keys():
    rsa_cipher.generate_keys()
    return jsonify({'message': 'Keys generated successfully'})

@app.route("/api/rsa/encrypt", methods=["POST"])
def rsa_encrypt():
    data = request.json
    message = data['message']
    key_type = data['key_type']
    private_key, public_key = rsa_cipher.load_keys()
    key = public_key if key_type == 'public' else private_key if key_type == 'private' else None
    if key is None:
        return jsonify({'message': 'Invalid key type'})
    encrypted_message = rsa_cipher.encrypt(message, key).hex()
    return jsonify({'encrypted_message': encrypted_message})

@app.route("/api/rsa/decrypt", methods=["POST"])
def rsa_decrypt():
    data = request.json
    ciphertext_hex = data['ciphertext']
    key_type = data['key_type']
    private_key, public_key = rsa_cipher.load_keys()
    key = public_key if key_type == 'public' else private_key if key_type == 'private' else None
    if key is None:
        return jsonify({'message': 'Invalid key type'})
    ciphertext = bytes.fromhex(ciphertext_hex)
    decrypted_message = rsa_cipher.decrypt(ciphertext, key)
    return jsonify({'decrypted_message': decrypted_message})

@app.route("/api/rsa/sign", methods=["POST"])
def rsa_sign():
    data = request.json
    message = data['message']
    private_key, _ = rsa_cipher.load_keys()
    signature = rsa_cipher.sign(message, private_key).hex()
    return jsonify({'signature': signature})

@app.route("/api/rsa/verify", methods=["POST"])
def rsa_verify():
    data = request.json
    message = data['message']
    signature_hex = data['signature']
    public_key, _ = rsa_cipher.load_keys()
    signature = bytes.fromhex(signature_hex)
    is_verified = rsa_cipher.verify(message, signature, public_key)
    return jsonify({'is_verified': is_verified})

@app.route("/api/ecc/generate_keys", methods=["GET"])
def ecc_generate_keys():
    ecc_cipher.generate_keys()
    return jsonify({'message': 'Keys generated successfully'})

@app.route("/api/ecc/sign", methods=["POST"])
def ecc_sign():
    data = request.json
    message = data['message']
    private_key, _ = ecc_cipher.load_keys()
    signature = ecc_cipher.sign(message, private_key).hex()
    return jsonify({'signature': signature})

@app.route("/api/ecc/verify", methods=["POST"])
def ecc_verify():
    data = request.json
    message = data['message']
    signature_hex = data['signature']
    public_key, _ = ecc_cipher.load_keys()
    signature = bytes.fromhex(signature_hex)
    is_verified = ecc_cipher.verify(message, signature, public_key)
    return jsonify({'is_verified': is_verified})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)