import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.ecc import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_5.clicked.connect(self.call_api_gen_keys)
        self.ui.pushButton_3.clicked.connect(self.call_api_sign)
        self.ui.pushButton_4.clicked.connect(self.call_api_verify)

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/ecc/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(data.get("message", "Keys generated successfully"))
                msg.exec_()
            else:
                print(f"Error while calling API: Status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/ecc/sign"
        payload = {
            "message": self.ui.plainTextEdit_3.toPlainText(),
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.plainTextEdit_4.setPlainText(data.get("signature", ""))

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Signed Successfully")
                msg.exec_()
            else:
                print(f"Error while calling API: Status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/ecc/verify"
        payload = {
            "message": self.ui.plainTextEdit_3.toPlainText(),
            "signature": self.ui.plainTextEdit_4.toPlainText()
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                try:
                    data = response.json()
                    if "is_verified" in data:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information if data["is_verified"] else QMessageBox.Warning)
                        msg.setText("Signature verified successfully" if data["is_verified"] else "Signature verification failed")
                        msg.exec_()
                    else:
                        print("Error: 'is_verified' key not found in API response")
                        print(f"API response: {data}")
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("Verification failed: Invalid API response")
                        msg.exec_()
                except ValueError:
                    print("Error: API did not return valid JSON")
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Verification failed: Invalid API response format")
                    msg.exec_()
            else:
                print(f"Error while calling API: Status code {response.status_code}")
                print(f"API response: {response.text}")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText(f"Verification failed: Server returned status {response.status_code}")
                msg.exec_()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Verification failed: Unable to connect to server")
            msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())