from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
import sys

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()

engine.load('21-QtQuick_Animation/04-gui_animation_with_qtquick.qml')

sys.exit(app.exec())