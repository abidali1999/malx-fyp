from PyQt5 import QtWidgets
from my_header import HeaderWidget
from PyQt5.QtWidgets import QWidget


class UI_help(QtWidgets.QWidget):
    def __init__(self,main_window):
        super().__init__()
        self.main_window=main_window
        self.setupUI()
        self.active_scans=[]


    def setupUI(self):
        self.central_widget=QWidget(self)
        self.header=HeaderWidget(self.main_window,self.central_widget)
