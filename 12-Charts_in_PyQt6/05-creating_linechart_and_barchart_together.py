from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCharts import QChart, QChartView, QBarSeries, QValueAxis, QBarSet, QLineSeries
from PyQt6.QtCore import Qt, QPointF
import sys

class window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 300)
        self.setWindowTitle("PyQt6 LineChart & BarChart")
        self.setWindowIcon(QIcon('images/icon.png'))
        self.setStyleSheet("background-color: white;")

        set0 = QBarSet("Python")
        set1 = QBarSet("Java")
        set2 = QBarSet("C++")
        set3 = QBarSet("C#")
        set4 = QBarSet("JavaScript")

        set0.append([1, 2, 3, 4, 5, 6])
        set1.append([5, 0, 0, 4, 0, 7])
        set2.append([4, 5, 9, 7, 6, 5])
        set3.append([3, 5, 8, 13, 8, 5])
        set4.append([5, 6, 7, 3, 4, 5])

        bar_series = QBarSeries()
        bar_series.append(set0)
        bar_series.append(set1)
        bar_series.append(set2)
        bar_series.append(set3)
        bar_series.append(set4)

        line_series = QLineSeries()
        line_series.append(QPointF(0, 4))
        line_series.append(QPointF(1, 15))
        line_series.append(QPointF(2, 7))
        line_series.append(QPointF(3, 12))
        line_series.append(QPointF(4, 10))
        line_series.append(QPointF(5, 5))

        chart = QChart()
        chart.addSeries(bar_series)
        chart.addSeries(line_series)
        chart.setTitle("Line Chart & Bar Chart Example")

        chart_view = QChartView(chart)

        self.setCentralWidget(chart_view)

        
app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())