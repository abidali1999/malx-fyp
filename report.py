from PyQt5 import QtCore, QtWidgets
from MyPushButton import PushButton
from qrc import source_rc
from my_header import HeaderWidget


class Ui_scanhistorywindow(QtWidgets.QWidget):
    def __init__(self,main_window):
        super().__init__()
        self.main_window=main_window
        self.setupUi()

    def open_scans(self):
        self.main_window.showscans()

    def update_screen(self,report_id):
        import requests
        api_url = 'https://abidali1999063.pythonanywhere.com/data_api'  # Replace with your actual API URL
        data = {
            'id': report_id,
            'qtype': 'report'
        }
        response = requests.get(api_url, params=data).json()[0]
        print(len(response))
        files_scanned,threats_found,threats_quarantined,time_taken=response[2],response[3],response[4],response[5]
        
        self.label_9.setText(time_taken)
        self.label_10.setText(str(files_scanned))
        self.threat_detected_text.setText(str(threats_found))
        self.threat_quarantine_text.setText(str(threats_quarantined))
        print(response,type(response))
        return response


    def setupUi(self):
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.resize(1096, 900)
        self.centralwidget.setObjectName("centralwidget")
        HeaderWidget(self.main_window,self.centralwidget)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(410, 120, 481, 131))
        self.label_7.setStyleSheet("font-size:20px;\n""font-weight:bold;\n""line-height:40px;\n""margin:0px auto;\n""text-align:center;\n""")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(430, 310, 171, 51))
        self.label_8.setStyleSheet("font-size:15px;\n""font-weight:bold;\n""line-height:40px;\n""margin:0px auto;\n""text-align:center;\n""color:#968989;\n""")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(620, 320, 171, 31))
        self.label_9.setStyleSheet("font-size:15px;\n""font-weight:bold;\n""line-height:40px;\n""margin:0px auto;\n""text-align:center;\n""")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(620, 360, 171, 31))
        self.label_10.setStyleSheet("font-size:15px;\n""font-weight:bold;\n""line-height:40px;\n""margin:0px auto;\n""text-align:center;\n""")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(400, 350, 201, 51))
        self.label_11.setStyleSheet("font-size:15px;\n""font-weight:bold;\n""line-height:40px;\n""margin:0px auto;\n""text-align:center;\n""color:#968989;\n""")
        self.label_11.setObjectName("label_11")
        self.threat_detected_text = QtWidgets.QLabel(self.centralwidget)
        self.threat_detected_text.setGeometry(QtCore.QRect(640, 440, 171, 31))
        self.threat_detected_text.setStyleSheet("font-size:15px;\n""font-weight:bold;\n""line-height:40px;\n""margin:0px auto;\n""text-align:center;\n""")
        self.threat_detected_text.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(380, 430, 221, 51))
        self.label_15.setStyleSheet("font-size:15px;\n""font-weight:bold;\n""line-height:40px;\n""margin:0px auto;\n""text-align:center;\n""color:#968989;\n""")
        self.label_15.setObjectName("label_15")
        self.threat_quarantine_text = QtWidgets.QLabel(self.centralwidget)
        self.threat_quarantine_text.setGeometry(QtCore.QRect(640, 640, 171, 31))
        self.threat_quarantine_text.setStyleSheet("font-size:15px;\n""font-weight:bold;\n""line-height:40px;\n""margin:0px auto;\n""text-align:center;\n""")
        self.threat_quarantine_text.setObjectName("label_18")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(310, 630, 291, 51))
        self.label_23.setStyleSheet("font-size:15px;\n""font-weight:bold;\n""line-height:40px;\n""margin:0px auto;\n""text-align:center;\n""text-transform:uppercase;\n""color:#968989;\n""")
        self.pushButton_5=PushButton(self.centralwidget,True)
        self.pushButton_5.setGeometry(QtCore.QRect(770, 760, 121, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setText('Back')
        self.pushButton_5.clicked.connect(self.open_scans)        
        self.label_23.setObjectName("label_23")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(360, 410, 491, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(360, 570, 491, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self, scanhistorywindow):
        _translate = QtCore.QCoreApplication.translate
        scanhistorywindow.setWindowTitle(_translate("scanhistorywindow", "MainWindow"))
        self.label_7.setText(_translate("scanhistorywindow", "THREAT SCAN SUMMARY"))
        self.label_8.setText(_translate("scanhistorywindow", "SCAN TIME"))
        self.label_9.setText(_translate("scanhistorywindow", "2m,9s"))
        self.label_10.setText(_translate("scanhistorywindow", "266,647"))
        self.label_11.setText(_translate("scanhistorywindow", "ITEM SCANNED"))
        self.threat_detected_text.setText(_translate("scanhistorywindow", "0"))
        self.label_15.setText(_translate("scanhistorywindow", "THREAT DETECTED"))
        self.threat_quarantine_text.setText(_translate("scanhistorywindow", "0"))
        self.label_23.setText(_translate("scanhistorywindow", "Detection quarantined"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_scanhistorywindow(app)
    window.show()
    sys.exit(app.exec_())

