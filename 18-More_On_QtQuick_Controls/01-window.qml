import QtQuick.Controls
import QtQuick
ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "QtQuick Window"
    background: Rectangle {
        gradient: Gradient {
            GradientStop { position: 0.0; color: "lightblue" }
            GradientStop { position: 1.0; color: "white" }
        }
    }
}