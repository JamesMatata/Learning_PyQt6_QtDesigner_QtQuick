import QtQuick.Controls
import QtQuick.Layouts
import QtQuick

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "QtQuick Control DialogButton"

    DialogButtonBox {
        standardButtons: DialogButtonBox.Ok | DialogButtonBox.Cancel
        onAccepted: {
            console.log("Accepted")
        }
        onRejected: {
            console.log("Rejected")
        }
    }
}