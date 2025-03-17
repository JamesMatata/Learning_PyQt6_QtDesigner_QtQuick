import QtQuick.Controls
import QtQuick.Layouts
import QtQuick

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "QtQuick Control BusyIndicator"

    BusyIndicator {
        anchors.centerIn: parent
        id: indicator
        running: true
    }
}