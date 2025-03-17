import QtQuick 2.5
import QtQuick.Controls 2.5
import QtCharts 2.5

ApplicationWindow {
    visible:true
    width:600
    height:400
    title:"Creating LineChart"

    ChartView {
        anchors.fill: parent
        antialiasing: true
        theme: ChartView.ChartThemeDark
        legend.visible: true

        LineSeries {
            name: "LineSeries"
            XYPoint { x: 0; y: 0 }
            XYPoint { x: 1; y: 1 }
            XYPoint { x: 2; y: 2 }
            XYPoint { x: 3; y: 3 }
            XYPoint { x: 4; y: 4 }
            XYPoint { x: 5; y: 5 }
        }
    }

}