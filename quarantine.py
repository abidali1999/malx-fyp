import sys
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QLabel,QHBoxLayout
from my_header import HeaderWidget
from PyQt5.QtCore import QRect
from MyPushButton import PushButton



class Ui_Quarantine(QWidget):
    def __init__(self,main_window):
        super().__init__()
        self.main_window=main_window
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Scrollable Label Example')
        self.setGeometry(100, 100, 1000, 800)

        # Create a scroll area
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setGeometry(0, 100, 1000, 800)
        self.header=HeaderWidget(self.main_window,self)
        # Create a widget to hold the labels
        widget = QWidget(scroll_area)
        scroll_area.setWidget(widget)

        # Create a vertical layout for the widget
        layout = QVBoxLayout(widget)
        layout.setSpacing(20)
        # Add a large number of labels
        for i in range(2):
            container = QLabel()
            container.setStyleSheet("border:2px solid black;\n")
            container.setFixedSize(800,100)
            
            layout.addWidget(container)

            directory_label=QLabel(container)
            directory_label.setText('directory label goes here')
            directory_label.setStyleSheet("font-size:14px;\n")
            directory_label.setGeometry(QRect(0, 0, 600, 50))

            malware_class_label=QLabel(container)
            malware_class_label.setText('malware class goes here')
            malware_class_label.setStyleSheet("font-size:14px;\n")
            malware_class_label.setGeometry(QRect(600, 0, 200, 50))

            delete_button=PushButton(container,True)
            delete_button.setText('remove')
            delete_button.setStyleSheet("font-size:14px;\n")
            delete_button.setGeometry(QRect(0, 50, 400, 50))


            release_button=PushButton(container,True)
            release_button.setText('relase')
            release_button.setStyleSheet("font-size:14px;\n")
            release_button.setGeometry(QRect(400, 50, 400, 50))
            

def main():
    app = QApplication(sys.argv)
    ex = Ui_Quarantine(app)
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
