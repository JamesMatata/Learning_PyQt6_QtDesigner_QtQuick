import QtQuick 2.5
import QtQuick.Controls 2.5
import QtCharts 2.5

ApplicationWindow {
    visible:true
    width:600
    height:400
    title:"Creating ScatterChart"

    ChartView {
        anchors.fill: parent
        antialiasing: true
        theme: ChartView.ChartThemeDark

        ScatterSeries {
            id: scatterseries1
            name: "ScatterSeries 1"
            XYPoint { x: 1.5; y: 1.5 }
            XYPoint { x: 2.2; y: 1.6 }
            XYPoint { x: 1.8; y: 1.55 }
            XYPoint { x: 1.57; y: 1.6 }
            XYPoint { x: 1.8; y: 1.2 }
            XYPoint { x: 2.5; y: 1.5 }
        }

        ScatterSeries {
            id: scatterseries2
            name: "ScatterSeries 2"
            XYPoint { x: 2.8; y: 1.7 }
            XYPoint { x: 1.6; y: 1.1 }
            XYPoint { x: 1.5; y: 2.5 }
            XYPoint { x: 2.57; y: 1.6 }
            XYPoint { x: 2.0; y: 1.43 }
            XYPoint { x: 1.9; y: 2.4 }
        }
    }
}