from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QHeaderView, QMessageBox
from PyQt6.QtSql import QSqlDatabase,QSqlQuery


class View_Books_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(950, 500)
        Dialog.setStyleSheet("""
            #filter_book_input {
                padding: 10px;
                font-size: 14px;
                border-radius: 2px;
                border: 1px solid black;
            }
            QTableWidget {
                background-color: white;
                border: 2px solid black;
                gridline-color: white;
            }
            QHeaderView::section {
                background-color: blue;
                color: white;
                font-size: 14px;
                font-weight: bold;
                padding: 6px;
                border: 1px solid white;
                text-align: center;
            }
            QTableWidget::item {
                padding: 8px;
                color: black;
                font-size: 14px;
                border: 1px solid white;
            }
            QTableWidget::item:selected {
                background-color: darkblue;
                color: white;
            }
        """)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.filter_book_input = QtWidgets.QLineEdit(parent=Dialog)
        self.filter_book_input.setObjectName("filter_book_input")
        self.filter_book_input.textChanged.connect(self.filter_books)
        self.verticalLayout.addWidget(self.filter_book_input)
        self.books_table = QtWidgets.QTableWidget(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.books_table.setFont(font)
        self.books_table.setStyleSheet("QTableWidget {background-color:rgb(218,218,218)}")
        self.books_table.setObjectName("books_table")
        self.books_table.setColumnCount(5)
        self.books_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.books_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.books_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.books_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.books_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.books_table.setHorizontalHeaderItem(4, item)
        self.books_table.horizontalHeader().setDefaultSectionSize(130)
        self.books_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.books_table.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.books_table)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.load_books_data()

    def load_books_data(self):
        db = QSqlDatabase.database()  # Use existing database connection
        db.setDatabaseName('library.db')

        if not db.open():
            QMessageBox.critical(None, "Database Error", db.lastError().text())
            return 

        query = QSqlQuery("SELECT * FROM books")

        self.books_table.setRowCount(0)
        row = 0

        while query.next():
            self.books_table.insertRow(row)
            for col in range(5):
                if col == 4:
                    available = "Yes" if query.value(col) == 1 else "No"
                    item = QtWidgets.QTableWidgetItem(available)
                else:
                    item = QtWidgets.QTableWidgetItem(str(query.value(col)))
                
                self.books_table.setItem(row, col, item)
            row += 1

        db.close()

    def filter_books(self):
        filter_input = self.filter_book_input.text()

        db = QSqlDatabase.database()
        db.setDatabaseName('library.db')

        if not db.open():
            QMessageBox.critical(None, "Database Error", db.lastError().text())
            return
        
        query = QSqlQuery()
        if filter_input:
            query.prepare("SELECT * FROM books WHERE id LIKE ? OR name LIKE ?")
            filter_value = f"%{filter_input}%"
            query.addBindValue(filter_value)
            query.addBindValue(filter_value)
        else:
            query.prepare("SELECT * FROM books")
        query.exec()

        self.books_table.setRowCount(0)
        row = 0

        while query.next():
            self.books_table.insertRow(row)
            for col in range(5):
                if col == 4:
                    available = "Yes" if query.value(col) == 1 else "No"
                    item = QtWidgets.QTableWidgetItem(available)
                else:
                    item = QtWidgets.QTableWidgetItem(str(query.value(col)))
                
                self.books_table.setItem(row, col, item)
            row += 1

        db.close()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "View Books"))
        self.filter_book_input.setPlaceholderText(_translate("Dialog", "Type to filter books ......."))
        item = self.books_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Title"))
        item = self.books_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "ID"))
        item = self.books_table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Author"))
        item = self.books_table.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Publisher"))
        item = self.books_table.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Available"))
