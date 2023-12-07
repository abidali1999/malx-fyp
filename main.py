import sys
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5 import QtWidgets
from Fileupload import Ui_Fileupload
from signup import Ui_signupwindow
from login import Ui_loginwindow
from malxdashboard import Dashboard
from Directory_scan import DirectoryScan
from monitorprogress import ProgressWindow
from scan import UI_scans
from report import Ui_scanhistorywindow
from setting import Ui_settings
from notifications import UI_notifications
from help import Ui_Helpwindow
from profileUI import UI_profile
from quarantine import Ui_Quarantine
from feedback import Ui_Feedbackwindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):
        self.isloggedin=False
        self.userid=''
        self.resize(1096, 841)
        self.stackedWidget = QtWidgets.QStackedWidget()
        self.dashboard = Dashboard(self)
        self.directoryScan = DirectoryScan(self)
        self.filescan = Ui_Fileupload(self)
        self.login=Ui_loginwindow(self)
        self.signup=Ui_signupwindow(self)
        self.progress_window=ProgressWindow(self)
        self.scans=UI_scans(self)
        self.report=Ui_scanhistorywindow(self)
        self.setting=Ui_settings(self)
        self.notification=UI_notifications(self)
        self.help=Ui_Helpwindow(self)
        self.profile=UI_profile(self)
        self.quarantine=Ui_Quarantine(self)
        self.feedback=Ui_Feedbackwindow(self)
        self.stackedWidget.addWidget(self.dashboard)
        self.stackedWidget.addWidget(self.directoryScan)
        self.stackedWidget.addWidget(self.filescan)
        self.stackedWidget.addWidget(self.login)
        self.stackedWidget.addWidget(self.signup)
        self.stackedWidget.addWidget(self.progress_window)
        self.stackedWidget.addWidget(self.scans)
        self.stackedWidget.addWidget(self.report)
        self.stackedWidget.addWidget(self.setting)
        self.stackedWidget.addWidget(self.notification)
        self.stackedWidget.addWidget(self.help)
        self.stackedWidget.addWidget(self.profile)
        self.stackedWidget.addWidget(self.quarantine)
        self.stackedWidget.addWidget(self.feedback)
        self.setCentralWidget(self.stackedWidget)
        self.showlogin()

    def showDashboard(self):
        self.stackedWidget.setCurrentWidget(self.dashboard)
    def showDirectoryScan(self):
        self.stackedWidget.setCurrentWidget(self.directoryScan)
    def showfilescan(self):
        self.stackedWidget.setCurrentWidget(self.filescan)
    def showlogin(self):
        self.stackedWidget.setCurrentWidget(self.login)
    def showsignup(self):
        self.stackedWidget.setCurrentWidget(self.signup)
    def showprogress(self):
        self.stackedWidget.setCurrentWidget(self.progress_window)
    def showscans(self):
        self.scans.setupUI()
        self.stackedWidget.setCurrentWidget(self.scans)
    def showreport(self):
        self.stackedWidget.setCurrentWidget(self.report)
    def update_report(self,report_id):
        self.report.update_screen(report_id)
    def showsetting(self):
        self.stackedWidget.setCurrentWidget(self.setting)
    def shownotification(self):
        self.stackedWidget.setCurrentWidget(self.notification)
    def showhelp(self):
        self.stackedWidget.setCurrentWidget(self.help)
    def showfeedback(self):
        self.stackedWidget.setCurrentWidget(self.feedback)
    def showprofile(self):
        if self.isloggedin: self.stackedWidget.setCurrentWidget(self.profile)
        else: self.stackedWidget.setCurrentWidget(self.login)
    def showquarantine(self):
        self.quarantine.initUI()
        self.stackedWidget.setCurrentWidget(self.quarantine)

class BackgroundLabel(QLabel):
    def __init__(self, background_image_path, parent=None):
        super().__init__(parent)
        self.background_image_path = background_image_path
        self.setScaledContents(True)

    def paintEvent(self, event):
        painter = QPainter(self)
        background = QPixmap(self.background_image_path)
        painter.drawPixmap(self.rect(), background)
        super().paintEvent(event)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setFixedSize(1100,900)
    window.show()
    sys.exit(app.exec_())
