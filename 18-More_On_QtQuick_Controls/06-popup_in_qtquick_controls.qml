import QtQuick.Controls
import QtQuick

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "QtQuick Control Pop-Up"

    Button {
        text: "Open"
        onClicked: popup.open()
    }

    Popup {
        id: popup
        x: 100
        y: 100
        width: 200
        height: 200
        modal: true
        focus: true
        closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutside

        contentItem: Text {
            text: "Python PyQt6"
        }

        background: BorderImage {
            source: 'icon.png'
            opacity: 0.5
        }
    }
}