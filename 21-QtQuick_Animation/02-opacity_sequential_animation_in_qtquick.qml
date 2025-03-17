import QtQuick

Window {
    width: 640
    height: 480
    visible: true
    title: "Opacity SequentialAnimation in QtQuick"

    Rectangle {
        id: background
        anchors.fill: parent
        color: "black"

        Text {
            text: "Welcome to PyQt6 Course"
            font.pixelSize: 40
            anchors.centerIn: parent
            color: "white"

            SequentialAnimation on opacity {
                NumberAnimation {to: 0.0; duration: 500}
                NumberAnimation {to: 1.0; duration: 500}
                loops: Animation.Infinite
            }
        }
    }
}
