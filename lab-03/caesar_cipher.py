import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow  # Import from caesar.py (not ui.caesar)
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Connect buttons to methods (using correct button names from caesar.py)
        self.ui.pushButton.clicked.connect(self.call_api_encrypt)
        self.ui.pushButton_2.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        # Get inputs
        plain_text = self.ui.plainTextEdit.toPlainText()
        key = self.ui.lineEdit.text()

        # Basic input validation
        if not plain_text:
            QMessageBox.warning(self, "Input Error", "Plain text cannot be empty!")
            return
        if not key.isdigit():
            QMessageBox.warning(self, "Input Error", "Key must be a valid integer!")
            return

        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": plain_text,
            "key": key
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit.setPlainText(data["encrypted_message"])
                QMessageBox.information(self, "Success", "Encrypted Successfully")
            else:
                QMessageBox.critical(self, "API Error", f"Error while calling API: Status {response.status_code}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Request failed: {str(e)}")

    def call_api_decrypt(self):
        # Get inputs
        cipher_text = self.ui.textEdit.toPlainText()
        key = self.ui.lineEdit.text()

        # Basic input validation
        if not cipher_text:
            QMessageBox.warning(self, "Input Error", "Cipher text cannot be empty!")
            return
        if not key.isdigit():
            QMessageBox.warning(self, "Input Error", "Key must be a valid integer!")
            return

        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": cipher_text,
            "key": key
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.plainTextEdit.setPlainText(data["decrypted_message"])
                QMessageBox.information(self, "Success", "Decrypted Successfully")
            else:
                QMessageBox.critical(self, "API Error", f"Error while calling API: Status {response.status_code}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Request failed: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())