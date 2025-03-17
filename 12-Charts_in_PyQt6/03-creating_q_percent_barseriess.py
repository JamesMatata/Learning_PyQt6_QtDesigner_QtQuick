from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCharts import QChart, QChartView, QPercentBarSeries, QBarSet
from PyQt6.QtCore import Qt
import sys

class window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 300)
        self.setWindowTitle("PyQt6 QPercentBarChart")
        self.setWindowIcon(QIcon('images/icon.png'))
        self.setStyleSheet("background-color: white;")

        self.bar_chart()

    def bar_chart(self):
        set0 = QBarSet("Python")
        set1 = QBarSet("Java")
        set2 = QBarSet("C++")
        set3 = QBarSet("C#")
        set4 = QBarSet("JavaScript")

        set0 << 1 << 2 << 3 << 4 << 5 << 6
        set1 << 5 << 0 << 0 << 4 << 0 << 7
        set2 << 4 << 5 << 9 << 7 << 6 << 5
        set3 << 3 << 5 << 8 << 13 << 8 << 5
        set4 << 5 << 6 << 7 << 3 << 4 << 5

        series = QPercentBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)
        series.append(set3)
        series.append(set4)

        chart = QChart()
        chart.addSeries(series)

        chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)
        chart.setTitle("Bar Chart Example")
        chart.setTheme(QChart.ChartTheme.ChartThemeDark)
        chart.createDefaultAxes()

        chart_view = QChartView(chart)

        self.setCentralWidget(chart_view)



app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())