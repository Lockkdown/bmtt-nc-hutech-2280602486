class RailFenceCipher:
    def __init__(self):
        pass


    def rail_fence_encrypt(self, plain_text: str, num_rails: int) -> str:
        if num_rails <= 1: # Xử lý trường hợp num_rails không hợp lệ
            return plain_text

        rails = ["" for _ in range(num_rails)] # Sử dụng chuỗi thay vì list char để dễ join
        rail_index = 0
        direction = 1  # 1 for down, -1 for up

        for char in plain_text:
            rails[rail_index] += char # Thêm ký tự vào rail hiện tại
            
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            
            rail_index += direction

        cipher_text = "".join(rails) # Nối các rail lại
        return cipher_text


    def rail_fence_decrypt(self, cipher_text: str, num_rails: int) -> str:
        if num_rails <= 1: # Xử lý trường hợp num_rails không hợp lệ
            return cipher_text

        # 1. Tính toán độ dài của mỗi "rail"
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1
        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        # 2. Xây dựng lại các "rail" từ cipher_text
        rails_content = []
        current_pos = 0
        for length in rail_lengths:
            rails_content.append(list(cipher_text[current_pos : current_pos + length])) # Chuyển thành list để pop
            current_pos += length
        
        # 3. Đọc lại plain_text từ các "rail"
        plain_text = []
        rail_index = 0
        direction = 1
        for _ in range(len(cipher_text)):
            plain_text.append(rails_content[rail_index].pop(0)) # Lấy ký tự đầu tiên của rail hiện tại
            
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
            
        return "".join(plain_text)