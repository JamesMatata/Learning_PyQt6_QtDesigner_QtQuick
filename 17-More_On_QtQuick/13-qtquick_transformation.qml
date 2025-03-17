import QtQuick

Window {
    width: 640
    height: 480
    title: "QtQuick Transformation"
    visible: true
    color: 'lightblue'

    Shape {
        id: circle
        x: 84; y: 68
        source: "circle.png"
        onClicked: {
            x+=20
        }
    }

    Shape {
        id: rect
        x: 284; y: 268
        source: "rectangle.png"
        onClicked: {
            rotation += 15
            scale += 0.1
        }
    }
}