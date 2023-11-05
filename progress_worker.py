from PyQt5.QtCore import QObject, pyqtSignal
import os
import threading
from datetime import datetime
import time
from byteplot_func import create_byteplot_image
import numpy as np
from quarantine import encrypt_and_move_to_quarantine



class ProgressWorker(QObject):
    progress = pyqtSignal(int, int)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.lock = threading.Lock()
        self.total_time = None
        self.MAX_FILE_SIZE = 10 * 1024 * 1024
        self.threats_found = 0
        self.scanned_files = 0
        self.threats_quarantined=0
        self.completed_event = threading.Event()

    def start_scan(self, directory, progid, callback):
        from keras.preprocessing import image
        from keras.models import load_model
        model = load_model('projekt_fyp\\model\\m192_v3.h5')

        self.progid = progid
        self.total_files = len(os.listdir(directory))
        self.scanned_files = 0
        def scan_directory(directory, files_in_this_folder):
            for entry in os.scandir(directory):
                try:
                    if entry.is_file():
                        with self.lock:
                            self.scanned_files += 1
                            self.scanned_files = min(self.scanned_files, self.total_files)
                            progress_percentage = int((self.scanned_files / self.total_files) * 100)
                        self.progress.emit(progress_percentage, self.progid)
                    elif entry.is_dir():
                        files_in_this_folder = len(os.listdir(entry.path))
                        with self.lock:
                            self.total_files += files_in_this_folder
                            if entry.name.endswith(".dll") or entry.name.endswith(".exe"):
                                self.total_files += 1
                                self.scanned_files += 1
                                img=create_byteplot_image(entry.path)
                                img_array = image.img_to_array(img)
                                img_array = np.expand_dims(img_array, axis=0)
                                img_array /= 255.0  
                                predictions = model.predict(img_array)            
                                predicted_class_index = np.argmax(predictions)
                                code_to_class={0: 'AdwareWin32Gabpath', 1: 'AdwareWin32SaveShare', 2: 'BackdoorWin32Kelihos.F', 3: 'BackdoorWin32PcClient.BX', 4: 'BackdoorWin32Rbot', 5: 'BackdoorWin32Zegost.AD', 6: 'DialerWin32InstantAccess', 7: 'ExploitWin32CVE-2010-0188', 8: 'ExploitWin32Pdfjsc.RF', 9: 'PWSWin32Ceekat.gen!A', 10: 'PWSWin32Lolyda.BF', 11: 'PWSWin32OnLineGames.IZ', 12: 'PWSWin32OnLineGames.JB', 13: 'RogueWin32Defmid', 14: 'TrojanDownloaderWin32Beebone.FN', 15: 'TrojanDropperWin32Systex.A', 16: 'TrojanJSBlacoleRef.DF', 17: 'TrojanSpyWin32Tiop.A', 18: 'TrojanWin32Agent', 19: 'TrojanWin32Delf.KP', 20: 'WormWin32Vobfus.gen!D', 21: 'benign'}
                                class_labels=[]
                                for key in sorted(code_to_class.keys()): class_labels.append(code_to_class[key])
                                predicted_class = class_labels[predicted_class_index]
                                if predicted_class!='benign': 
                                    self.threats_found+=1
                                    self.threats_quarantined+=1
                                    encrypt_and_move_to_quarantine(entry.path)
                        scan_directory(entry.path, files_in_this_folder)
                except Exception as e:
                    with self.lock:
                        self.total_files -= files_in_this_folder
                    print(repr(e))
                    # You might want to log or display the error.

        def start_scan_in_thread():
            start = time.time()
            scan_directory(directory, self.total_files)
            total_time_s = time.time() - start
            self.total_time = f'{int(total_time_s//60)}m, {int(total_time_s%60)}s'
            date_today = datetime.today().strftime('%Y-%m-%d-%H-%M')
            self.completed_event.set()  # Signal that the thread has completed

            self.progress.emit(100, self.progid)  # Ensure progress reaches 100% when completed
            print("Scanning completed. Total files:", self.total_files)

            if callback:
                callback(directory,self.threats_found,date_today,self.scanned_files,self.total_time,self.threats_quarantined)

        # Create a thread to execute the scan_directory function
        scan_thread = threading.Thread(target=start_scan_in_thread)
        scan_thread.start()

        print("Scanning started in a separate thread.")

    def wait_for_completion(self):
        self.completed_event.wait()
