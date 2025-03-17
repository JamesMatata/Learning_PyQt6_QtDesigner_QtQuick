from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
import sys

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()

engine.load('17-More_On_QtQuick/13-qtquick_transformation.qml')

sys.exit(app.exec())