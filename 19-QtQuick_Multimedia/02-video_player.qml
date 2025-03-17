import QtQuick.Controls
import QtMultimedia
import QtQuick

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "VideoPlayer"

    MediaPlayer {
        id: mediaPlayer
        source: "media/video.MOV"
        audioOutput: AudioOutput {}
        videoOutput: videoOutput
    }

    VideoOutput {
        id: videoOutput
        anchors.fill: parent
        anchors.margins: 20
    }

    Component.onCompleted: {
        mediaPlayer.play()
    }
}
