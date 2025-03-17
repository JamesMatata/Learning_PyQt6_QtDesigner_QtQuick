import QtQuick.Controls
import QtMultimedia
import QtQuick

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "MediaPlayer"

    MediaPlayer {
        id: mediaPlayer
        source: "media/video2.MOV"
        audioOutput: audioOutput
        videoOutput: videoOutput
    }

    AudioOutput {
        id: audioOutput
        volume: volumeSlider.value
    }

    VideoOutput {
        id: videoOutput
        anchors.fill: parent
        anchors.margins: 20
    }

    Slider {
        id: volumeSlider
        anchors.top: parent.top
        anchors.right: parent.right
        anchors.margins: 20
        orientation: Qt.Vertical
        value: 0.5
        from: 0
        to: 1
        height: parent.height - 40
    }

    Slider {
        id: progressSlider
        width: parent.width - 40
        anchors.bottom: parent.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        enabled: mediaPlayer.seekable
        value: mediaPlayer.duration > 0 ? mediaPlayer.position / mediaPlayer.duration : 0

        onMoved: function() {
            mediaPlayer.position = progressSlider.value * mediaPlayer.duration
        }

        background: Rectangle {
            implicitHeight: 8
            color: "lightgray"
            radius: 2
            border.color: "black"
            border.width: 1

            Rectangle {
                width: progressSlider.visualPosition * parent.width
                height: parent.height
                color: "black"
            }
        }
    }

    Item {
        height: 50
        anchors.left: parent.left
        anchors.bottom: parent.bottom
        anchors.margins: 20

        Button {
            anchors.horizontalCenter: parent.horizontalCenter
            text: mediaPlayer.playbackState === MediaPlayer.PlayingState ? "Pause" : "Play"
            font.pixelSize: 15
            font.bold: true
            onClicked: mediaPlayer.playbackState === MediaPlayer.PlayingState ? mediaPlayer.pause() : mediaPlayer.play()
        }
    }

    Component.onCompleted: {
        mediaPlayer.play()
    }
}
