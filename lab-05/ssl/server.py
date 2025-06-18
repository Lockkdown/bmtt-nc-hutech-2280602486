import socket
import ssl 
import threading
import os

server_address = ('localhost', 2486)
clients = []

def handle_client(client_socket):
    clients.append(client_socket)
    print("Da ket noi voi:", client_socket.getpeername())
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print("Nhan:", data.decode('utf-8'))
            
            for client in clients:
                if client != client_socket:
                    try:
                        client.send(data)
                    except Exception as e:
                        print(f"Loi gui tin nhan: {str(e)}")
                        clients.remove(client)
    except Exception as e:
        print(f"Loi xu ly client: {str(e)}")
        clients.remove(client_socket)
    finally:
        print("Da ngat ket noi:", client_socket.getpeername())
        clients.remove(client_socket)
        client_socket.close()

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(5)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    cert_dir = os.path.join(current_dir, 'certificates')
    cert_path = os.path.join(cert_dir, 'server-cert.crt')
    key_path = os.path.join(cert_dir, 'server-key.key')

    # Tạo thư mục chứng chỉ nếu chưa tồn tại
    if not os.path.exists(cert_dir):
        os.makedirs(cert_dir)
        print(f"Da tao thu muc chung chi: {cert_dir}")

    # Kiểm tra sự tồn tại của các file chứng chỉ
    if not os.path.exists(cert_path) or not os.path.exists(key_path):
        raise FileNotFoundError(f"Khong tim thay file chung chi hoac key tai:\n{cert_path}\n{key_path}")

    print("Server dang cho ket noi...")
    while True:
        client_socket, client_address = server_socket.accept()
        
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.verify_mode = ssl.CERT_NONE  # Tắt xác thực client
        context.load_cert_chain(certfile=cert_path, keyfile=key_path)
        
        ssl_socket = context.wrap_socket(client_socket, server_side=True)

        client_thread = threading.Thread(target=handle_client, args=(ssl_socket,))
        client_thread.start()
except FileNotFoundError as e:
    print(f"Loi: {str(e)}")
    print("Hay dam bao cac file chung chi da duoc tao dung vi tri.")
except Exception as e:
    print(f"Loi server: {str(e)}")
finally:
    server_socket.close()