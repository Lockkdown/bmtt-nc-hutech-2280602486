# Sử dụng thư viện pycryptodomex đã cài đặt
from Cryptodome.Cipher import AES, PKCS1_OAEP
from Cryptodome.PublicKey import RSA 
from Cryptodome.Random import get_random_bytes 
from Cryptodome.Util.Padding import pad, unpad 
import socket 
import threading 
import hashlib 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 2486)) # Sử dụng cổng giống với client
server_socket.listen(5)

print("Đang tạo khóa RSA 2048-bit, vui lòng đợi...")
server_key = RSA.generate(2048)
print("Đã tạo xong khóa RSA, server sẵn sàng kết nối!")

clients = []

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

def handle_client(client_socket, client_address): 
    print(f"Connected with {client_address}")
    
    try:
        client_socket.send(server_key.publickey().export_key(format='PEM'))
        print(f"Đã gửi khóa công khai đến {client_address}")
    except Exception as e:
        print(f"Lỗi khi gửi khóa công khai đến {client_address}: {e}")
        client_socket.close()
        return
    
    try:
        client_key_data = client_socket.recv(2048)
        if not client_key_data:
            print(f"Không nhận được khóa công khai từ {client_address}")
            client_socket.close()
            return
        client_received_key = RSA.import_key(client_key_data)
        print(f"Đã nhận khóa công khai từ {client_address}")
    except Exception as e:
        print(f"Lỗi khi nhận khóa công khai từ {client_address}: {e}")
        client_socket.close()
        return
    
    aes_key = get_random_bytes(16)
    
    try:
        cipher_rsa = PKCS1_OAEP.new(client_received_key)
        encrypted_aes_key = cipher_rsa.encrypt(aes_key)
        client_socket.send(encrypted_aes_key)
        print(f"Đã gửi khóa AES đã mã hóa đến {client_address}")
    except Exception as e:
        print(f"Lỗi khi gửi khóa AES đến {client_address}: {e}")
        client_socket.close()
        return
    
    clients.append((client_socket, aes_key))
    
    while True: 
        try:
            encrypted_data = client_socket.recv(1024) 
            if not encrypted_data:
                break
            message_text = decrypt_message(aes_key, encrypted_data)
            print(f"Received from {client_address}: {message_text}")
            
            for client, key in clients: 
                if client != client_socket: 
                    try:
                        encrypted = encrypt_message(key, message_text)
                        client.send(encrypted)
                    except Exception as e:
                        print(f"Lỗi khi gửi tin nhắn đến client khác: {e}")
                        continue
            if message_text == "exit":
                break
        except Exception as e:
            print(f"Lỗi khi nhận hoặc xử lý tin nhắn từ {client_address}: {e}")
            break
    clients.remove((client_socket, aes_key))
    client_socket.close()
    print(f"Connection with {client_address} closed")
    
while True: 
    try:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()
    except KeyboardInterrupt:
        print("\nServer đang dừng...")
        break
    except Exception as e:
        print(f"Lỗi khi chấp nhận kết nối: {e}")
        continue
    
    