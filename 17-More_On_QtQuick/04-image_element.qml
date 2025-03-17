import QtQuick

Window {
    width: 640
    height: 480
    title: "QtQuick Image Element"
    visible: true
    color: 'lightblue'

    Image {
        id: img1
        source: "icon.png"
        x: 10
        y: 10
        width: 200
        height: 200
    }
}