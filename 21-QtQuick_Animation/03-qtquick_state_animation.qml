import QtQuick

Window {
    width: 640
    height: 480
    visible: true
    title: "QtQuick State Animation"

    Rectangle {
        id: background
        anchors.fill: parent

        state: "RELEASED"
        states: [
            State {
                name: "PRESSED"
                PropertyChanges {
                    target: background
                    color: "blue"
                }
            },
            State {
                name: "RELEASED"
                PropertyChanges {
                    target: background
                    color: "red"
                }
            }
        ]

        MouseArea {
            anchors.fill: parent
            onPressed: background.state = "PRESSED"
            onReleased: background.state = "RELEASED"
        }

        transitions: [
            Transition {
                from: "PRESSED"
                to: "RELEASED"
                ColorAnimation {
                    target: background
                    duration: 400
                }
            },

            Transition {
                from: "RELEASED"
                to: "PRESSED"
                ColorAnimation {
                    target: background
                    duration: 400
                }
            }
        ]
    }
}
