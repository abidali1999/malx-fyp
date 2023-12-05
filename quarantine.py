import sys, os,shutil
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QLabel
from my_header import HeaderWidget
from PyQt5.QtCore import QRect
from MyPushButton import PushButton
import sqlite3
from cryptography.fernet import Fernet

# Initialize the database file and table if not already done
DATABASE_FILE = "quarantine_db.sqlite"
QUARANTINE_DIRECTORY = "C:\\Users\\user\\AppData\\Local\\malx\\quarantine_zone"

def initialize_database():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS quarantine (
                      source_path TEXT PRIMARY KEY,
                      quarantine_path TEXT,
                      key TEXT)''')
    conn.commit()
    conn.close()

def retrieve_quarantined_files():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT source_path, quarantine_path, key FROM quarantine")
    files = cursor.fetchall()
    conn.close()
    return files

def add_filepath_and_key_to_database(source_path, quarantine_path, key):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO quarantine (source_path, quarantine_path, key) VALUES (?, ?, ?)", (source_path, quarantine_path, key))
    conn.commit()
    conn.close()



def encrypt_and_move_to_quarantine(source_path):
    destination_path = os.path.join(QUARANTINE_DIRECTORY, os.path.basename(source_path))
    shutil.move(source_path, destination_path)
    key = Fernet.generate_key()
    print(len(key))
    cipher_suite = Fernet(key)
    with open(destination_path, 'rb') as f:
        original_data = f.read()
    encrypted_data = cipher_suite.encrypt(original_data)
    with open(destination_path, 'wb') as f:
        f.write(encrypted_data)
    add_filepath_and_key_to_database(source_path, destination_path, key)
    return destination_path



def delete_quarantined_file(source_path):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM quarantine WHERE source_path=?", (source_path,))
    conn.commit()
    conn.close()


def decrypt_and_remove_from_quarantine(filepath, destination_path, key,remove=False):
    if not remove: 
        cipher_suite = Fernet(key)
        with open(destination_path, 'rb') as f:
            encrypted_data = f.read()
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        with open(filepath, 'wb') as f:
            f.write(decrypted_data)

    os.remove(destination_path)

class Ui_Quarantine(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        initialize_database()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Quarantined Files')
        self.setGeometry(100, 100, 1000, 800)

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setGeometry(0, 100, 1000, 800)
        self.header = HeaderWidget(self.main_window, self)

        self.widget = QWidget(scroll_area)
        scroll_area.setWidget(self.widget)

        layout = QVBoxLayout(self.widget)
        layout.setSpacing(20)
        self.widget.setLayout(layout) 

        self.update_ui()  

    def update_ui(self):
        for i in reversed(range(self.widget.layout().count())):
            self.widget.layout().itemAt(i).widget().setParent(None)

        quarantined_files = retrieve_quarantined_files()

        for source_path, quarantine_path, key in quarantined_files:
            container = QLabel()
            container.setStyleSheet("border:2px solid black;\n")
            container.setFixedSize(800, 100)

            self.widget.layout().addWidget(container)

            directory_label = QLabel(container)
            directory_label.setText('Directory: ' + source_path)
            directory_label.setStyleSheet("font-size:14px;\n")
            directory_label.setGeometry(QRect(0, 0, 800, 50))

            delete_button = PushButton(container, True)
            delete_button.setText('Remove')
            delete_button.setStyleSheet("font-size:14px;\n")
            delete_button.setGeometry(QRect(0, 50, 400, 50))
            delete_button.clicked.connect(
                lambda _, src=source_path, dest=quarantine_path, k=key: self.remove_file(src, dest, k))

            release_button = PushButton(container, True)
            release_button.setText('Release')
            release_button.setStyleSheet("font-size:14px;\n")
            release_button.setGeometry(QRect(400, 50, 400, 50))
            release_button.clicked.connect(
                lambda _, src=source_path, dest=quarantine_path, k=key: self.release_file(src, dest, k))

    def release_file(self, source_path, destination_path, key):
        decrypt_and_remove_from_quarantine(source_path, destination_path, key)
        delete_quarantined_file(source_path)
        self.update_ui()  

    def remove_file(self, source_path, destination_path, key):
        decrypt_and_remove_from_quarantine(source_path, destination_path, key,remove=True)
        delete_quarantined_file(source_path)
        self.update_ui() 
        pass

def main():
    app = QApplication(sys.argv)
    ex = Ui_Quarantine(app)
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
