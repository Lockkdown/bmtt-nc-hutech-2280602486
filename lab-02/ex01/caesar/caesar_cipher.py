from .alphabet import ALPHABET  # Đảm bảo bạn có file alphabet.py trong cùng thư mục caesar

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    # --- SỬA LỖI: Thụt đầu dòng các phương thức sau ---
    def encrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()  # Chuyển văn bản đầu vào thành chữ hoa
        encrypted_text = []
        for letter in text:
            try:
                letter_index = self.alphabet.index(letter)
                output_index = (letter_index + key) % alphabet_len
                output_letter = self.alphabet[output_index]
                encrypted_text.append(output_letter)
            except ValueError:  # Nếu ký tự không có trong alphabet, giữ nguyên nó
                encrypted_text.append(letter)
        return "".join(encrypted_text)

    def decrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        # text = text.upper() # Không cần thiết ở đây nếu encrypt đã là upper và alphabet là upper
        decrypted_text = []
        for letter in text:
            try:
                letter_index = self.alphabet.index(letter)
                output_index = (letter_index - key + alphabet_len) % alphabet_len # Thêm alphabet_len để đảm bảo kết quả luôn dương
                output_letter = self.alphabet[output_index]
                decrypted_text.append(output_letter)
            except ValueError:  # Nếu ký tự không có trong alphabet, giữ nguyên nó
                decrypted_text.append(letter)
        return "".join(decrypted_text)