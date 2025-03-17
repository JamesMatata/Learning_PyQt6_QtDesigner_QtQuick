from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCharts import QChart, QChartView, QStackedBarSeries, QValueAxis, QBarSet, QBarCategoryAxis
from PyQt6.QtCore import Qt
import sys

class window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 300)
        self.setWindowTitle("PyQt6 QStackedBarChart")
        self.setWindowIcon(QIcon('images/icon.png'))
        self.setStyleSheet("background-color: white;")

        low = QBarSet("Min")
        high = QBarSet("Max")

        low.append([-52, -50, -45.3, -37.0, -25.6, -8.0,
             -6.0, -11.8, -19.7, -32.8, -43.0, -48.0])
        high.append([11.9, 12.8, 18.2, 26.7, 32.0, 34.8,
            38.0, 37.0, 31.3, 23.0, 16.0, 12.0])

        series = QStackedBarSeries()
        series.append(low)
        series.append(high)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Temperature Record in Celcius")

        categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                      "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        
        axis_x = QBarCategoryAxis()
        axis_x.append(categories)
        axis_x.setTitleText("Months")

        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)

        axis_y = QValueAxis()
        axis_y.setRange(-52,52)
        axis_y.setTitleText("Temperature [&deg;c]")

        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        series.attachAxis(axis_x)
        series.attachAxis(axis_y)

        chart_view = QChartView(chart)

        self.setCentralWidget(chart_view)


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())