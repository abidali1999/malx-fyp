import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget

# Import your custom UI classes from file1.py and file2.py
from file1 import File1UI
from file2 import File2UI
class MainApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('File Navigation Example')

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.file1_ui = File1UI()
        self.file2_ui = File2UI()

        self.central_widget.addWidget(self.file1_ui)
        self.central_widget.addWidget(self.file2_ui)

        self.navigation_button = QPushButton('Go to File 2', self)
        self.navigation_button.clicked.connect(self.switch_to_file2)
        self.navigation_button.setGeometry(10, 10, 150, 30)
        self.navigation_button = QPushButton('Go to File 1', self)
        self.navigation_button.clicked.connect(self.switch_to_file1)
        self.navigation_button.setGeometry(20, 10, 150, 30)

    def switch_to_file2(self):
        self.central_widget.setCurrentIndex(1)

    def switch_to_file1(self):
        self.central_widget.setCurrentIndex(0)

def main():
    app = QApplication(sys.argv)
    window = MainApplication()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
