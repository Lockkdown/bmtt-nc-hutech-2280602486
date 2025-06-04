import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from urllib3 import response
from ui.rsa import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.GenerateKeys.clicked.connect(self.call_api_gen_keys)
        self.ui.Encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.Decrypt.clicked.connect(self.call_decrypt)
        self.ui.Sign.clicked.connect(self.call_api_sign)
        self.ui.Verify.clicked.connect(self.call_api_verify)
        
    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"
        try: 
            response = requests.get(url)
            if response.status_code == 200:
                QMessageBox.information(self, "Success", "Keys generated successfully")
            else:
                QMessageBox.warning(self, "Error", "Failed to generate keys")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
    
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        try:
            message = self.ui.PlainText.toPlainText()
            if not message:
                QMessageBox.warning(self, "Warning", "Please enter a message to encrypt")
                return
            
            data = {
                "message": message,
                "key_type": "public"
            }
            response = requests.post(url, json=data)
            if response.status_code == 200:
                encrypted_message = response.json().get("encrypted_message")
                self.ui.CipherText.setPlainText(encrypted_message)
            else:
                QMessageBox.warning(self, "Error", "Failed to encrypt message")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
    
    def call_decrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        try:
            ciphertext = self.ui.CipherText.toPlainText()
            if not ciphertext:
                QMessageBox.warning(self, "Warning", "Please enter a ciphertext to decrypt")
                return
            
            data = {
                "ciphertext": ciphertext,
                "key_type": "private"
            }
            response = requests.post(url, json=data)
            if response.status_code == 200:
                decrypted_message = response.json().get("decrypted_message")
                self.ui.PlainText.setPlainText(decrypted_message)
            else:
                QMessageBox.warning(self, "Error", "Failed to decrypt message")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
    
    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"
        try:
            message = self.ui.Information.toPlainText()
            if not message:
                QMessageBox.warning(self, "Warning", "Please enter information to sign")
                return
            
            data = {
                "message": message
            }
            response = requests.post(url, json=data)
            if response.status_code == 200:
                signature = response.json().get("signature")
                self.ui.Signature.setPlainText(signature)
            else:
                QMessageBox.warning(self, "Error", "Failed to sign message")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
    
    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/rsa/verify"
        try:
            message = self.ui.Information.toPlainText()
            signature = self.ui.Signature.toPlainText()
            if not message or not signature:
                QMessageBox.warning(self, "Warning", "Please enter both information and signature to verify")
                return
            
            data = {
                "message": message,
                "signature": signature
            }
            response = requests.post(url, json=data)
            if response.status_code == 200:
                is_verified = response.json().get("is_verified")
                if is_verified:
                    QMessageBox.information(self, "Success", "Signature verified successfully")
                else:
                    QMessageBox.warning(self, "Warning", "Signature verification failed")
            else:
                QMessageBox.warning(self, "Error", "Failed to verify signature")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())