import QtQuick

Window {
    width: 640
    height: 480
    visible: true
    title: "Color SequentialAnimation in QtQuick"

    Rectangle {
        id: background
        anchors.fill: parent
        color: "blue"

        SequentialAnimation on color {
            ColorAnimation {to: "yellow"; duration: 1000}
            ColorAnimation {to: "red"; duration: 1000}
            ColorAnimation {to: "blue"; duration: 1000}
            loops: Animation.Infinite
        }
    }
}
