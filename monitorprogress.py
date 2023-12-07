from PyQt5.QtWidgets import QWidget, QVBoxLayout, QProgressBar, QLabel, QApplication
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from MyPushButton import PushButton
from qrc import source_rc
from my_header import HeaderWidget
class ProgressWindow(QWidget):

    def open_dashboard(self):
        self.main_window.showDashboard()

    def __init__(self,main_window):
        super().__init__()
        self.main_window=main_window
        self.setup_UI()

    def remove_progress_bar(self,progid,label):
        # print(progid,type(progid))
        label.deleteLater()
        # progid.deleteLater()


    def add_progress_bar(self, directory):
        label = QLabel(self.body)
        label.setStyleSheet("border:1px solid black;")
        label.setFixedSize(500,100)
        label.setText(directory)

        progress_bar = QProgressBar(label)
        progress_bar.setStyleSheet("margin:0px auto !important;")
        progress_bar.setFixedSize(451, 41)
        # progress_bar.find

        # Set a fixed stretch factor to control the spacing
        self.body_layout.addWidget(label)
        # print('appending: ',progress_bar)
        self.progress_labels.append(label)
        self.progress_bars.append(progress_bar)  # Add the progress bar to the list
        return progress_bar,label  # Return the progress bar for further updates

    def set_progress(self, value, progress_bar):
        # print(progress_bar,type(progress_bar))
        # print('to update: ', progress_bar)
        if progress_bar in self.progress_bars:
            progress_bar.setValue(value)
            # print('setting value: ',value)
        # else: print('not found')

    def setup_UI(self):
        self.centralwidget = QWidget(self)
        self.centralwidget.resize(1096, 800)
        self.centralwidget.setObjectName("centralwidget")
        self.progress_bars = []
        self.progress_labels=[] 
        self.body_layout = QVBoxLayout()
        self.main_layout=QVBoxLayout()
        self.header=HeaderWidget(self.main_window,self)
        # self.header.setFixedSize(1100,200)
        
        self.body=QWidget(self.centralwidget)
        self.body.setLayout(self.body_layout)
        self.main_layout.addWidget(self.header)
        self.main_layout.addWidget(self.body)
        self.centralwidget.setLayout(self.main_layout)
        # self.body.setContentsMargins
        # self.body.setGeometry(QRect(0, 250, 1100, 550))
        # self.pushButton_5=PushButton(self.centralwidget,True)
        # self.pushButton_5.setText('Back')
        # self.pushButton_5.setGeometry(QRect(770, 660, 121, 41))
        # self.pushButton_5.setObjectName("pushButton_5")
        # self.pushButton_5.clicked.connect(self.open_dashboard)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, directorywindow):
        _translate = QtCore.QCoreApplication.translate
        directorywindow.setWindowTitle(_translate("directorywindow", "MainWindow"))
        # self.pushButton.setText(_translate("directorywindow", "ACTIVATE SUBSCRIPTION"))
        # self.pushButton_2.setText(_translate("directorywindow", "BUY NOW"))



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = ProgressWindow(app)
    
    # Add progress bars and get their references
    # progress_bar1 = window.add_progress_bar('C:\\Users\\user\Desktop\\test')
    # progress_bar2 = window.add_progress_bar('D:\digicartapp\digicart')
    # progress_bar3 = window.add_progress_bar('E://')
    # # Set values for progress bars
    # window.set_progress(60, progress_bar1)
    # window.set_progress(50, progress_bar2)
    # window.set_progress(10, progress_bar3)
    window.show()
    sys.exit(app.exec_())
