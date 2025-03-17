from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
import sys

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()

engine.load('20-QtQuick3D/02-add_model_to_scene.qml')

sys.exit(app.exec())