import QtQuick.Controls
import QtQuick.Layouts
import QtQuick

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "QtQuick Control TabButton"

    ColumnLayout {
        TabBar {
            TabButton {
                text: "Python"
                width: 100
                height: 40
                onClicked: {
                    console.log("Python Clicked")
                }
            }
            TabButton {
                text: "C++"
                width: 100
                height: 40
                onClicked: {
                    console.log("C++ Clicked")
                }
            }
            TabButton {
                text: "Java"
                width: 100
                height: 40
                onClicked: {
                    console.log("Java Clicked")
                }
            }
            TabButton {
                text: "JavaScript"
                width: 100
                height: 40
                onClicked: {
                    console.log("JavaScript Clicked")
                }
            }
        }
    }
}