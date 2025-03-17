from PyQt6.QtWidgets import QGraphicsTextItem
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class Health(QGraphicsTextItem):
    def __init__(self):
        super().__init__()

        self.health = 3

        self.setPlainText(f"Health: {str(self.health)}")
        self.setFont(QFont("Sanserif", 16))
        self.setDefaultTextColor(Qt.GlobalColor.green)

    def decrease(self, lifes=1):
        self.health -= lifes
        
        if self.health < 0:
            self.health = 0

        self.setPlainText(f"Health: {str(self.health)}")

    def is_alive(self):
        return self.health > 0