from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt
import numpy as np
from PyQt5 import QtCore, QtWidgets
from MyPushButton import PushButton
from drag_n_drop import DragnDropLabel
from qrc import source_rc
from my_header import HeaderWidget
from byteplot import create_byteplot_image
import joblib
import cv2
from quarantine import encrypt_and_move_to_quarantine

class Ui_Fileupload(QtWidgets.QWidget):
    def __init__(self,window):
        super().__init__()
        self.main_window=window
        self.selected_file_path = None
        self.setupUi()
        
    def select_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        self.selected_file_path, _ = QFileDialog.getOpenFileName(
            None, "Select a File to Upload", "", "All Files (*)", options=options
        )
        self.label_9.setText(f"Selected File: {self.selected_file_path}")
        
    def scan(self):
        if self.selected_file_path:
            from keras.preprocessing import image
            from keras.models import load_model
            model = load_model('projekt_fyp\\model\\m192_v3.h5')
            img=create_byteplot_image(self.selected_file_path)
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array /= 255.0  
            predictions = model.predict(img_array)            
            predicted_class_index = np.argmax(predictions)
            code_to_class={0: 'AdwareWin32Gabpath', 1: 'AdwareWin32SaveShare', 2: 'BackdoorWin32Kelihos.F', 3: 'BackdoorWin32PcClient.BX', 4: 'BackdoorWin32Rbot', 5: 'BackdoorWin32Zegost.AD', 6: 'DialerWin32InstantAccess', 7: 'ExploitWin32CVE-2010-0188', 8: 'ExploitWin32Pdfjsc.RF', 9: 'PWSWin32Ceekat.gen!A', 10: 'PWSWin32Lolyda.BF', 11: 'PWSWin32OnLineGames.IZ', 12: 'PWSWin32OnLineGames.JB', 13: 'RogueWin32Defmid', 14: 'TrojanDownloaderWin32Beebone.FN', 15: 'TrojanDropperWin32Systex.A', 16: 'TrojanJSBlacoleRef.DF', 17: 'TrojanSpyWin32Tiop.A', 18: 'TrojanWin32Agent', 19: 'TrojanWin32Delf.KP', 20: 'WormWin32Vobfus.gen!D', 21: 'benign'}
            class_labels=[]
            for key in sorted(code_to_class.keys()): class_labels.append(code_to_class[key])
            predicted_class = class_labels[predicted_class_index]
            self.label_9.setText(f'Predicted Class: {predicted_class}')
            if predicted_class!='bengin': encrypt_and_move_to_quarantine(self.selected_file_path)

    def go_back(self):
        self.main_window.showDashboard()

    def setupUi(self):
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.resize(1096, 900)
        self.centralwidget.setObjectName("centralwidget")
        self.header=HeaderWidget(self.main_window,self.centralwidget)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(410, 120, 481, 131))
        self.label_7.setStyleSheet("font-size:18px;\n""font-weight:bold;\n""line-height:40px;\n""margin:0px auto;\n""text-align:center;\n""")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(220, 200, 791, 111))
        self.label_8.setStyleSheet("font-size:15px;\n""line-height:40px;\n""margin:0px auto;\n""")
        self.label_8.setObjectName("label_8")
        self.drag_and_drop_label = DragnDropLabel(self.centralwidget)
        self.drag_and_drop_label.setGeometry(QtCore.QRect(230, 330, 230, 230))
        self.drag_and_drop_label.setStyleSheet("background:#FFFFFF;\n""border:1px solid black;")
        self.drag_and_drop_label.setAlignment(QtCore.Qt.AlignCenter)
        self.drag_and_drop_label.setAcceptDrops(True)
        self.drag_and_drop_label.setObjectName("drag_and_drop_label")
        self.drag_and_drop_label.dragEnterEvent = self.handle_drag_enter_event
        self.drag_and_drop_label.dropEvent = self.handle_drop_event
        self.label_6 = DragnDropLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(270, 400, 150, 100))
        self.label_6.setStyleSheet("image:url(:/newPrefix/images/scanner.png);\n""background-repeat:no-repeat !important;\n""text-align:center !important;\n""margin:0px auto !important;")
        self.label_6.setText("")
        self.label_6.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(330, 570, 600, 41))
        self.label_9.setStyleSheet("font-size:15px;\n""line-height:40px;\n""margin:0px auto;\n""text-align:center;\n""")
        self.label_9.setObjectName("label_9")
        self.pushButton_4 = PushButton(self.centralwidget,True)
        self.pushButton_4.setGeometry(QtCore.QRect(560, 450, 230, 41))
        self.pushButton_4.setStyleSheet("background:black;\n""color:#fff;\n""border:1px solid black;\n""font-weight:bold;\n""font-size:14px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.select_file)  
        self.pushButton_5 = PushButton(self.centralwidget,True)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 630, 121, 41))
        self.pushButton_5.setStyleSheet("background:white;\n""border:1px solid black;\n""font-weight:bold;\n""font-size:14px;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.scan)
        self.expander=QtWidgets.QPushButton(self.centralwidget)
        self.expander.setGeometry(QtCore.QRect(630, 700, 121, 41))
        self.expander.hide()
        self.pushButton_7 = PushButton(self.centralwidget,True)
        self.pushButton_7.setGeometry(QtCore.QRect(630, 630, 121, 41))
        self.pushButton_7.setStyleSheet("background:black;\n""color:#fff;\n""border:1px solid black;\n""font-weight:bold;\n""font-size:14px;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.go_back)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def handle_drop_event(self, event):
        mime_data = event.mimeData()
        if mime_data.hasUrls():
            file_url = mime_data.urls()[0].toLocalFile()
            if file_url.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                self.selected_file_path = file_url
                self.label_9.setText(f"Selected File: {file_url}")
                event.accept()
            else:
                QtWidgets.QMessageBox.warning(None, "Invalid File Type", "Please select an image file (jpg, jpeg, png, gif, bmp).")
        else:
            event.ignore()

    def handle_drag_enter_event(self, event):
        mime_data = event.mimeData()
        if mime_data.hasUrls() and len(mime_data.urls()) == 1:
            event.acceptProposedAction()
        else:
            event.ignore()

    def retranslateUi(self, Fileupload):
        _translate = QtCore.QCoreApplication.translate
        Fileupload.setWindowTitle(_translate("Fileupload", "MainWindow"))
        self.label_7.setText(_translate("Fileupload", "Virus Scanner"))
        self.label_8.setText(_translate("Fileupload", "Drag and drop suspicious files to detect malware and other breaches for free.\n""Scan any document, image, pdf, or other file types. Make sure your files are safe and free from viruses \n"" before you open them with Internxt\'s zero-knowledge Virus Scanner."))
        self.label_9.setText(_translate("Fileupload", "Drop file to scan for viruses"))
        self.pushButton_4.setText(_translate("Fileupload", "Browse"))
        self.pushButton_5.setText(_translate("Fileupload", "SCAN"))
        self.pushButton_7.setText(_translate("Fileupload", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Fileupload(app)
    window.show()
    sys.exit(app.exec_())
