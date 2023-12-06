from PyQt5 import QtCore, QtGui, QtWidgets
import hashlib
from PyQt5.QtWidgets import QMessageBox,QApplication,QInputDialog
from qrc import source_rc
import requests
from MyPushButton import PushButton


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

    def show_confirmation_dialog(self,useremail):
        code, ok_pressed = QInputDialog.getText(self, "Enter Confirmation Code", "Verification Code:")
        if ok_pressed:
            print(f"Entered Code: {code}")
            # try: email=self.main_window.userid
            # except: email='abidali1999063@gmail.com'
            
            api_url = 'https://abidali1999063.pythonanywhere.com/verify_email'  # Replace with your actual API URL
            data = {
                'code': code,
                'email': useremail,
            }
            response = requests.post(api_url, json=data)
            print(response.status_code)
            print(response.text)
            try: 
                if response.json()['status']=='success':
                    self.main_window.showDashboard()
            except: pass

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
        response = requests.post(api_url, json=data)
        print(response.status_code)
        print(response.text)
        if response.status_code == 200:
            # self.show_message("Sign Up Successful", "Please verify email.")
            # api_url = 'https://abidali1999063.pythonanywhere.com/signup_api'  # Replace with your actual API URL
            # data = {
            #     'name': name,
            #     'email': email,
            #     'password': password_hash,
            #     'phone': phone
            # }
            # response = requests.post(api_url, json=data)
            self.show_confirmation_dialog(email)
            # self.main_window.showlogin()
        else: self.show_message("Sign Up Error", response.text)

    def setupUi(self):
        self.resize(1096, 900)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 100, 200, 150))
        self.label.setStyleSheet("image:url(:/newPrefix/images/Malx logo.png);\n""text-align:center;\n""margin:0px auto;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.Emailfield = QtWidgets.QLineEdit(self.centralwidget)
        self.Emailfield.setGeometry(QtCore.QRect(280, 300, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Emailfield.setFont(font)
        self.Emailfield.setStyleSheet("border:1px solid black;\n""padding:10px;")
        self.Emailfield.setText("")
        self.Emailfield.setObjectName("Emailfield")
        self.Emailfield_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Emailfield_2.setGeometry(QtCore.QRect(280, 370, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Emailfield_2.setFont(font)
        self.Emailfield_2.setStyleSheet("border:1px solid black;\n""padding:10px;")
        self.Emailfield_2.setText("")
        self.Emailfield_2.setObjectName("Emailfield_2")
        self.Emailfield_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.Emailfield_3.setGeometry(QtCore.QRect(600, 300, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Emailfield_3.setFont(font)
        self.Emailfield_3.setStyleSheet("border:1px solid black;\n""padding:10px;")
        self.Emailfield_3.setText("")
        self.Emailfield_3.setObjectName("Emailfield_3")
        self.Emailfield_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.Emailfield_4.setGeometry(QtCore.QRect(600, 370, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Emailfield_4.setFont(font)
        self.Emailfield_4.setStyleSheet("border:1px solid black;\n""padding:10px")
        self.Emailfield_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Emailfield_4.setObjectName("Emailfield_4")
        self.Emailfield_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.Emailfield_5.setGeometry(QtCore.QRect(280, 440, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Emailfield_5.setFont(font)
        self.Emailfield_5.setStyleSheet("border:1px solid black;\n""padding:10px;")
        self.Emailfield_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Emailfield_5.setObjectName("Emailfield_5")
        self.Emailfield_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.Emailfield_6.setGeometry(QtCore.QRect(600, 440, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Emailfield_6.setFont(font)
        self.Emailfield_6.setStyleSheet("border:1px solid black;\n""padding:10px;")
        self.Emailfield_6.setObjectName("Emailfield_6")
        self.pushButton = PushButton(self.centralwidget,True,1)
        self.pushButton.setGeometry(QtCore.QRect(600, 510, 151, 41))
        self.pushButton.setStyleSheet("background:black;\n""color:#fff;\n""border:1px solid black;\n""font-weight:bold;\n""font-size:14px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.showlogin)
        self.pushButton_2 = PushButton(self.centralwidget,True,1)
        self.pushButton_2.clicked.connect(self.signup)
        
        self.pushButton_2.setGeometry(QtCore.QRect(400, 510, 121, 41))
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



if __name__=='__main__':
    import sys
    app = QApplication(sys.argv)
    window = Ui_signupwindow(app)
    window.show()
    sys.exit(app.exec_())

