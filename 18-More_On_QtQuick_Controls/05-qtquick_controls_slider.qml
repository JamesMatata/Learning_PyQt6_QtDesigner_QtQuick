import QtQuick.Controls
import QtQuick

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "QtQuick Control Slider"

    Column {
        anchors.centerIn: parent

        Slider {
            from: 1
            value: 25
            to: 100
            id: control

            background: Rectangle {
                x: control.leftPadding
                y: control.topPadding + control.availableHeight / 2 - height / 2
                implicitWidth: 300
                implicitHeight: 4

                width: control.availableWidth
                height: implicitHeight

                color: "gray"
                border.color: "blue"
                border.width: 1
                radius: 1

                Rectangle {
                    width: control.visualPosition * parent.width
                    height: parent.height
                    color: "red"
                    radius: 1
                }
            }

            handle: Rectangle {
                x: control.leftPadding + control.visualPosition * (control.availableWidth - width / 2)
                y: control.topPadding + control.availableHeight / 2 - height / 2
                implicitWidth: 26
                implicitHeight: 26
                color: control.pressed ? "blue" : "black"
                radius: 13
            }
        }
    }
}