import QtQuick

Window {
    width: 640
    height: 480
    title: "QtQuick MouseArea Element"
    visible: true
    color: 'lightblue'

    Rectangle {
        id: rect1
        x: 10
        y: 10
        width: 400
        height: 200
        color: 'blue'
        border.color: 'black'
        border.width: 1
        radius: 5

        MouseArea {
            id: mouseArea1
            anchors.fill: parent
            onClicked: {
                console.log("Rect1 MouseArea clicked")
                rect2.visible = !rect2.visible
            }
        }
    }

    Rectangle {
        id: rect2
        x: 10
        y: 220
        width: 400
        height: 200
        color: 'blue'
        border.color: 'black'
        border.width: 1
        radius: 5

        MouseArea {
            id: mouseArea2
            anchors.fill: parent
            onClicked: {
                console.log("Rect2 MouseArea clicked")
                rect1.visible = !rect1.visible
            }
        }
    }
}