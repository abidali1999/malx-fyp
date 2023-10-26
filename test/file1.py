import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel


class File1UI(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("This is File 1")
        layout.addWidget(label)
        self.setLayout(layout)


def main():
    app = QApplication(sys.argv)
    window = File1UI()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
