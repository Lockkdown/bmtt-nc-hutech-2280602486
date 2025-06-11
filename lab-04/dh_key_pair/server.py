from inspect import Parameter
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
import os

def generate_dh_parameters():
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    return parameters

def generate_server_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def main():
    try:
        # Lấy đường dẫn của thư mục hiện tại
        current_dir = os.path.dirname(os.path.abspath(__file__))
        key_file_path = os.path.join(current_dir, "server_public_key.pem")
        
        print("Đang tạo tham số DH, vui lòng đợi...")
        parameters = generate_dh_parameters()
        print("Đã tạo tham số DH, đang tạo cặp khóa...")
        private_key, public_key = generate_server_key_pair(parameters)
        print("Đã tạo cặp khóa, đang lưu khóa công khai...")
        
        try:
            with open(key_file_path, "wb") as f: 
                f.write(public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                ))
            print(f"Đã lưu khóa công khai vào file {key_file_path}")
        except Exception as e:
            print(f"Lỗi khi lưu khóa công khai: {e}")
    except Exception as e:
        print(f"Lỗi khi tạo tham số DH hoặc cặp khóa: {e}")
        
if __name__ == "__main__":
    main()