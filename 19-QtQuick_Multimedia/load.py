from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
import sys

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()

engine.load('19-QtQuick_Multimedia/03-media.qml')

sys.exit(app.exec())