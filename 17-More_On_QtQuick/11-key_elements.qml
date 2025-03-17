import QtQuick

Window {
    width: 640
    height: 480
    title: "QtQuick Key Element"
    visible: true
    color: 'lightblue'

    Rectangle {
        id: rectangle
        x: 40
        y: 10
        width: 100
        height: 100
        color: 'red'
        border.color: 'black'
        border.width: 1

        focus: true

        Keys.onUpPressed: {
            rectangle.y -= 10
        }

        Keys.onDownPressed: {
            rectangle.y += 10
        }

        Keys.onLeftPressed: {
            rectangle.x -= 10
        }

        Keys.onRightPressed: {
            rectangle.x += 10
        }
    }
}