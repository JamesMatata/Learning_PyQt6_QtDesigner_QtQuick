from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCharts import QChart, QChartView, QLineSeries
from PyQt6.QtCore import QPointF
import sys

class window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 300)
        self.setWindowTitle("PyQt6 LineChart")
        self.setWindowIcon(QIcon('images/icon.png'))
        self.setStyleSheet("background-color: white;")

        self.line_chart()

    def line_chart(self):
        series = QLineSeries()

        series.append([
            QPointF(0.0, 6.3),
            QPointF(2.0, 4.0),
            QPointF(3.0, 8.21),
            QPointF(7.02, 4.0),
            QPointF(10.3, 5.12)
        ])

        chart = QChart()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setTitle("Line Chart Example")
        chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)

        chart.setTheme(QChart.ChartTheme.ChartThemeDark)

        chartview = QChartView(chart)
        self.setCentralWidget(chartview)




app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())