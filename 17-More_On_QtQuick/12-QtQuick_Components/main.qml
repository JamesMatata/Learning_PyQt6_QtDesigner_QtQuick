import QtQuick

Window {
    width: 640
    height: 480
    title: "QtQuick Components"
    visible: true
    color: 'lightblue'

    Button {
        id: button
        x: 10; y: 10
        width: 116; height: 26
        text: "Click Me"
        onClicked: {
            status.text = "Button Clicked"
            status.color = 'green'
            status.font.pixelSize = Math.floor(Math.random() * (30 - 16 + 1)) + 16;
        }
    }

    Text {
        id: status
        x: 10; y: 50
        width: 116; height: 26
        text: "-----[ ]--[ ]-----"
        horizontalAlignment: Text.AlignHCenter
    }
}