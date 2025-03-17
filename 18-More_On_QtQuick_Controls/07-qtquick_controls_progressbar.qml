import QtQuick.Controls
import QtQuick

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "QtQuick Control ProgressBar"

    Column {
        anchors.centerIn: parent

        ProgressBar {
            value: 0.5
            id: control

            background: Rectangle {
                implicitWidth: 300
                implicitHeight: 20
                color: "lightgray"
                radius: 2
                border.color: "black"
                border.width: 1
            }

            contentItem: Item {
                implicitWidth: 300
                implicitHeight: 16

                Rectangle {
                    width: control.visualPosition * parent.width
                    height: parent.height
                    radius: 2
                    color: "black"
                }
            }
        }
    }
}