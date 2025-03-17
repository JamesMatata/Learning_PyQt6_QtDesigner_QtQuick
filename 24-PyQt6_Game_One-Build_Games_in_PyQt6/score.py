from PyQt6.QtWidgets import QGraphicsTextItem
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class Score(QGraphicsTextItem):
    def __init__(self):
        super().__init__()

        self.score = 0

        self.setPlainText(f"Score: {str(self.score)}")
        self.setFont(QFont("Sanserif", 16))
        self.setDefaultTextColor(Qt.GlobalColor.darkGray)

    def increase(self, points=1):
        self.score += points
        self.setPlainText(f"Score: {str(self.score)}")

