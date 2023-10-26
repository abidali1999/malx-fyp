# from PyQt5.QtCore import QObject, pyqtSignal
# import os
# import threading
# from qrc import source_rc
# import time
# from datetime import datetime

# class ProgressWorker(QObject):
#     progress = pyqtSignal(int,QObject)

#     def __init__(self):
#         super().__init__()
#         self.lock = threading.Lock()

#     def start_scan(self, directory,progid):
#         self.progid=progid

#         self.total_files = len(os.listdir(directory))
#         self.scanned_files = 0
#         self.threats_found=0

#         def scan_directory(directory, files_in_this_folder):
#             for entry in os.scandir(directory):
#                 try: 
#                     if entry.is_file():
#                         with self.lock:
#                             self.scanned_files += 1
#                             self.scanned_files = min(self.scanned_files, self.total_files)
#                             progress_percentage = int((self.scanned_files / self.total_files) * 100)
#                         self.progress.emit(progress_percentage,self.progid)
#                     elif entry.is_dir():
#                         files_in_this_folder = len(os.listdir(entry.path))
#                         with self.lock:
#                             self.total_files += files_in_this_folder
#                         scan_directory(entry.path, files_in_this_folder)
#                 except Exception as e: 
#                     with self.lock:
#                         self.total_files -= files_in_this_folder
#                     print(repr(e))
#                     pass
            

#         def start_scan_in_thread():
#             start=time.time()
#             scan_directory(directory, self.total_files)
#             total_time_s=time.time()-start
#             self.total_time=f'{total_time_s//60}m, {total_time_s%60}s'
#             date_today=datetime.today().strftime('%Y-%m-%d-%H-%M')


#             self.progress.emit(100,progid)  # Asegura que el progreso llegue al 100% al finalizar.
#             print("Scanning completed. Total files:", self.total_files)
#             return self.threats_found,self.scanned_files,self.total_time
            

#         # Crear un hilo para ejecutar la función scan_directory
#         scan_thread = threading.Thread(target=start_scan_in_thread)
#         scan_thread.start()

#         print("Scanning started in a separate thread.")


from PyQt5.QtCore import QObject, pyqtSignal
import os
import threading
from datetime import datetime
import time
class ProgressWorker(QObject):
    progress = pyqtSignal(int, int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.lock = threading.Lock()
        self.total_time = None
        self.threats_found = 0
        self.scanned_files = 0
        self.threats_quarantined=0
        self.completed_event = threading.Event()

    def start_scan(self, directory, progid, callback):
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
