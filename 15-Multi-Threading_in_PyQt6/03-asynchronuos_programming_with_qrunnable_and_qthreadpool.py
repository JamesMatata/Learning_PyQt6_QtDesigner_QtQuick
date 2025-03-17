"""
QRunnable and QThreadPool:
    - QRunnable is a class that represents a task that can be run asynchronously.
    - By using QRunnable, you can create a task that can be run in a separate thread.
    - QThreadPool is a class that manages a collection of QRunnable tasks.
    - By using QThreadPool, you can run multiple QRunnable tasks concurrently.

Benefits of using QRunnable and QThreadPool:
    - Concurrency: QRunnable and QThreadPool provide a way to run multiple tasks concurrently.
    - Easy Integration: QRunnable and QThreadPool can be easily integrated with PyQt6 applications.
    - Thread Management: QThreadPool manages the creation and execution of threads, making it easier to manage threads in PyQt6 applications. It also ensure better resource utilization.
    - Signaling and Communication: QRunnable and QThreadPool can be used to communicate between threads using signals and slots.
"""

import sys, time
from random import randint
from PyQt6.QtCore import QRunnable, pyqtSignal, Qt, QObject, QThreadPool
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QPushButton, QScrollArea

class WorkerSignals(QObject):
    # This class acts as the emmitter of signals
    result_ready = pyqtSignal(int)

class Worker(QRunnable):
    def __init__(self, worker_id, signals):
        super().__init__()
        self.worker_id = worker_id
        self.signals = signals

    def run(self):
        time.sleep(randint(1, 5))
        result = self.worker_id * 10

        self.signals.result_ready.emit(result)

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

        self.thread_pool = QThreadPool()

    def start_tasks(self):
        self.button.setDisabled(True)

        for i in range(1, 6):
            signals = WorkerSignals()
            worker = Worker(i, signals)
            worker.signals.result_ready.connect(self.collect_results)
            self.thread_pool.start(worker)


    def collect_results(self, result):
        current_result = self.results_label.text()
        self.results_label.setText(current_result + f"\nResult: {result}")

        self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum())

        if self.thread_pool.activeThreadCount() == 0:
            self.button.setDisabled(False)

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())