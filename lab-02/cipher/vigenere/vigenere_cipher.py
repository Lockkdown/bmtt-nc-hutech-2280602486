class VigenereCipher:
    def __init__(self):
        pass # Phương thức khởi tạo không làm gì cả

    def vigenere_encrypt(self, plain_text, key):
        encrypted_text = ""
        key_index = 0
        for char in plain_text:
            if char.isalpha(): # Chỉ xử lý các ký tự là chữ cái
                # Xác định độ dịch chuyển dựa trên ký tự hiện tại của khóa
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')
                if char.isupper():
                    # Mã hóa chữ hoa
                    encrypted_text += chr(((ord(char) - ord('A') + key_shift) % 26) + ord('A'))
                else:
                    # Mã hóa chữ thường
                    encrypted_text += chr(((ord(char) - ord('a') + key_shift) % 26) + ord('a'))
                key_index += 1 # Chuyển sang ký tự tiếp theo của khóa
            else:
                # Giữ nguyên các ký tự không phải là chữ cái
                encrypted_text += char
        return encrypted_text

    def vigenere_decrypt(self, encrypted_text, key):
        decrypted_text = ""
        key_index = 0
        for char in encrypted_text:
            if char.isalpha(): # Chỉ xử lý các ký tự là chữ cái
                # Xác định độ dịch chuyển dựa trên ký tự hiện tại của khóa
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')
                if char.isupper():
                    # Giải mã chữ hoa
                    decrypted_text += chr(((ord(char) - ord('A') - key_shift + 26) % 26) + ord('A'))
                else:
                    # Giải mã chữ thường
                    decrypted_text += chr(((ord(char) - ord('a') - key_shift + 26) % 26) + ord('a'))
                key_index += 1 # Chuyển sang ký tự tiếp theo của khóa
            else:
                # Giữ nguyên các ký tự không phải là chữ cái
                decrypted_text += char
        return decrypted_text
