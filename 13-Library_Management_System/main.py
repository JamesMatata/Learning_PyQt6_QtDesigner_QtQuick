import sys
from PyQt6.QtWidgets import QApplication
from library_system import LibrarySystem

app = QApplication(sys.argv)
library = LibrarySystem()
sys.exit( app.exec())