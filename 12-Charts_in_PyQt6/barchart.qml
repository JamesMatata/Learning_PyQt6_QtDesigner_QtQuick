import QtQuick 2.5
import QtQuick.Controls 2.5
import QtCharts 2.5

ApplicationWindow {
    visible:true
    width:600
    height:400
    title:"Creating BarChart"

    ChartView {
        anchors.fill: parent
        antialiasing: true
        theme: ChartView.ChartThemeDark
        legend.visible: true

        BarSeries {
            id:myseries
            axisX: BarCategoryAxis {
                categories: ["2016", "2017", "2018", "2019", "2020", "2021"]
            }
            BarSet {label: "India"; values: [10, 20, 30, 40, 50, 60]}
            BarSet {label: "USA"; values: [20, 30, 40, 50, 60, 70]}
            BarSet {label: "Kenya"; values: [30, 40, 50, 60, 70, 80]}
        }
    }
}