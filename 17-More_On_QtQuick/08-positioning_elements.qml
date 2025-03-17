import QtQuick

Window {
    width: 640
    height: 480
    title: "QtQuick Element Positioning"
    visible: true
    color: 'lightblue'

    // Columns
    // Grids
    // Rows
    // Flow

    Row {
        spacing: 10
        anchors.centerIn: parent

        Rectangle {
            width: 100
            height: 100
            color: 'red'
        }

        Rectangle {
            width: 100
            height: 100
            color: 'green'
        }

        Rectangle {
            width: 100
            height: 100
            color: 'yellow'
        }

        Rectangle {
            width: 100
            height: 100
            color: 'blue'
        }
    }

}