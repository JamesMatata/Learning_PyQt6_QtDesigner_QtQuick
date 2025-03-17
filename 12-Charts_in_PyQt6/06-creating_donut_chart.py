from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCharts import QChart, QChartView, QPieSeries
import sys

class window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 600, 500)
        self.setWindowTitle("PyQt6 LineChart & BarChart")
        self.setWindowIcon(QIcon('images/icon.png'))
        self.setStyleSheet("background-color: white;")

        series = QPieSeries()
        series.setHoleSize(0.30)

        series.append("Protein 4.3 %", 4.3)

        my_slice = series.append("Fat 15.6 %", 15.6)
        my_slice.setExploded(True)

        series.append("Carbs 23.5 %", 23.5)
        series.append("Fiber 3.7 %", 3.7)
        series.append("Sugar 7.3 %", 7.3)
        series.append("Water 55.6 %", 45.6)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Donut Chart Example")

        chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
        chart.setTheme(QChart.ChartTheme.ChartThemeDark)

        chart_view = QChartView(chart)

        self.setCentralWidget(chart_view)
        
app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())