import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "QtQuick control PopupMenu"

    Button {
        id: fileButton
        text: "File"
        onClicked: menu.open()
    }

    Menu {
        id: menu
        y: fileButton.height
        
        MenuItem {text: "New"}
        MenuItem {text: "Open"}
        MenuItem {text: "Save"}
    }
}
