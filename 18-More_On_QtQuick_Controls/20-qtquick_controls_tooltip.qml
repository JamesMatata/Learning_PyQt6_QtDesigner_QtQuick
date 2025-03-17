import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "QtQuick control Tooltip"

    /*
    Button {
        text: "Save"

        ToolTip.visible: down
        ToolTip.text: "Save the file"   
    }
    */

    Slider {
        value: 0.5
        id: slider
        width: 400

        ToolTip {
            parent: slider.handle
            visible: slider.pressed
            text: slider.value.toFixed(1)

        }
    }
}
