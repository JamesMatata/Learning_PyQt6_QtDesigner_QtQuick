import QtQuick
import QtQuick3D

Window {
    width: 640
    height: 480
    visible: true
    title: "QtQuick3D Basic Scene"

    View3D {
        anchors.fill: parent

        environment: SceneEnvironment {
            clearColor: "#222222"
            backgroundMode: SceneEnvironment.Color
        }
    }
}
