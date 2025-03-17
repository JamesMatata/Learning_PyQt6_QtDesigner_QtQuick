"""
Results for using signals and slots to synchronize threads in PyQt6:
1. Thread Safe Communication: Signals and slots are thread-safe, which means that they can be used to communicate between threads(Exchanging data and signals).
2. GUI Responsiveness: Signals and slots can be used to update the GUI from a worker thread, which helps to keep the GUI responsive.
3. Asynchronous Procssing: Signals and slots can be used to perform asynchronous processing in a worker thread while keeping the main thread responsive.
4. Modularity and Maintainability: Signals and slots provide a modular and maintainable way to synchronize threads in PyQt6 applications.
"""

import sys, time
from random import randint
from PyQt6.QtCore import QThread, pyqtSignal, Qt
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QPushButton, QScrollArea

class Worker(QThread):
    result_ready = pyqtSignal(int)

    def __init__(self, worker_id):
        super().__init__()
        self.worker_id = worker_id

    def run(self):
        time.sleep(randint(1, 5))

        result = self.worker_id * 10

        self.result_ready.emit(result)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multi-Threading in PyQt6")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()
        self.button = QPushButton("Start")
        self.button.clicked.connect(self.start_tasks)

        layout.addWidget(self.button)

        self.scroll_area = QScrollArea()

        self.results_label = QLabel()
        self.results_label.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.results_label)

        layout.addWidget(self.scroll_area)
        
        self.setLayout(layout)

        self.worker_threads = []

    def start_tasks(self):
        self.button.setDisabled(True)

        for i in range(1, 6):
            worker = Worker(i)
            worker.result_ready.connect(self.collect_results)
            self.worker_threads.append(worker)
            worker.start()

    def collect_results(self, result):
        current_result = self.results_label.text()
        self.results_label.setText(current_result + f"\nResult: {result}")

        if len(self.worker_threads) == len([t for t in self.worker_threads if not t.isRunning()]):
            self.button.setDisabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


