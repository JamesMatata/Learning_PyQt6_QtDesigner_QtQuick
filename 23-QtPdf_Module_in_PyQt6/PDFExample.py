import sys
import os
from PyQt6.QtWidgets import QApplication
from PyQt6.QtPdf import QPdfDocument
from PyQt6.QtPdfWidgets import QPdfView

class PDFViewer(QApplication):
    def __init__(self, file_path):
        super().__init__(sys.argv)

        self.file_path = file_path

        self.document = QPdfDocument(None)
        
        self.view = QPdfView(None)

    def setup_ui(self):
        self.document.load(self.file_path)

        self.view.setPageMode(QPdfView.PageMode.MultiPage)
        self.view.setDocument(self.document)

        self.view.show()

        self.exec()


if __name__ == '__main__':
    file_path = '23-QtPdf_Module_in_PyQt6/pdf.pdf'
    app = PDFViewer(file_path)
    app.setup_ui()