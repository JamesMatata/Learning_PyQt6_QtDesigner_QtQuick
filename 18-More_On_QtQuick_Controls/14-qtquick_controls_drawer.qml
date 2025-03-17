import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "QtQuick Control Drawer"

    Drawer {
        id: drawer
        width: 0.66 * parent.width
        height: parent.height

        Label {
            text: "Welcome to PyQt6 Course"
            anchors.centerIn: parent
            font.pixelSize: 20
            id: content

            transform: Translate {
                x: drawer.position * content.width * 0.33
            }
        }

        background: Rectangle {
            x: parent.width - 2
            width: 2
            height: parent.height
            color: "white"
        }
    }
}
