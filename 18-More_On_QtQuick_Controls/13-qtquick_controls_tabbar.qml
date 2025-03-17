import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "QtQuick Control TabBar"

    ColumnLayout {
        anchors.fill: parent

        TabBar {
            id: tabBar
            Layout.fillWidth: true

            TabButton { text: "Python" }
            TabButton { text: "C++" }
            TabButton { text: "Java" }
        }

        StackLayout {
            id: stackLayout
            Layout.fillWidth: true
            Layout.fillHeight: true
            currentIndex: tabBar.currentIndex  // ✅ Syncing with TabBar

            Item {
                Rectangle {
                    anchors.fill: parent
                    color: "lightgreen"
                    Text {
                        text: "Python"
                        anchors.centerIn: parent
                    }
                }
            }

            Item {
                Rectangle {
                    anchors.fill: parent
                    color: "lightblue"
                    Text {
                        text: "C++"
                        anchors.centerIn: parent
                    }
                }
            }

            Item {
                Rectangle {
                    anchors.fill: parent
                    color: "lightcoral"
                    Text {
                        text: "Java"
                        anchors.centerIn: parent
                    }
                }
            }
        }
    }
}
