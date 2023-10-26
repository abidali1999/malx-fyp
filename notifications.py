from PyQt5.QtWidgets import QWidget
from my_header import HeaderWidget
class UI_notifications(QWidget):
    def __init__(self,main_window):
        super().__init__()
        self.main_window=main_window
        self.setupUI()
        self.active_scans=[]


    def setupUI(self):
        self.central_widget=QWidget(self)
        self.header=HeaderWidget(self.main_window,self.central_widget)
