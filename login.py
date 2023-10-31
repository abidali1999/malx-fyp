from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QLineEdit,QMessageBox,QApplication
from PyQt5.QtGui import QFont
from qrc import source_rc
import requests
from my_header import HeaderWidget


class Ui_loginwindow(QtWidgets.QWidget):
    def __init__(self,parent):
        super().__init__()
        self.main_window=parent
        self.setupUi()

    def opensignup(self):
        self.main_window.showsignup()

    def openwindow(self):
        email = self.Emailfield.text()
        password = self.Emailfield_2.text()
        print(email,password)
        api_url = 'https://abidali1999063.pythonanywhere.com/login_api'  # Replace with your actual API URL
        data = {
            'email': email,
            'password': password
        }
        response = requests.post(api_url, json=data)
        # print(response.status_code,response.text)
        # self.main_window.showDashboard()
        if response.status_code == 200: 
            self.main_window.isloggedin=True
            self.main_window.showDashboard()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Authentication failed. Please check your credentials.")
            msg.setWindowTitle("Login Error")
            msg.exec_()

    def setupUi(self):
        self.centralwidget = QWidget(self)
        self.resize(1096, 900)
        self.header=HeaderWidget(self.main_window,self.centralwidget)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(440, 400, 121, 41)
        self.pushButton_2.setStyleSheet("background-color: white;\n""color: black;\n""border: 1px solid black;\n""font-weight: bold;\n""font-size: 14px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.opensignup)
        # self.label = QtWidgets.QLabel(self.centralwidget)
        # self.label.setGeometry(QtCore.QRect(340, 70, 151, 121))
        # self.label.setStyleSheet("image:url(:/newPrefix/images/Malx logo.png);\n""text-align:center;\n""margin:0px auto;")
        # self.label.setText("")
        # self.label.setObjectName("label")
        self.Emailfield_2 = QLineEdit(self.centralwidget)
        self.Emailfield_2.setGeometry(240, 320, 321, 41)
        font = QFont()
        font.setPointSize(11)
        self.Emailfield_2.setFont(font)
        self.Emailfield_2.setStyleSheet("border: 1px solid black;")
        self.Emailfield_2.setEchoMode(QLineEdit.Password)
        self.Emailfield_2.setObjectName("Emailfield_2")
        self.Emailfield = QLineEdit(self.centralwidget)
        self.Emailfield.setGeometry(240, 240, 321, 41)
        self.Emailfield.setFont(font)
        self.Emailfield.setStyleSheet("border: 1px solid black;")
        self.Emailfield.setObjectName("Emailfield")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setGeometry(240, 450, 121, 21)
        self.label_2.setStyleSheet("font-size: 15px;")
        self.label_2.setObjectName("label_2")
        self.loginbtn = QPushButton(self.centralwidget)
        self.loginbtn.setGeometry(240, 400, 121, 41)
        self.loginbtn.setStyleSheet("background-color: black;\n""color: white;\n""border: 1px solid black;\n""font-weight: bold;\n""font-size: 14px;")
        self.loginbtn.setObjectName("loginbtn")
        self.loginbtn.clicked.connect(self.openwindow)
        self.retranslateUi(self)

    def retranslateUi(self, loginwindow):
        _translate = QtCore.QCoreApplication.translate        
        loginwindow.setWindowTitle(_translate("loginwindow", "MainWindow"))
        self.pushButton_2.setText(_translate("loginwindow", "SIGN UP"))
        self.Emailfield_2.setPlaceholderText(_translate("loginwindow", "Enter Password"))
        self.Emailfield.setPlaceholderText(_translate("loginwindow", "Enter Email"))
        self.label_2.setText(_translate("loginwindow", "Forgot Password"))
        self.loginbtn.setText(_translate("loginwindow", "LOGIN"))


if __name__=='__main__':
    import sys
    app = QApplication(sys.argv)
    window = Ui_loginwindow(app)
    window.show()
    sys.exit(app.exec_())

