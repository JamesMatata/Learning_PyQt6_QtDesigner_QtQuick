import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "QtQuick Frame"

    Frame {
        ColumnLayout {
            anchors.fill: parent
            
            CheckBox {text: "Email"}
            CheckBox {text: "Phone"}
            CheckBox {text: "Address"}
            CheckBox {text: "Name"}
        }
    }
}
