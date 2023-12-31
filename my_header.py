# header_widget.py
from PyQt5.QtWidgets import QWidget, QLabel,QApplication,QFrame,QPushButton,QMessageBox
from PyQt5 import QtCore
from qrc import source_rc
from MyPushButton import PushButton
from PyQt5.QtCore import Qt


class HeaderWidget(QWidget):
    def __init__(self,main_window,parent_widget=None):
        super().__init__()
        self.main_wid=parent_widget
        self.main_window=main_window
        print(main_window)
        self.setupUi()

    def showdashboard(self):
        self.main_window.showDashboard()

    def showsetting(self):
        self.main_window.showsetting()

    def shownotification(self):
        self.main_window.shownotification()
    
    def showprofile(self):
        self.main_window.showprofile()

    def showhelp(self):
        self.main_window.showhelp()

    def confirmlogout(self):
        result = QMessageBox.question(None, "Logout", "Do you want to logout?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        logout=result == QMessageBox.Yes
        if logout:
            self.main_window.showlogin()


    def setupUi(self):
        self.resize(1096, 100)
        self.main_wid=self if self.main_wid is None else self.main_wid
        self.logobtn = QPushButton(self.main_wid)
        self.logobtn.setGeometry(QtCore.QRect(0, 10, 80, 80))
        self.logobtn.setObjectName("directorybtn")
        self.logobtn.setFlat(True)
        self.logobtn.enterEvent = lambda event: self.logobtn.setCursor(Qt.PointingHandCursor)
        self.logobtn.leaveEvent = lambda event: self.logobtn.setCursor(Qt.ArrowCursor)
        self.logobtn.clicked.connect(self.showdashboard)
        self.logoimg = QLabel(self.logobtn)
        self.logoimg.setGeometry(QtCore.QRect(-35, -10, 150, 100))
        self.logoimg.setStyleSheet("image:url(:/newPrefix/images/Malx logo.png);\n""background-repeat:no-repeat !important;\n""text-align:center !important;\n""margin:0px auto !important;")
        self.logoimg.setObjectName("Directoryimg")

        # self.btn2=QPushButton(self.main_wid)
        # self.btn2.setGeometry(QtCore.QRect(760, 10, 130, 80))
        # self.btn2.setFlat(True)
        # self.btn2.clicked.connect(self.showprofile)
        # self.btn2.enterEvent = lambda event: self.btn2.setCursor(Qt.PointingHandCursor)
        # self.btn2.leaveEvent = lambda event: self.btn2.setCursor(Qt.ArrowCursor)
        # self.label_2 = QLabel(self.btn2)
        # self.label_2.setGeometry(QtCore.QRect(-30, -10, 140, 100))
        # self.label_2.setStyleSheet("image:url(:/newPrefix/images/user.png);\n""background-repeat:no-repeat !important;\n""text-align:center !important;\n""margin:0px auto !important;")
        # self.label_2.setObjectName("label_2")
        # self.label_2.hide()

        # self.btn3=QPushButton(self.main_wid)
        # self.btn3.setGeometry(QtCore.QRect(840, 10, 80, 80))
        # self.btn3.setFlat(True)
        # self.btn3.clicked.connect(self.shownotification)
        # self.btn3.enterEvent = lambda event: self.btn3.setCursor(Qt.PointingHandCursor)
        # self.btn3.leaveEvent = lambda event: self.btn3.setCursor(Qt.ArrowCursor)

        # self.label_3 = QLabel(self.btn3)
        # self.label_3.setGeometry(QtCore.QRect(-30, -10, 140, 100))
        # self.label_3.setStyleSheet("image:url(:/newPrefix/images/bell.png);\n""background-repeat:no-repeat !important;\n""text-align:center !important;\n""margin:0px auto !important;")
        # self.label_3.setObjectName("label_3")
        # self.label_3.hide()

        self.btn4 = QPushButton(self.main_wid)
        self.btn4.setGeometry(QtCore.QRect(920, 10, 80, 80))
        self.btn4.setFlat(True)
        self.btn4.clicked.connect(self.showsetting)
        self.btn4.enterEvent = lambda event: self.btn4.setCursor(Qt.PointingHandCursor)
        self.btn4.leaveEvent = lambda event: self.btn4.setCursor(Qt.ArrowCursor)

        self.label_4=QLabel(self.btn4)
        self.label_4.setGeometry(QtCore.QRect(-30, -10, 140, 100))
        self.label_4.setStyleSheet("image:url(:/newPrefix/images/settings.png);\n""background-repeat:no-repeat !important;\n""text-align:center !important;\n""margin:0px auto !important;")
        self.label_4.setObjectName("label_4")
        
        self.btn5 = QPushButton(self.main_wid)
        self.btn5.setGeometry(QtCore.QRect(1000, 10, 80, 80))
        self.btn5.setFlat(True)
        self.btn5.enterEvent = lambda event: self.btn5.setCursor(Qt.PointingHandCursor)
        self.btn5.leaveEvent = lambda event: self.btn5.setCursor(Qt.ArrowCursor)
        self.btn5.clicked.connect(self.confirmlogout)
        self.label_5=QLabel(self.btn5)
        self.label_5.setGeometry(QtCore.QRect(-20, -5, 130, 90))
        self.label_5.setStyleSheet("image:url(:/newPrefix/images/logout.png);\n""background-repeat:no-repeat !important;\n""text-align:center !important;\n""margin:0px auto !important;")
        self.label_5.setObjectName("label_5")

        self.horizontalLine = QFrame(self.main_wid)
        self.horizontalLine.setGeometry(QtCore.QRect(0, 100, 1111, 1)) 
        self.horizontalLine.setStyleSheet("background-color: #000;") 
        QtCore.QMetaObject.connectSlotsByName(self)


if __name__=='__main__':
    import sys
    app=QApplication(sys.argv)
    window = HeaderWidget(app)
    window.show()
    sys.exit(app.exec_())



# testing git 