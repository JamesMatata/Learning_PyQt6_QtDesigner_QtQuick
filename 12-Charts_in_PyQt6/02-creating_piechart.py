from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCharts import QChart, QChartView, QPieSeries
from PyQt6.QtCore import Qt
import sys

class window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 300)
        self.setWindowTitle("PyQt6 PieChart")
        self.setWindowIcon(QIcon('images/icon.png'))
        self.setStyleSheet("background-color: white;")

        self.pie_chart()

    def pie_chart(self):
        series = QPieSeries()

        series.append("Python", 80)
        series.append("Java", 50)
        series.append("C++", 40)
        series.append("C#", 30)
        series.append("JavaScript", 20)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Pie Chart Example")
        chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)

        chart.setTheme(QChart.ChartTheme.ChartThemeBlueCerulean)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)

        # Add Slice
        my_slice = series.slices()[2]
        my_slice.setExploded(True)
        my_slice.setLabelVisible(True)

        chart_view = QChartView(chart)

        self.setCentralWidget(chart_view)


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())