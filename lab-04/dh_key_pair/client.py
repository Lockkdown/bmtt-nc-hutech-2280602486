from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import os

def generate_client_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def derive_shared_secret(private_key, server_public_key):
    shared_key = private_key.exchange(server_public_key)
    return shared_key

def main():
    try:
        # Lấy đường dẫn của thư mục hiện tại
        current_dir = os.path.dirname(os.path.abspath(__file__))
        key_file_path = os.path.join(current_dir, "server_public_key.pem")
        
        print("Đang đọc khóa công khai của server...")
        try:
            with open(key_file_path, "rb") as f: 
                server_public_key = serialization.load_pem_public_key(f.read())
            print(f"Đã đọc khóa công khai của server từ {key_file_path}")
        except FileNotFoundError:
            print(f"Không tìm thấy file {key_file_path}. Hãy chạy server.py trước.")
            return
        except Exception as e:
            print(f"Lỗi khi đọc khóa công khai của server: {e}")
            return
            
        print("Đang tạo tham số và cặp khóa...")
        try:
            parameters = server_public_key.parameters()
            private_key, public_key = generate_client_key_pair(parameters)
            print("Đã tạo cặp khóa, đang tính toán khóa chung...")
        except Exception as e:
            print(f"Lỗi khi tạo tham số và cặp khóa: {e}")
            return
        
        try:
            shared_secret = derive_shared_secret(private_key, server_public_key)
            print("Đã tính toán khóa chung thành công")
            print("Shared Secret: ", shared_secret.hex())
        except Exception as e:
            print(f"Lỗi khi tính toán khóa chung: {e}")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
    
if __name__ == "__main__":
    main()