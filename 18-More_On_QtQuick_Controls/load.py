from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
import sys

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()

engine.load('18-More_On_QtQuick_Controls/20-qtquick_controls_tooltip.qml')

sys.exit(app.exec())