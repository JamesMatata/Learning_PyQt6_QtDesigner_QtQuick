from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6.QtCore import QTimer
from random import randint
from health import Health
from PyQt6.QtGui import QPixmap

class Enemy(QGraphicsPixmapItem):
    def __init__(self):
        super().__init__()

        random_number = randint(10, 700)
        self.setPos(random_number, 0)

        self.setPixmap(QPixmap("24-PyQt6_Game_One-Build_Games_in_PyQt6/enemy.png").scaled(60, 60))

        self.timer = QTimer()
        self.timer.timeout.connect(self.move)

        self.timer.start(50)

    def move(self):
        self.setPos(self.x(), self.y() + 5)

        if self.pos().y() + self.pixmap().height() < 0:
            self.scene().removeItem(self)
            del self

        colliding_items = self.collidingItems()

        for item in colliding_items:
            from player import Player
            if isinstance(item, Player):
                for scene_item in self.scene().items():
                    if isinstance(scene_item, Health):
                        scene_item.decrease()

                        if not scene_item.is_alive():
                            print("Game Over")
                            self.scene().views()[0].close()

                self.scene().removeItem(self)
                self.timer.stop()
                del self
                return
