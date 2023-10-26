from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QLineEdit, QMessageBox, QApplication, QVBoxLayout
from PyQt5.QtGui import QFont
import requests
from my_header import HeaderWidget

class Ui_loginwindow(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.main_window = parent
        self.setupUi()

    def opensignup(self):
        self.main_window.showsignup()

    def openwindow(self):
        email = self.Emailfield.text()
        password = self.Emailfield_2.text()
        print(email, password)
        api_url = 'https://abidali1999063.pythonanywhere.com/login_api'
        data = {
            'email': email,
            'password': password
        }
        response = requests.post(api_url, json=data)
        if response.status_code == 200:
            self.main_window.isloggedin = True
            self.main_window.showDashboard()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Authentication failed. Please check your credentials.")
            msg.setWindowTitle("Login Error")
            msg.exec_()

    def setupUi(self):
        self.centralwidget = QWidget(self)
        self.setWindowTitle("Login Window")
        self.resize(600, 400)

        self.layout = QVBoxLayout(self)

        self.header = HeaderWidget(self.main_window, self.centralwidget)
        self.layout.addWidget(self.header)

        self.formLayout = QVBoxLayout()

        self.Emailfield = QLineEdit(self)
        self.Emailfield.setPlaceholderText("Enter Email")
        self.Emailfield.setMinimumHeight(40)  # Increase the height
        self.formLayout.addWidget(self.Emailfield)

        self.Emailfield_2 = QLineEdit(self)
        self.Emailfield_2.setPlaceholderText("Enter Password")
        self.Emailfield_2.setEchoMode(QLineEdit.Password)
        self.Emailfield_2.setMinimumHeight(40)  # Increase the height
        self.formLayout.addWidget(self.Emailfield_2)

        self.loginbtn = QPushButton("LOGIN", self)
        self.loginbtn.setStyleSheet("background-color: black; color: white; font-weight: bold; font-size: 14px;")
        self.loginbtn.setMinimumHeight(40)  # Increase the height
        self.loginbtn.clicked.connect(self.openwindow)
        self.formLayout.addWidget(self.loginbtn)

        self.signupbtn = QPushButton("SIGN UP", self)
        self.signupbtn.setStyleSheet("background-color: white; color: black; border: 1px solid black; font-weight: bold; font-size: 14px;")
        self.signupbtn.setMinimumHeight(40)  # Increase the height
        self.signupbtn.clicked.connect(self.opensignup)
        self.formLayout.addWidget(self.signupbtn)

        self.forgotPasswordLabel = QLabel("Forgot Password", self)
        self.forgotPasswordLabel.setStyleSheet("font-size: 15px;")
        self.formLayout.addWidget(self.forgotPasswordLabel)

        self.layout.addLayout(self.formLayout)

    def resizeEvent(self, event):
        # Adjust widget sizes when the window is resized
        self.header.resize(self.width(), self.header.height())

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Ui_loginwindow(app)
    window.show()
    sys.exit(app.exec_())
