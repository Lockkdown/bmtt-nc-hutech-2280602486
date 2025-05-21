from flask import Flask, request, jsonify
# Giả sử api.py nằm ở your_project_root/
from caesar.caesar_cipher import CaesarCipher
from cipher.vigenere import VigenereCipher

app = Flask(__name__)

# CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
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

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt(): # Đổi tên hàm để tránh trùng lặp nếu có
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt(): # Đổi tên hàm để tránh trùng lặp nếu có
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})


# main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)