from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QWidget,QLabel,QApplication
from my_header import HeaderWidget

class UI_profile(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.main_window=parent
        self.setup_UI()

    def setup_UI(self):
        self.central_widget=QWidget(self)
        self.header=HeaderWidget(self.main_window,self.central_widget)

        self.logintext=QLabel(self.central_widget)
        self.logintext.setGeometry(QRect(50, 100, 140, 100))
        # self.logintext.setStyleSheet("image:url(:/newPrefix/images/question.png);\n""background-repeat:no-repeat !important;\n""text-align:center !important;\n""margin:0px auto !important;")
        self.logintext.setObjectName("label_5")
        self.logintext.setText('Logged in as: ')


if __name__=='__main__':
    import sys
    app=QApplication(sys.argv)
    window=UI_profile(app)
    window.show()
    sys.exit(app.exec_())