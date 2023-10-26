# header_widget.py
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QSlider,QApplication,QFrame
from PyQt5 import QtCore
from qrc import source_rc
from MyPushButton import PushButton


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

    def setupUi(self):
        self.resize(1096, 100)
        self.main_wid=self if self.main_wid is None else self.main_wid
        self.logobtn = PushButton(self.main_wid)
        self.logobtn.setGeometry(QtCore.QRect(0, 10, 80, 80))
        self.logobtn.setObjectName("directorybtn")
        self.logobtn.setFlat(True)
        self.logobtn.clicked.connect(self.showdashboard)
        self.logoimg = QLabel(self.logobtn)
        self.logoimg.setGeometry(QtCore.QRect(-35, -10, 150, 100))
        self.logoimg.setStyleSheet("image:url(:/newPrefix/images/Malx logo.png);\n""background-repeat:no-repeat !important;\n""text-align:center !important;\n""margin:0px auto !important;")
        self.logoimg.setObjectName("Directoryimg")

        self.btn2=PushButton(self.main_wid)
        self.btn2.setGeometry(QtCore.QRect(760, 10, 130, 80))
        self.btn2.setFlat(True)
        self.btn2.clicked.connect(self.showprofile)
        self.label_2 = QLabel(self.btn2)
        self.label_2.setGeometry(QtCore.QRect(-30, -10, 140, 100))
        self.label_2.setStyleSheet("image:url(:/newPrefix/images/user.png);\n""background-repeat:no-repeat !important;\n""text-align:center !important;\n""margin:0px auto !important;")
        self.label_2.setObjectName("label_2")

        self.btn3=PushButton(self.main_wid)
        self.btn3.setGeometry(QtCore.QRect(840, 10, 80, 80))
        self.btn3.setFlat(True)
        self.btn3.clicked.connect(self.shownotification)
        self.label_3 = QLabel(self.btn3)
        self.label_3.setGeometry(QtCore.QRect(-30, -10, 140, 100))
        self.label_3.setStyleSheet("image:url(:/newPrefix/images/bell.png);\n""background-repeat:no-repeat !important;\n""text-align:center !important;\n""margin:0px auto !important;")
        self.label_3.setObjectName("label_3")

        self.btn4 = PushButton(self.main_wid)
        self.btn4.setGeometry(QtCore.QRect(920, 10, 80, 80))
        self.btn4.setFlat(True)
        self.btn4.clicked.connect(self.showsetting)
        self.label_4=QLabel(self.btn4)
        self.label_4.setGeometry(QtCore.QRect(-30, -10, 140, 100))
        self.label_4.setStyleSheet("image:url(:/newPrefix/images/settings.png);\n""background-repeat:no-repeat !important;\n""text-align:center !important;\n""margin:0px auto !important;")
        self.label_4.setObjectName("label_4")
        
        self.btn5 = PushButton(self.main_wid)
        self.btn5.setGeometry(QtCore.QRect(1000, 10, 80, 80))
        self.btn5.setFlat(True)
        self.btn5.clicked.connect(self.showhelp)
        self.label_5=QLabel(self.btn5)
        self.label_5.setGeometry(QtCore.QRect(-30, -10, 140, 100))
        self.label_5.setStyleSheet("image:url(:/newPrefix/images/question.png);\n""background-repeat:no-repeat !important;\n""text-align:center !important;\n""margin:0px auto !important;")
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