from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtCore import QObject, pyqtSlot
from PyQt6.QtWidgets import QApplication
import sys


class Window(QObject):
    def __init__(self):
        super().__init__()

    @pyqtSlot()
    def hello(self):
        print('Hello, World!')



app = QApplication(sys.argv)
engine = QQmlApplicationEngine()
window = Window()
engine.rootContext().setContextProperty('window', window)
engine.load('C:/Users/James Matata/Desktop/CodeWizard/Python_Programming/Learning_Python_GUIs_with_PyQt6/11-QtQuick_and_QML_in_PyQt6/buttons.qml')
sys.exit(app.exec())