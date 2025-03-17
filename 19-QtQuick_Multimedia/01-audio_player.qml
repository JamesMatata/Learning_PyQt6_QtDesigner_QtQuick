import QtQuick.Controls
import QtMultimedia
import QtQuick

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "AudioPlayer"

    MediaPlayer {
        id: mediaPlayer
        source: "media/song.mp3"
        audioOutput: AudioOutput {}
    }

    Component.onCompleted: {
        mediaPlayer.play()
    }
}
