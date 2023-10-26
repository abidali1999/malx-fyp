from PyQt5 import QtCore, QtGui, QtWidgets
import hashlib
from PyQt5.QtWidgets import QMessageBox
from qrc import source_rc
import requests



class Ui_signupwindow(QtWidgets.QWidget):
    def __init__(self,parent):
        super().__init__()
        self.main_window=parent
        self.setupUi()

    def show_message(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()

    def showlogin(self):
        self.main_window.showlogin()

    def signup(self):
        first_name = self.Emailfield.text()
        email = self.Emailfield_2.text()
        last_name = self.Emailfield_3.text()
        password = self.Emailfield_4.text()
        confirm_password = self.Emailfield_5.text()
        phone = self.Emailfield_6.text()
        name=first_name+' '+last_name
        if password != confirm_password:
            self.show_message("Password mismatch", "Passwords do not match.")
            return
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        api_url = 'https://abidali1999063.pythonanywhere.com/signup_api'  # Replace with your actual API URL
        data = {
            'name': name,
            'email': email,
            'password': password_hash,
            'phone': phone
        }
        response = requests.post(api_url, data=data)
        print(response.status_code)
        print(response.text)
        if response.status_code == 201:
            self.show_message("Sign Up Successful", "You have successfully signed up.")
            self.main_window.showlogin()
        else: self.show_message("Sign Up Error", response.text)

    def setupUi(self):
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 70, 151, 121))
        self.label.setStyleSheet("image:url(:/newPrefix/images/Malx logo.png);\n""text-align:center;\n""margin:0px auto;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.Emailfield = QtWidgets.QLineEdit(self.centralwidget)
        self.Emailfield.setGeometry(QtCore.QRect(130, 230, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Emailfield.setFont(font)
        self.Emailfield.setStyleSheet("border:1px solid black;\n""padding:10px;")
        self.Emailfield.setText("")
        self.Emailfield.setObjectName("Emailfield")
        self.Emailfield_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Emailfield_2.setGeometry(QtCore.QRect(130, 300, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Emailfield_2.setFont(font)
        self.Emailfield_2.setStyleSheet("border:1px solid black;\n""padding:10px;")
        self.Emailfield_2.setText("")
        self.Emailfield_2.setObjectName("Emailfield_2")
        self.Emailfield_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.Emailfield_3.setGeometry(QtCore.QRect(451, 230, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Emailfield_3.setFont(font)
        self.Emailfield_3.setStyleSheet("border:1px solid black;\n""padding:10px;")
        self.Emailfield_3.setText("")
        self.Emailfield_3.setObjectName("Emailfield_3")
        self.Emailfield_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.Emailfield_4.setGeometry(QtCore.QRect(450, 300, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Emailfield_4.setFont(font)
        self.Emailfield_4.setStyleSheet("border:1px solid black;\n""padding:10px")
        self.Emailfield_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Emailfield_4.setObjectName("Emailfield_4")
        self.Emailfield_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.Emailfield_5.setGeometry(QtCore.QRect(130, 370, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Emailfield_5.setFont(font)
        self.Emailfield_5.setStyleSheet("border:1px solid black;\n""padding:10px;")
        self.Emailfield_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Emailfield_5.setObjectName("Emailfield_5")
        self.Emailfield_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.Emailfield_6.setGeometry(QtCore.QRect(450, 370, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Emailfield_6.setFont(font)
        self.Emailfield_6.setStyleSheet("border:1px solid black;\n""padding:10px;")
        self.Emailfield_6.setObjectName("Emailfield_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 440, 151, 41))
        self.pushButton.setStyleSheet("background:black;\n""color:#fff;\n""border:1px solid black;\n""font-weight:bold;\n""font-size:14px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.showlogin)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.clicked.connect(self.signup)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 440, 121, 41))
        self.pushButton_2.setStyleSheet("background:white;\n""color:#00000;\n""border:1px solid black;\n""font-weight:bold;\n""font-size:14px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, signupwindow):
        _translate = QtCore.QCoreApplication.translate
        signupwindow.setWindowTitle(_translate("signupwindow", "MainWindow"))
        self.Emailfield.setPlaceholderText(_translate("signupwindow", "First Name"))
        self.Emailfield_2.setPlaceholderText(_translate("signupwindow", "Email"))
        self.Emailfield_3.setPlaceholderText(_translate("signupwindow", "Last Name"))
        self.Emailfield_4.setPlaceholderText(_translate("signupwindow", "Password"))
        self.Emailfield_5.setPlaceholderText(_translate("signupwindow", "Confirm Password"))
        self.Emailfield_6.setPlaceholderText(_translate("signupwindow", "Phone"))
        self.pushButton.setText(_translate("signupwindow", "BACK TO LOGIN"))
        self.pushButton_2.setText(_translate("signupwindow", "SIGN UP"))
