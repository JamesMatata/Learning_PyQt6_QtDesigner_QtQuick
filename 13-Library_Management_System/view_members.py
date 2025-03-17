from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QHeaderView, QMessageBox
from PyQt6.QtSql import QSqlDatabase,QSqlQuery


class View_Members_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(950, 500)
        Dialog.setStyleSheet("""
            #filter_members_input {
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
        self.filter_members_input = QtWidgets.QLineEdit(parent=Dialog)
        self.filter_members_input.setObjectName("filter_members_input")
        self.filter_members_input.textChanged.connect(self.filter_members)
        self.verticalLayout.addWidget(self.filter_members_input)
        self.members_table = QtWidgets.QTableWidget(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.members_table.setFont(font)
        self.members_table.setStyleSheet("QTableWidget {background-color:rgb(218,218,218)}")
        self.members_table.setObjectName("tableWidget")
        self.members_table.setColumnCount(4)
        self.members_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.members_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.members_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.members_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.members_table.setHorizontalHeaderItem(3, item)
        self.members_table.horizontalHeader().setDefaultSectionSize(155)
        self.members_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.members_table.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.members_table)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.load_members_data()

    def load_members_data(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('library.db')

        if not db.open():
            QMessageBox.critical(None, "Database Error", db.lastError().text())
            return

        query = QSqlQuery("SELECT * FROM members")

        self.members_table.setRowCount(0)
        row = 0

        while query.next():
            self.members_table.insertRow(row)
            for col in range(4):
                item = QtWidgets.QTableWidgetItem(query.value(col))
                self.members_table.setItem(row, col, item)
            row += 1

        db.close()

    def filter_members(self):
        filter_input = self.filter_members_input.text()

        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('library.db')

        if not db.open():
            QMessageBox.critical(None, "Database Error", db.lastError().text())
            return
        
        query = QSqlQuery()
        if input:
            query.prepare("SELECT * FROM members WHERE id LIKE ? OR full_name LIKE ?")
            filter_value = f"%{filter_input}%"
            query.addBindValue(filter_value)
            query.addBindValue(filter_value)
        else:
            query.prepare("SELECT * FROM members")

        query.exec()
        self.members_table.setRowCount(0)
        row = 0

        while query.next():
            self.members_table.insertRow(row)
            for col in range(5):
                item = QtWidgets.QTableWidgetItem(str(query.value(col)))
                self.members_table.setItem(row, col, item)
            row += 1

        db.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "View Members"))
        self.filter_members_input.setPlaceholderText(_translate("Dialog", "Type to filter members ...."))
        item = self.members_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID"))
        item = self.members_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Name"))
        item = self.members_table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Mobile"))
        item = self.members_table.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Email"))
