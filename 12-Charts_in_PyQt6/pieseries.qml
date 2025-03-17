import QtQuick 2.5
import QtQuick.Controls 2.5
import QtCharts 2.5

ApplicationWindow {
    visible:true
    width:600
    height:400
    title:"Creating PieChart"

    ChartView {
        anchors.fill: parent
        antialiasing: true
        theme: ChartView.ChartThemeDark
        
        PieSeries {
            id: myseries
            PieSlice {label: "Mangoes"; value: 90}
            PieSlice {label: "Bananas"; value: 40}
            PieSlice {label: "Oranges"; value: 30}
            PieSlice {label: "Apples"; value: 50}
        }
    }
}