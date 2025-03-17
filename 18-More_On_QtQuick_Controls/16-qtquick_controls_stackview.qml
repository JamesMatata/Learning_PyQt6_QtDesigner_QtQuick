import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "QtQuick Control StackView"

    StackView {
        id: stack
        initialItem: mainView
        anchors.fill: parent
    }

    Component {
        id: mainView 

        Row {
            spacing: 10

            Button {
                text: "Push"
                onClicked: stack.push(mainView)
            }

            Button {
                text: "Pop"
                enabled: stack.depth > 1
                onClicked: stack.pop()
            }

            Text {
                text: stack.depth
            }
        }
    }
}
