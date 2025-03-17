import sys
from PyQt6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsItem
from player import Player
from enemy import Enemy
from PyQt6.QtCore import Qt, QTimer, QUrl
from score import Score
from health import Health
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtGui import QPixmap

class Window(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.setup_music()

        self.scene = QGraphicsScene()

        self.setStyleSheet("background-color: white;")

        self.player = Player()
        self.player.setPixmap(QPixmap("24-PyQt6_Game_One-Build_Games_in_PyQt6/player.png").scaled(80, 80))

        self.scene.addItem(self.player)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.setScene(self.scene)

        self.player.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)
        self.player.setFocus()

        self.setWindowTitle("PyQt6 Game One")
        self.setFixedSize(800, 600)

        self.score = Score()
        self.scene.addItem(self.score)
        self.score.setPos(self.score.x() + 5, self.score.y() + 5)

        self.health = Health()
        self.scene.addItem(self.health)
        self.health.setPos(self.health.x() + 5, self.health.y() + 35)

        self.scene.setSceneRect(0, 0, 800, 600)

        self.player.setPos(self.scene.width()/2 - self.player.pixmap().width()/2, self.scene.height() - self.player.pixmap().height())

        self.timer = QTimer()
        self.timer.timeout.connect(self.spawn)
        self.timer.start(2000)

    def spawn(self):
        enemy = Enemy()
        self.scene.addItem(enemy)

    def setup_music(self):
        self.media_player = QMediaPlayer()
        self.audio = QAudioOutput()
        self.audio.setVolume(0.1)

        self.media_player.setAudioOutput(self.audio)

        music_file = QUrl.fromLocalFile("24-PyQt6_Game_One-Build_Games_in_PyQt6/bgmusic.mp3")
        self.media_player.setSource(music_file)

        self.media_player.play()



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())