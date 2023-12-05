from PyQt5.QtWidgets import QFileDialog,QLabel
from PyQt5.QtCore import QThread
from MyPushButton import PushButton
from PyQt5 import QtCore, QtWidgets
from progress_worker import ProgressWorker
from qrc import source_rc
from my_header import HeaderWidget
class DirectoryScan(QtWidgets.QWidget):
    def __init__(self,main_window):
        
        super().__init__()
        self.main_window=main_window
        self.setupUi()
        self.active_scans=[]

    def open_dashboard(self):
        self.main_window.showDashboard()

    def setupUi(self):
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.resize(1096, 900)
        self.centralwidget.setObjectName("centralwidget")
        self.header=HeaderWidget(self.main_window,self.centralwidget)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(410, 210, 251, 251))
        self.label_6.setStyleSheet("image:url(:/newPrefix/images/search-file.png);\n""background-repeat:no-repeat !important;\n""text-align:center !important;\n""margin:0px auto !important;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = PushButton(self.centralwidget,True)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 520, 230, 41))
        self.pushButton_3.setStyleSheet("background:black;\n""color:#fff;\n""border:1px solid black;\n""font-weight:bold;\n""font-size:14px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.choose_scan_directory)
        self.choosen_directory=QLabel(self.centralwidget)
        self.choosen_directory.setGeometry(QtCore.QRect(430, 600, 430, 41))
        self.pushButton_4 = PushButton(self.centralwidget,True)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 660, 121, 41))
        self.pushButton_4.setStyleSheet("background:black;\n""color:#fff;\n""border:1px solid black;\n""font-weight:bold;\n""font-size:14px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5=PushButton(self.centralwidget,True)
        self.pushButton_5.setGeometry(QtCore.QRect(770, 660, 121, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.open_dashboard)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(310, 160, 451, 41))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        # self.menubar = QtWidgets.QMenuBar(self)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 1096, 22))
        # self.menubar.setObjectName("menubar")
        # self.statusbar = QtWidgets.QStatusBar(self)
        # self.statusbar.setObjectName("statusbar")
        self.scanning = False
        self.progressBar.hide()
        self.progress_thread = QThread()
        self.progress_worker = ProgressWorker()
        self.progress_worker.moveToThread(self.progress_thread)
        self.progress_worker.progress.connect(self.update_progress)
        self.progress_thread.start()
        self.pushButton_4.setText("CANCEL")
        self.pushButton_4.clicked.connect(self.perform_directory_scan)
        self.retranslateUi(self)
        # QtCore.QMetaObject.connectSlotsByName(self)

    def disconnect_all(self,btn):        
        for connection in btn.receivers(btn.clicked):
            btn.clicked.disconnect(connection)

    def toggle_scan(self):
        if self.scanning:
            self.scanning = False
            # self.progressBar.hide()
            # self.pushButton_3.show()
            # self.label_6.show()
            # self.pushButton_4.setText("SCAN")
            # self.pushButton_4.receivers
            # self.pushButton_4.disconnect()
            # self.pushButton_4.clicked.connect(self.perform_directory_scan)
        else:
            self.scanning = True
            # self.progressBar.show()
            # self.pushButton_3.hide()
            # self.label_6.hide()
            # self.pushButton_4.setText("CANCEL")
            # self.pushButton_4.disconnect()
            # self.pushButton_4.clicked.connect(self.toggle_scan)
        
    def update_progress(self, value,progid):
        self.progressBar.setValue(value)
        self.main_window.progress_window.set_progress(value,progid)

    def go_back(self):
        print('going back')
        # self.pushButton_4.setText("Back")
        # self.pushButton_4.disconnect()
        # self.pushButton_4.clicked.connect(self.toggle_scan)
        
    def choose_scan_directory(self):
        self.selected_directory=QFileDialog.getExistingDirectory(
            None, "Select a directory for scanning")
        print(self.selected_directory)
        self.choosen_directory.setText(self.selected_directory)

    def make_scan_entry(self,directory,threats_found,date_today,scanned_files,total_time,threats_quarantined):
        import requests
        url= "https://abidali1999063.pythonanywhere.com/record_api"
        data_scan = {
            "qtype": "scan",
            "directory": directory,
            "threats_found": threats_found,
            "date":date_today,  # Replace with the actual number of threats found
            "userid": self.main_window.userid  # Replace with the actual user ID
        }
        # url_report = "http://your-flask-app-url/record_api"
        
        response = requests.post(url, data=data_scan)
        print(response.status_code,response.text)
        last_id=response.json()['insert_id']
        data_report = {
            "qtype": "report",
            "id":last_id,
            "date": date_today,
            "threats_found": threats_found,  # Replace with the actual number of threats found
            "scanned_files": scanned_files,  # Replace with the actual user ID
            "threats_qurantined": threats_quarantined,
            "total_time":total_time
        }
        response = requests.post(url, data=data_report)
        # try:
        #     insert_id=response.text
        #     print(type(insert_id))
        # except: pass
    def perform_directory_scan(self):

        print(self.selected_directory)
        if self.selected_directory:
            prog=self.main_window.progress_window.add_progress_bar(self.selected_directory)
            print('as returned: ', prog)
            self.active_scans.append(prog)
            if not self.scanning: self.toggle_scan()  
            self.progress_worker.start_scan(self.selected_directory,prog,self.make_scan_entry)

            self.go_back()
        
    def retranslateUi(self, directorywindow):
        _translate = QtCore.QCoreApplication.translate
        directorywindow.setWindowTitle(_translate("directorywindow", "MainWindow"))
        self.pushButton_3.setText(_translate("directorywindow", "CHOOSE DIRECTORY "))
        self.pushButton_4.setText(_translate("directorywindow", "SCAN"))
        self.pushButton_5.setText(_translate("directorywindow", "BACK"))
        self.progressBar.setToolTip(_translate("directorywindow", "<html><head/><body><p><br/></p></body></html>"))
        self.progressBar.setWhatsThis(_translate("directorywindow", "<html><head/><body><p><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = DirectoryScan(app)
    
    window.show()
    sys.exit(app.exec_())
