# Sử dụng thư viện pycryptodomex đã cài đặt
from Cryptodome.Cipher import AES, PKCS1_OAEP
from Cryptodome.PublicKey import RSA 
from Cryptodome.Random import get_random_bytes 
from Cryptodome.Util.Padding import pad, unpad 
import socket 
import threading 
import hashlib 

print("Đang tạo khóa RSA 2048-bit, vui lòng đợi...")
client_key = RSA.generate(2048)
print("Đã tạo xong khóa RSA, đang kết nối đến server...")

# Khởi tạo socket và kết nối đến server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect(('localhost', 2486))
    print("Đã kết nối đến server!")
except ConnectionRefusedError:
    print("Không thể kết nối đến server. Hãy đảm bảo server đang chạy.")
    exit()
except Exception as e:
    print(f"Lỗi kết nối: {e}")
    exit()

# Nhận public key từ server
try:
    server_public_key_data = client_socket.recv(2048)
    if not server_public_key_data:
        print("Không nhận được khóa công khai từ server.")
        client_socket.close()
        exit()
    server_public_key = RSA.import_key(server_public_key_data)
    print("Đã nhận khóa công khai từ server.")
except Exception as e:
    print(f"Lỗi khi nhận khóa công khai từ server: {e}")
    client_socket.close()
    exit()

# Gửi public key của client đến server
try:
    client_socket.send(client_key.publickey().export_key(format='PEM'))
    print("Đã gửi khóa công khai đến server.")
except Exception as e:
    print(f"Lỗi khi gửi khóa công khai đến server: {e}")
    client_socket.close()
    exit()

# Nhận AES key đã được mã hóa từ server
try:
    encrypted_aes_key = client_socket.recv(2048)
    if not encrypted_aes_key:
        print("Không nhận được khóa AES từ server.")
        client_socket.close()
        exit()
    print("Đã nhận khóa AES đã mã hóa từ server.")
except Exception as e:
    print(f"Lỗi khi nhận khóa AES từ server: {e}")
    client_socket.close()
    exit()

# Giải mã AES key bằng private key của client
try:
    cipher_rsa = PKCS1_OAEP.new(client_key)
    aes_key = cipher_rsa.decrypt(encrypted_aes_key)
    print("Đã giải mã khóa AES thành công.")
except Exception as e:
    print(f"Lỗi khi giải mã khóa AES: {e}")
    client_socket.close()
    exit()

def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

def decrypt_message(key, encrypted_data):
    iv = encrypted_data[:AES.block_size]
    ciphertext = encrypted_data[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted.decode()

def receive_messages():
    while True:
        try:
            encrypted_data = client_socket.recv(1024)
            if not encrypted_data:
                break
            message_text = decrypt_message(aes_key, encrypted_data)
            print("Received:", message_text)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

# Khởi động thread nhận tin nhắn
receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()
    
# Vòng lặp chính để gửi tin nhắn
print("Connected to server. Start typing messages.")
while True: 
    try:
        message = input("Enter message ('exit' to quit): ")
        encrypted_data = encrypt_message(aes_key, message)
        client_socket.send(encrypted_data)
        if message == 'exit':
            break
    except Exception as e:
        print(f"Error sending message: {e}")
        break
        
client_socket.close()
    