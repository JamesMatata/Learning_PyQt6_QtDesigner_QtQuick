import QtQuick

Window {
    width: 640
    height: 480
    title: "QtQuick Anchors"
    visible: true
    color: 'lightblue'

    Rectangle {
        id: redRect
        width: 100
        height: 100
        color: 'red'
        // anchors.centerIn: parent
        // anchors.margins: 10

        // Left anchors
        // anchors.left: parent.left
        // anchors.leftMargin: 10

        // Right anchors
        // anchors.right: parent.right
        // anchors.rightMargin: 10

        anchors.horizontalCenter: parent.horizontalCenter
        // anchors.verticalCenter: parent.verticalCenter
    }

    Rectangle {
        id: greenRect
        width: 100
        height: 100
        color: 'green'
        anchors.top: redRect.bottom
        anchors.topMargin: 10
        anchors.horizontalCenter: parent.horizontalCenter
    }

    Rectangle {

    }
}