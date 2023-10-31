from PyQt5.QtWidgets import QApplication,QVBoxLayout, QMainWindow, QLabel, QTableWidget, QTableWidgetItem, QSizePolicy, QHBoxLayout, QWidget
import sys
from MyPushButton import PushButton
from PyQt5.QtCore import Qt,QRect
import requests
from report import Ui_scanhistorywindow
from my_header import HeaderWidget

class MyTable(QTableWidget):
    def __init__(self, data,parent):
        super().__init__()
        self.data = data
        self.main_window=parent
        self.tt={i:x[0] for i,x in enumerate(self.data)}
        self.data=[[x[1],x[3]] for x in data]
        print(self.tt)
        self.init_ui()    

    def show_report(self,report_id):
        self.main_window.update_report(report_id)
        self.main_window.showreport()

    def init_ui(self):
        self.setColumnCount(1)
        self.horizontalHeader().setVisible(False)  
        self.setRowCount(len(self.data) + 1)
        header_layout = QHBoxLayout()
        header_layout.addWidget(QLabel('Directory'))
        header_layout.addWidget(QLabel('Date'))
        header_label = QLabel(self)
        header_label.setLayout(header_layout)
        self.setCellWidget(0, 0, header_label)
        for i, row in enumerate(self.data):
            data_layout = QHBoxLayout()
            data_layout.addWidget(QLabel(row[0]))
            data_layout.addWidget(QLabel(row[1]))
            self.setColumnWidth(i, 1096)
            button = PushButton(self)
            button.setLayout(data_layout)
            button.clicked.connect(self.handle_button_click)
            self.setCellWidget(i+1, 0, button)

    def handle_button_click(self):
        button = self.sender()
        index = self.indexAt(button.pos())
        row = index.row()
        data = self.data[row-1]
        report_id=self.tt[row-1]
        self.show_report(report_id)
        # self.report=Ui_scanhistorywindow(self.main_window,report_id)
        # self.report.show()
        print("Button Clicked for Row:", data)

class UI_scans(QMainWindow):
    def __init__(self, parent):
        self.main_window = parent
        super().__init__()
        self.setupUI()
        # header = HeaderWidget(self)

    def open_dashboard(self):
        self.main_window.showDashboard()

    def setupUI(self):
        self.resize(1096, 841)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)
        # data = [[1, 'some directory', 'NO', '10-22-2023', 'boota@gmail.com'],
        #         [1, 'some directory', 'NO', '10-22-2023', 'boota@gmail'],
        #         [1, 'some directory', 'NO', '10-22-2023', 'boota@gmail.com']]

        # Create an instance of the HeaderWidget
        data=self.load_data()
        header = HeaderWidget(self.main_window,self)
        header.setFixedSize(1096, 91)  # Set a fixed size for the header
        layout.addWidget(header)  # Add the header to the layout

        self.table_widget = MyTable(data, self.main_window)
        layout.addWidget(self.table_widget)  # Add the table below the header

        self.pushButton_5 = PushButton(self, True)
        self.pushButton_5.setFixedSize(121, 41)
        layout.addWidget(self.pushButton_5, alignment=Qt.AlignBottom | Qt.AlignRight)

        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.open_dashboard)
        self.pushButton_5.setText('Back')


    def load_data(self):
        api_url = 'https://abidali1999063.pythonanywhere.com/data_api'  # Replace with your actual API URL
        data = {
            'userid': self.main_window.userid,
            'qtype': 'scan'
        }
        response = requests.get(api_url, params=data).json()
        print(response,type(response))
        return response


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # data = [
    #     ['Directory 1', 'Report 1', 'Status 1', '2023-10-22'],
    #     ['Directory 2', 'Report 2', 'Status 2', '2023-10-23'],
    #     ['Directory 3', 'Report 3', 'Status 3', '2023-10-24']
    # ]
    window = UI_scans(app)
    window.show()
    sys.exit(app.exec_())
