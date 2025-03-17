from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6.QtCore import QTimer
from enemy import Enemy
from score import Score
from PyQt6.QtGui import QPixmap


class Bullet(QGraphicsPixmapItem):
    def __init__(self):
        super().__init__()

        self.setPixmap(QPixmap("24-PyQt6_Game_One-Build_Games_in_PyQt6/bullet.png").scaled(50, 50))

        self.timer = QTimer()

        self.timer.timeout.connect(self.move)

        self.timer.start(10)

    def move(self):
        self.setPos(self.x(), self.y() - 10)

        colliding_items = self.collidingItems()

        for item in colliding_items:
            if isinstance(item, Enemy):
                for scene_item in self.scene().items():
                    if isinstance(scene_item, Score):
                        scene_item.increase()

                self.scene().removeItem(item)
                self.scene().removeItem(self)

                self.timer.stop()

                del item
                del self

                return
            
        if self.y() - self.pixmap().height() > self.scene().height():
            self.scene().removeItem(self)
            self.timer.stop()
            del self

    