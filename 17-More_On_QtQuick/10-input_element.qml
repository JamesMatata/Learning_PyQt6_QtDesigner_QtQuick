import QtQuick

Window {
    width: 640
    height: 480
    title: "QtQuick Input Element"
    visible: true
    color: 'lightblue'

    Column {
        spacing: 10
        width: parent.width

        // TextEdit {
        //     id: input
        //     color: 'black'
        //     width: 200
        //     height: 100
        //     text: "Text Edit"
        // }

        Rectangle {
            width: parent.width
            color: 'white'
            border.color: 'black'
            border.width: 1

            TextEdit {
                id: input
                color: 'black'
                width: parent.width
                height: 400
                text: "Text Input"
                anchors.fill: parent
                focus: true
                anchors.margins: 5
            }
        }
    }
}