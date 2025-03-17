# Multithreading refers to the ability of a program to execute multiple threads concurrently.
# A thread is a sequence of instructions that can run and independently and concurrently with other threads within a process.
# In PyQt6, the QThread class is used to create a new thread.

import sys
from PyQt6.QtCore import QThread, pyqtSignal
import time
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLabel

class WorkerThread(QThread):
    progress_updated = pyqtSignal(int)

    def run(self):
        for i in range(101):
            time.sleep(0.1)
            self.progress_updated.emit(i)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multi-Threading in PyQt6")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()
        self.button = QPushButton("Start")

        self.button.clicked.connect(self.start_thread)
        self.label = QLabel("Progress: ")

        layout.addWidget(self.button)
        layout.addWidget(self.label)
        
        self.setLayout(layout)

        self.worker_thread = WorkerThread()
        self.worker_thread.progress_updated.connect(self.update_progress)

    def start_thread(self):
        self.button.setDisabled(True)
        self.worker_thread.start()

    def update_progress(self, progress):
        self.label.setText(f"Progress: {progress}%")
        if progress == 100:
            self.button.setDisabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
        

