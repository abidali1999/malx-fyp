import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

class File2UI(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        label = QLabel("This is File 2")
        layout.addWidget(label)

        self.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    window = File2UI()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
