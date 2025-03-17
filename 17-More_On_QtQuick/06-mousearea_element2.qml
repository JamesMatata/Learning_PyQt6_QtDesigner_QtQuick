import QtQuick

Window {
    width: 640
    height: 480
    title: "QtQuick MouseArea Element"
    visible: true
    color: 'lightblue'

    Rectangle {
        id: button
        x: 10
        y: 10
        width: 116
        height: 26
        color: 'blue'
        border.color: 'black'
        border.width: 1
        radius: 4

        Text {
            id: buttonText
            text: "Change Text"
            color: 'white'
            anchors.centerIn: parent
        }

        MouseArea {
            id: mouseArea
            anchors.fill: parent
            onClicked: {
                status.text = "Button Clicked!"
                status.color = 'red'
            }
        }
    }

    Text {
        id: status
        x: 10
        y: 60
        text: "Hello, World!"
        font.pixelSize: 24
    }
}