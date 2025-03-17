import QtQuick

Window {
    width: 640
    height: 580
    title: "QtQuick Rectangle Element"
    visible: true
    color: 'gray'

    Rectangle {
        id: rect1
        x: 10
        y: 10
        width: 400
        height: 200
        color: 'lightblue'
        border.color: 'blue'
        border.width: 1
        radius: 10
    }
    
    Rectangle {
        id: rect2
        x: 10
        y: 220
        width: 400
        height: 200
        color: 'lightblue'
        border.color: 'blue'
        border.width: 1
        radius: 10
    }

    Rectangle {
        id: rect3
        x: 10
        y: 430
        width: 400
        height: 100
        gradient: Gradient {
            GradientStop { position: 0.0; color: "lightblue" }
            GradientStop { position: 1.0; color: "blue" }
        }
        border.color: 'blue'
        border.width: 1
        radius: 10
    }
}