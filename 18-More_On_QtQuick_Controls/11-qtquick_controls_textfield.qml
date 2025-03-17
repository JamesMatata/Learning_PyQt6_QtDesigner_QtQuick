import QtQuick.Controls
import QtQuick.Layouts
import QtQuick

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "QtQuick Control TextField"

    TextField {
        anchors.centerIn: parent
        placeholderText: "Enter your name"

        background: Rectangle {
            color: "lightgray"
            radius: 2
            width: 200
            border.color: control.enabled ? "black" : "gray"
            border.width: 1
        }
    }
}