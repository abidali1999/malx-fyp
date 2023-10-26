from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel
from qrc import source_rc



class DragnDropLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAlignment(Qt.AlignCenter)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls() and e.mimeData().urls()[0].isLocalFile() and e.mimeData().urls()[0].toLocalFile().lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        file_path = e.mimeData().urls()[0].toLocalFile()
