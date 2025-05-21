from flask import Flask, request, jsonify
# Giả sử api.py nằm ở your_project_root/
from caesar.caesar_cipher import CaesarCipher

app = Flask(__name__)

# CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key) # Bây giờ sẽ gọi đúng phương thức của đối tượng
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key) # Bây giờ sẽ gọi đúng phương thức của đối tượng
    return jsonify({'decrypted_message': decrypted_text})

# main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)