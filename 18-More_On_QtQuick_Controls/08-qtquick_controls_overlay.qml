import QtQuick.Controls
import QtQuick.Layouts
import QtQuick

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "QtQuick Control OverLay"

    ColumnLayout {
        anchors.centerIn: parent

        Button {
            text: "Click"

            onClicked: popup.open()
        }

        /*
        Popup {
            id: popup
            parent: Overlay.overlay

            width: 200
            height: 200

            x: Math.round((parent.width - width) / 2)
            y: Math.round((parent.height - height) / 2)

            closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutside
        }
        */

        Popup {
            id: popup
            width: 200
            height: 200
            modal: true
            visible: false
            x: Math.round((parent.width - width) / 2)
            y: Math.round((parent.height - height) / 2)

            closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutside

            Overlay.modal: Rectangle {
                color: "black"
                opacity: 0.5
            }
        }
    }
}