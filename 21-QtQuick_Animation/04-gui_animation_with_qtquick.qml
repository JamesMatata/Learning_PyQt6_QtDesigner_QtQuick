import QtQuick

Window {
    width: 640
    height: 480
    visible: true
    title: "GUI Animation with QtQuick"

    Rectangle {
        id: my_box
        width: 50
        height: 50
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        color: "red"

        ScaleAnimator {
            target: my_box
            from: 5
            to: 1
            duration: 2000
            running: true
        }

        ParallelAnimation {
            ScaleAnimator {
                target: my_box
                from: 5
                to: 1
                duration: 2000
            }

            RotationAnimator {
                target: my_box
                from: 0
                to: 360
                duration: 1000
            }

            running: true
        }
    }
}
