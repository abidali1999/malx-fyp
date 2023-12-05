from MyPushButton import PushButton
from PyQt5 import QtCore, QtWidgets
from qrc import source_rc
from my_header import HeaderWidget


class Dashboard(QtWidgets.QWidget):
    def __init__(self,main_window):
        self.main_window=main_window
        print(main_window)
        super().__init__()
        self.setupUi()
    
    def opendirectory(self):
        self.main_window.showDirectoryScan()

    def openfile(self):
        self.main_window.showfilescan()

    def openprogess(self):
        self.main_window.showprogress()
    
    def openscan(self):
        self.main_window.showscans()

    def opensetting(self):
        self.main_window.showsetting()

    def openquarantine(self):
        self.main_window.showquarantine()

    def opensetting(self):
        self.main_window.showsetting()

    def openhelp(self):
        self.main_window.showhelp()

    def openfeedback(self):
        self.main_window.showfeedback()

    def setupUi(self):
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setFixedSize(1100, 900)
        self.centralwidget.setObjectName("centralwidget")
        self.header=HeaderWidget(self.main_window,self.centralwidget)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(220, 120, 151, 121))
        self.label_6.setStyleSheet("image:url(:/newPrefix/images/verified.png);\n""background-repeat:no-repeat !important;\n""text-align:center !important;\n""margin:0px auto !important;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(360, 110, 481, 131))
        self.label_7.setStyleSheet("font-size:18px;\n""font-weight:bold;\n""line-height:40px;\n""")
        self.label_7.setObjectName("label_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 220, 121, 41))
        self.pushButton_3.setStyleSheet("background:white;\n""border:1px solid black;\n""font-weight:bold;\n""font-size:13px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.openscan)
        
        self.filebtn = PushButton(self.centralwidget,True)
        self.filebtn.setGeometry(QtCore.QRect(120, 310, 181, 191))
        self.filebtn.setObjectName("filebtn")
        self.fileimg = QtWidgets.QLabel(self.filebtn)
        self.fileimg.setGeometry(QtCore.QRect(30, 25, 121, 91))
        self.fileimg.setStyleSheet("image: url(:/newPrefix/images/file.png);\n""background-repeat:no-repeat !important;\n""text-align:center !important;\n""margin:0px auto !important;")
        self.fileimg.setObjectName("fileimg")
        # self.fileimg.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.filelabel = QtWidgets.QLabel(self.filebtn)
        self.filelabel.setGeometry(QtCore.QRect(30, 115, 131, 61))
        self.filelabel.setStyleSheet("font-size:14px;\n""font-weight:bold;\n""line-height:40px;\n")
        self.filelabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.filelabel.setText('File Scan')
        self.filelabel.setObjectName("filelabel")
        self.filebtn.clicked.connect(self.openfile)

        self.directorybtn = PushButton(self.centralwidget,True)
        self.directorybtn.setGeometry(QtCore.QRect(350, 310, 181, 191))
        self.directorybtn.setObjectName("directorybtn")
        self.Directoryimg = QtWidgets.QLabel(self.directorybtn)
        self.Directoryimg.setGeometry(QtCore.QRect(30, 25, 121, 91))
        self.Directoryimg.setStyleSheet("image: url(:/newPrefix/images/qr-code-scan.png);\n""background-repeat: no-repeat !important;\n""margin: 0px auto !important;")
        self.Directoryimg.setObjectName("Directoryimg")
        self.Directorylabel = QtWidgets.QLabel(self.directorybtn)
        self.Directorylabel.setGeometry(QtCore.QRect(30, 115, 131, 61))
        self.Directorylabel.setStyleSheet("font-size:14px;\n""font-weight:bold;\n""line-height:40px;\n")
        self.Directorylabel.setObjectName("Directorylabel")
        self.Directorylabel.setText('Directory Scan')
        self.directorybtn.clicked.connect(self.opendirectory)
        
        self.progressbtn = PushButton(self.centralwidget,True)
        self.progressbtn.setGeometry(QtCore.QRect(580, 310, 181, 191))
        self.progressbtn.setObjectName("progressbtn")
        self.progressimg = QtWidgets.QLabel(self.progressbtn)
        self.progressimg.setGeometry(QtCore.QRect(30, 25, 121, 91))
        self.progressimg.setStyleSheet("image:url(:/newPrefix/images/progress.png);\n""background-repeat:no-repeat !important;\n""margin:0px auto !important;")
        self.progressimg.setObjectName("progressimg")
        self.progresslabel = QtWidgets.QLabel(self.progressbtn)
        self.progresslabel.setGeometry(QtCore.QRect(30, 115, 131, 61))
        self.progresslabel.setStyleSheet("font-size:14px;\n""font-weight:bold;\n""line-height:40px;\n")
        self.progresslabel.setObjectName("progresslabel")
        self.progressbtn.clicked.connect(self.openprogess)

        self.classificationbtn = PushButton(self.centralwidget,True)
        self.classificationbtn.setGeometry(QtCore.QRect(810, 310, 181, 191))
        self.classificationbtn.setObjectName("classificationbtn")
        self.classificationlabel = QtWidgets.QLabel(self.classificationbtn)
        self.classificationlabel.setGeometry(QtCore.QRect(30, 115, 131, 61))
        self.classificationlabel.setStyleSheet("font-size:14px;\n""font-weight:bold;\n""line-height:40px;\n")
        self.classificationlabel.setObjectName("classificationlabel")
        self.classificationimg = QtWidgets.QLabel(self.classificationbtn)
        self.classificationimg.setGeometry(QtCore.QRect(30, 25, 121, 91))
        self.classificationimg.setStyleSheet("image:url(:/newPrefix/images/bug-detector.png);\n""background-repeat:no-repeat !important;\n""margin:0px auto !important;")
        self.classificationimg.setObjectName("classificationimg")
        self.classificationbtn.clicked.connect(self.openscan)

        self.qurantinebtn = PushButton(self.centralwidget,True)
        self.qurantinebtn.setGeometry(QtCore.QRect(120, 540, 181, 191))
        self.qurantinebtn.setObjectName("visualizationbtn")
        self.visualizationlabel = QtWidgets.QLabel(self.qurantinebtn)
        self.visualizationlabel.setGeometry(QtCore.QRect(30, 115, 131, 61))
        self.visualizationlabel.setStyleSheet("font-size:14px;\n""font-weight:bold;\n""line-height:40px;\n")
        self.visualizationlabel.setObjectName("visualizationlabel")
        self.visualizationimg = QtWidgets.QLabel(self.qurantinebtn)
        self.visualizationimg.setGeometry(QtCore.QRect(30, 25, 121, 91))
        self.visualizationimg.setStyleSheet("image:url(:/newPrefix/images/data-visualization.png);\n""background-repeat:no-repeat !important;\n""margin:0px auto !important;")
        self.visualizationimg.setObjectName("visualizationimg")
        self.qurantinebtn.clicked.connect(self.openquarantine)

        self.settingbtn = PushButton(self.centralwidget,True)
        self.settingbtn.setGeometry(QtCore.QRect(350, 540, 181, 191))
        self.settingbtn.setObjectName("settingbtn")
        self.settinglabel = QtWidgets.QLabel(self.settingbtn)
        self.settinglabel.setGeometry(QtCore.QRect(30, 115, 131, 61))
        self.settinglabel.setStyleSheet("font-size:14px;\n""font-weight:bold;\n""line-height:40px;\n")
        self.settinglabel.setObjectName("settinglabel")
        self.settingimg = QtWidgets.QLabel(self.settingbtn)
        self.settingimg.setGeometry(QtCore.QRect(30, 25, 121, 91))
        self.settingimg.setStyleSheet("image:url(:/newPrefix/images/settings.png);\n""background-repeat:no-repeat !important;\n""text-align:center !important;\n""margin:0px auto !important;")
        self.settinglabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.settingimg.setObjectName("settingimg")
        self.settingbtn.clicked.connect(self.opensetting)


        self.helpbtn = PushButton(self.centralwidget,True)
        self.helpbtn.setGeometry(QtCore.QRect(580, 540, 181, 191))
        self.helpbtn.setObjectName("helpbtn")
        self.helpimg = QtWidgets.QLabel(self.helpbtn)
        self.helpimg.setGeometry(QtCore.QRect(30, 25, 121, 91))
        self.helpimg.setStyleSheet("image:url(:/newPrefix/images/question.png);\n""background-repeat:no-repeat !important;\n""text-align:center !important;\n""margin:0px auto !important;")
        self.helpimg.setObjectName("helpimg")
        self.helplabel = QtWidgets.QLabel(self.helpbtn)
        self.helplabel.setGeometry(QtCore.QRect(30, 115, 131, 61))
        self.helplabel.setStyleSheet("font-size:14px;\n""font-weight:bold;\n""line-height:40px;\n""text-align:center\n""")
        self.helplabel.setObjectName("helplabel")
        self.helplabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.helpbtn.clicked.connect(self.openhelp)



        self.feedbackbtn = PushButton(self.centralwidget,True)
        self.feedbackbtn.setGeometry(QtCore.QRect(810, 540, 181, 191))
        self.feedbackbtn.setObjectName("feedbackbtn")
        self.feedbackimg = QtWidgets.QLabel(self.feedbackbtn)
        self.feedbackimg.setGeometry(QtCore.QRect(30, 25, 121, 91))
        self.feedbackimg.setStyleSheet("image:url(:/newPrefix/images/feedback.png);\n""background-repeat:no-repeat !important;\n""text-align:center !important;\n""margin:0px auto !important;")
        self.feedbackimg.setObjectName("feedbackimg")
        self.feedbacklabel = QtWidgets.QLabel(self.feedbackbtn)
        self.feedbacklabel.setGeometry(QtCore.QRect(30, 115, 131, 61))
        self.feedbacklabel.setStyleSheet("font-size:14px;\n""font-weight:bold;\n""line-height:40px;\n""text-align:center\n""")
        self.feedbacklabel.setObjectName("feedbacklabel")
        self.feedbacklabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.feedbackbtn.clicked.connect(self.openfeedback)
        # self.menubar = QtWidgets.QMenuBar(self)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 1096, 22))
        # self.menubar.setObjectName("menubar")
        # self.statusbar = QtWidgets.QStatusBar(self)
        # self.statusbar.setObjectName("statusbar")
        self.retranslateUi(self)        
        QtCore.QMetaObject.connectSlotsByName(self)
        
    def retranslateUi(self, dashboard):
        _translate = QtCore.QCoreApplication.translate
        dashboard.setWindowTitle(_translate("dashboard", "MainWindow"))
        # self.pushButton.setText(_translate("dashboard", "ACTIVATE SUBSCRIPTION"))
        # self.pushButton_2.setText(_translate("dashboard", "BUY NOW"))
        self.label_7.setText(_translate("dashboard", "YOUR DEVICE IS PROTECTED\n""SOME SYSTEM ISSUES REQUIRE YOUR ATTENTION"))
        self.pushButton_3.setText(_translate("dashboard", "VIEW DETAILS"))
        self.filelabel.setText(_translate("dashboard", "FILE UPLOAD"))
        self.Directorylabel.setText(_translate("dashboard", "DIRECTORY SCAN"))
        self.progresslabel.setText(_translate("dashboard", "PROGRESS \n""MONITORING"))
        self.classificationlabel.setText(_translate("dashboard", "CLASSIFICATION \n""RESULT"))
        self.visualizationlabel.setText(_translate("dashboard", "QUARANTINED \nTHREATS"))
        self.settinglabel.setText(_translate("dashboard", "SETTING"))
        self.helplabel.setText(_translate("dashboard", "HELP"))
        self.feedbacklabel.setText(_translate("dashboard", "FEED BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Dashboard(app)
    window.setFixedSize(1100,900)
    window.show()
    sys.exit(app.exec_())


