import QtQuick

Window {
    width: 640
    height: 480
    title: "QtQuick TextInput Element"
    visible: true
    color: 'lightblue'

    Rectangle {
        id: rect1
        x: 10
        y: 10
        width: 400
        height: 50
        border.color: 'blue'
        border.width: 1
        radius: 2

        TextInput {
            id: textInput
            text: "Hello, World!"
            color: 'blue'
            font.pixelSize: 20
            x: 20
            padding: 10
            anchors.fill: parent

            onAccepted: {
                textOutput.text = textInput.text
            }
        }
    }

    Text {
        id: textOutput
        text: "---------[]--[]---------"
        color: 'red'
        y: 80
        font.pixelSize: 20
        x: 20
    }
}