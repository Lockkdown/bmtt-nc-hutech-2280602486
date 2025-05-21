
class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key): # key ở đây là số cột
        encrypted_text = ""
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key): # text ở đây là cipher_text, key là số cột
        decrypted_text = [""] * key # Tạo ra 'key' (số cột) chuỗi rỗng
        row, col = 0, 0
        for symbol in text: # Duyệt qua các ký tự của văn bản đã mã hóa
            decrypted_text[col] += symbol # Nối ký tự vào cột hiện tại
            col += 1
            if col == key or (col == key - 1 and row >= len(text) % key):
                col = 0
                row += 1
        return "".join(decrypted_text) # Nối các cột lại -> sẽ không ra văn bản gốc