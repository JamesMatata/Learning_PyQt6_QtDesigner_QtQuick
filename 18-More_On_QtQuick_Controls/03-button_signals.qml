import QtQuick.Controls
import QtQuick

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "QtQuick Buttons Signals"

    Column {
        anchors.centerIn: parent
        spacing: 20

        Button {
            id: control
            text: "Click Me"
            anchors.horizontalCenter: parent.horizontalCenter

            // Button clicked
            onClicked: {
                label.text = "Button Clicked"
                label.color = "green"
            }

            // Button pressed down
            onPressed: {
                label.text = "Button Pressed"
                label.color = "blue"
            }

            // Button released after being pressed
            onReleased: {
                label.text = "Button Released"
                label.color = "purple"
            }

            // Mouse hovered over button
            onHoveredChanged: {
                if (hovered) {
                    label.text = "Mouse Hovering"
                    label.color = "orange"
                } else {
                    label.text = "Click Me"
                    label.color = "black"
                }
            }

            // Button enabled/disabled state
            onEnabledChanged: {
                if (enabled) {
                    label.text = "Button Enabled"
                    label.color = "black"
                } else {
                    label.text = "Button Disabled"
                    label.color = "gray"
                }
            }

            contentItem: Text {
                text: control.text
                font: control.font
                opacity: enabled ? 1.0 : 0.3
                color: control.down ? "red" : "green"
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
            }

            background: Rectangle {
                implicitWidth: 100
                implicitHeight: 40
                opacity: enabled ? 1.0 : 0.3
                border.color: control.down ? "red" : "green"
                border.width: 2
                radius: 2
            }
        }

        Label {
            id: label
            text: "------[]--[]------"
            font.pixelSize: 20
            anchors.horizontalCenter: parent.horizontalCenter
        }
    }
}