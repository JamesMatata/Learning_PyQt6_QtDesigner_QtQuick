import QtQuick.Controls
import QtQuick

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "QtQuick Control CheckBox"

    Column {
        anchors.centerIn: parent

        CheckBox {
            id: python
            checked: true
            text: "Python"
            font.pixelSize: 16

            onClicked: {
                if (python.checked) {
                    label.text = "Python"
                } else {
                    label.text = "Not Python"
                }
                
            }
        }

        CheckBox {
            id: cplusplus
            checked: false
            text: "C++"
            font.pixelSize: 16

            onClicked: {
                if (cplusplus.checked) {
                    label.text = "C++"
                } else {
                    label.text = "Not C++"
                }
            }
        }

        CheckBox {
            id: java
            checked: false
            text: "Java"
            font.pixelSize: 16

            onClicked: {
                if (java.checked) {
                    label.text = "Java"
                } else {
                    label.text = "Not Java"
                }
            }
        }

        Label {
            id: label
            text: "-----[]--[]-----"
            font.pixelSize: 20
            color: "black"
        }
    }
}