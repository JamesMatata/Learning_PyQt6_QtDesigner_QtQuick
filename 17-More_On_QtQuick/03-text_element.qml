import QtQuick

Window {
    width: 640
    height: 480
    title: "QtQuick Text Element"
    visible: true

    Text {
        id: text1
        text: "Welcome to QtQuick Course"
        color: blue
        font.family: "Arial"
        font.pixelSize: 24
        font.bold: true
        x: 10
        y: 50
    }
}