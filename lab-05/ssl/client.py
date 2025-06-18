import socket
import ssl 
import threading
import os

server_address = ('localhost', 2486)
ssl_socket = None

def receive_data(ssl_socket):
    try:
        while True:
            data = ssl_socket.recv(1024)
            if not data: 
                break
            print("Nhan:", data.decode('utf-8'))
    except Exception as e:
        print(f"Loi nhan du lieu: {str(e)}")
    finally:
        if ssl_socket:
            ssl_socket.close()
        print("Ket noi da dong.")

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    cert_path = os.path.join(current_dir, 'certificates', 'server-cert.crt')

    if not os.path.exists(cert_path):
        raise FileNotFoundError(f"Khong tim thay file chung chi tai: {cert_path}")

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.check_hostname = False  # Tắt kiểm tra hostname
    context.verify_mode = ssl.CERT_NONE  # Tắt xác thực chứng chỉ

    ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')
    print("Dang ket noi toi server...")
    ssl_socket.connect(server_address)
    print("Da ket noi thanh cong!")

    receive_thread = threading.Thread(target=receive_data, args=(ssl_socket,))
    receive_thread.start()

    while True:
        message = input("Nhap tin nhan: ")
        if message.lower() == 'quit':
            break
        ssl_socket.send(message.encode('utf-8'))

except FileNotFoundError as e:
    print(f"Loi: {str(e)}")
except Exception as e:
    print(f"Loi ket noi: {str(e)}")
except KeyboardInterrupt:
    print("\nDung chuong trinh...")
finally: 
    if ssl_socket:
        ssl_socket.close()