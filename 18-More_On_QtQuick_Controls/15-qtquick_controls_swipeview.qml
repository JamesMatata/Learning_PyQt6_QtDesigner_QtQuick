import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "QtQuick Control SwipeView"

    SwipeView {
        id: view
        currentIndex: 0
        anchors.fill: parent

        Item {
            id: firstPage

            Rectangle {
                color: "blue"
                anchors.fill: parent
            }

            Label {
                text: "First Page"
                anchors.centerIn: parent
                font.pixelSize: 24
            }
        }

        Item {
            id: secondPage

            Rectangle {
                color: "green"
                anchors.fill: parent
            }

            Label {
                text: "Second Page"
                anchors.centerIn: parent
                font.pixelSize: 24
            }
        }

        Item {
            id: thirdPage

            Rectangle {
                color: "red"
                anchors.fill: parent
            }

            Label {
                text: "Third Page"
                anchors.centerIn: parent
                font.pixelSize: 24
            }
        }
    }

    PageIndicator {
        id: indicator
        count: view.count
        currentIndex: view.currentIndex
        anchors.bottom: view.bottom
        anchors.horizontalCenter: view.horizontalCenter
    }
}
