from PyQt6.QtWidgets import QMainWindow, QDialog, QMessageBox, QTableWidgetItem, QAbstractItemView
from PyQt6.QtSql import QSqlDatabase,QSqlQuery
from PyQt6.QtCore import Qt

import sys

from main_UI import Ui_MainWindow
from add_book import Add_Book_Dialog
from add_member import Add_Member_Dialog
from view_books import View_Books_Dialog
from view_members import View_Members_Dialog
from renew_issue import Renew_Issue_Dialog

class LibrarySystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.show()

        self.tool_button_add_book.clicked.connect(self.add_book)
        self.tool_button_add_member.clicked.connect(self.add_member)
        self.tool_button_view_books.clicked.connect(self.view_books)
        self.tool_button_view_members.clicked.connect(self.view_members)

        self.issue_book_button.clicked.connect(self.add_book_issue)

        self.book_id_input.textChanged.connect(lambda: self.check_book(self.book_id_input.text()))
        self.member_id_input.textChanged.connect(lambda: self.check_member(self.member_id_input.text()))

        self.book_exists_checkbox.stateChanged.connect(self.enable_issue_button)
        self.member_exists_checkbox.stateChanged.connect(self.enable_issue_button)

        self.submit_or_renew_book_id_input.textChanged.connect(self.filter_book_issues)

        self.issued_books_info.itemSelectionChanged.connect(self.enable_submit_and_renew_buttons)

        self.submit_book_button.clicked.connect(self.submit_book)
        self.renew_book_button.clicked.connect(self.renew_book_issue)

        self.create_books_db()
        self.create_members_db()
        self.create_books_issue_db()
        self.display_book_issues()

    def add_book(self):
        dialog = QDialog()
        ui = Add_Book_Dialog()

        ui.setupUi(dialog)
        dialog.exec()

    def add_member(self):
        dialog = QDialog()
        ui = Add_Member_Dialog()

        ui.setupUi(dialog)
        dialog.exec()

    def view_books(self):
        dialog = QDialog()
        ui = View_Books_Dialog()

        ui.setupUi(dialog)
        dialog.exec()

    def view_members(self):
        dialog = QDialog()
        ui = View_Members_Dialog()

        ui.setupUi(dialog)
        dialog.exec()

    def create_books_db(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('library.db')

        if not db.open():
            QMessageBox.critical(None, "Database Error:", db.lastError().text())
            sys.exit(1)

        query = QSqlQuery()
        create_table = """
            CREATE TABLE IF NOT EXISTS books(
                id TEXT PRIMARY KEY UNIQUE NOT NULL,
                name TEXT NOT NULL,
                author TEXT NOT NULL,
                publisher TEXT NOT NULL,
                availability BOOLEAN NOT NULL DEFAULT 1
            )
        """
        if not query.exec(create_table):
            QMessageBox.critical(None, "Error creating Table:", query.lastError().text())
            sys.exit(1)

        db.close()

    def create_members_db(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('library.db')  

        if not db.open():
            QMessageBox.critical(None, "Database Error:", db.lastError().text())
            print(db.lastError().text())
            sys.exit(1)

        query = QSqlQuery()
        create_table = """
            CREATE TABLE IF NOT EXISTS members(
                id TEXT PRIMARY KEY UNIQUE NOT NULL,
                full_name TEXT NOT NULL,
                phone_number TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """
        query.exec(create_table)

        if not query.exec(create_table):
            QMessageBox.critical(None, "Error creating Table:", query.lastError().text())
            sys.exit(1)

        db.close()

    def create_books_issue_db(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('library.db')  

        if not db.open():
            QMessageBox.critical(None, "Database Error:", db.lastError().text())
            sys.exit(1)

        query = QSqlQuery()
        create_table = """
            CREATE TABLE IF NOT EXISTS book_issues(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                member_id TEXT NOT NULL,
                book_id TEXT NOT NULL,
                return_date TEXT NOT NULL,
                return_time TEXT NOT NULL,
                renew_counts TEXT NOT NULL DEFAULT 0,
                returned BOOLEAN NOT NULL DEFAULT 0
            )
        """
        query.exec(create_table)

        if not query.exec(create_table):
            QMessageBox.critical(None, "Error creating Table:", query.lastError().text())
            sys.exit(1)

        db.close()

    def add_book_issue(self):
        db = QSqlDatabase.database()
        if not db.isValid():
            db = QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('library.db')

        if db.open():
            book_id = self.book_id_input.text()
            member_id = self.member_id_input.text()
            return_date = self.return_date.text()
            return_time = self.return_time.text()

            if book_id and member_id and return_date and return_time:
                query = QSqlQuery()
                insert_book_issue_query = "INSERT INTO book_issues(book_id, member_id, return_date, return_time) VALUES(:book_id, :member_id, :return_date, :return_time)"
                query.prepare(insert_book_issue_query)
                query.bindValue(':book_id', book_id)
                query.bindValue(':member_id', member_id)
                query.bindValue(':return_date', return_date)
                query.bindValue(':return_time', return_time)

                if query.exec():
                    self.book_id_input.clear()
                    self.member_id_input.clear()
                    self.return_date.clear()
                    self.return_time.clear()

                else:
                    QMessageBox.critical(None, "Error adding Book Issue:", query.lastError().text())

            else:
                QMessageBox.critical(None, "Database Error:", db.lastError().text())

        else:
            pass

    def check_book(self, book_id):
        db = QSqlDatabase.database()

        if not db.isValid():
            db = QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('library.db')

        if not db.open():
            QMessageBox.critical(None, "Database Error:", db.lastError().text())
            return

        query = QSqlQuery()
        query.prepare("SELECT name, author FROM books WHERE id = :id")
        query.bindValue(":id", book_id)

        if query.exec() and query.next():
                name = query.value(0)
                author = query.value(1)
                self.book_id_input.setStyleSheet("border: 1px solid blue;")
                self.book_name_label.setText(name)
                self.book_author_label.setText(author)
                self.book_exists_checkbox.setChecked(True)
        else:
            self.book_exists_checkbox.setChecked(False)

        db.close()
    
    def check_member(self, member_id):
        db = QSqlDatabase.database()
        if not db.isValid():
            db = QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('library.db')

        if not db.open():
            QMessageBox.critical(None, "Database Error:", db.lastError().text())
            return

        query = QSqlQuery(db)
        query.prepare("SELECT full_name, phone_number FROM members WHERE id = :id")
        query.bindValue(":id", member_id)

        if query.exec() and query.next():
            full_name = query.value(0)
            phone_number = query.value(1)

            self.member_id_input.setStyleSheet("border: 1px solid blue;")
            self.member_name_label.setText(full_name)
            self.contact_info_label.setText(phone_number)
            self.member_exists_checkbox.setChecked(True)
        else:
            self.member_exists_checkbox.setChecked(False)

        db.close()

    def display_book_issues(self):
        db = QSqlDatabase.database()
        if not db.isValid():
            db = QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('library.db')

        if not db.open():
            QMessageBox.critical(None, "Database Error:", db.lastError().text())
            return

        query = QSqlQuery(db)
        query.prepare("SELECT * FROM book_issues WHERE returned = 0")

        if not query.exec():
            QMessageBox.critical(None, "Query execution error:", query.lastError().text())
            db.close()
            return

        self.issued_books_info.setRowCount(0)
        self.issued_books_info.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        row = 0
        while query.next():
            self.issued_books_info.insertRow(row)
            for col in range(6):
                item = QTableWidgetItem(str(query.value(col)))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.issued_books_info.setItem(row, col, item)
            row += 1

        db.close()

    def issue_book(self):
        book_id = self.book_id_input.text().strip()
        member_id = self.member_id_input.text().strip()
        return_date = self.return_date.text().strip()
        return_time = self.return_time.text().strip()

        if not book_id or not member_id or not return_date or not return_time:
            QMessageBox.critical(None, "Empty Fields:", "All fields must be filled")
            return

        db = QSqlDatabase.database()
        if not db.isValid():
            db = QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('library.db')

        if not db.open():
            QMessageBox.critical(None, "Database error:", db.lastError().text())
            return
        
        query = QSqlQuery(db)
        query.prepare("""
            INSERT INTO book_issues (book_id, member_id, return_date, return_time)
            VALUES (:book_id, :member_id, :return_date, :return_time)
        """)
        query.bindValue(':book_id', book_id)
        query.bindValue(':member_id', member_id)
        query.bindValue(':return_date', return_date)
        query.bindValue(':return_time', return_time)

        if query.exec():
            QMessageBox.information(None, "issue Successful:", "Book issue was added successfully")

            self.book_id_input.clear()
            self.member_id_input.clear()
            self.return_date.clear()
            self.return_time.clear()
            self.display_book_issues()
        else:
            QMessageBox.critical(None, "Query execution error:", query.lastError().text())

        db.close()

    def enable_issue_button(self):
        if self.book_exists_checkbox.isChecked() and self.member_exists_checkbox.isChecked():
            self.issue_book_button.setEnabled(True)
        else:
            self.issue_book_button.setEnabled(False)

    def filter_book_issues(self):
        db = QSqlDatabase.database()
        if not db.isValid():
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName("library.db")

        if not db.open():
            QMessageBox.critical(None, "Database Error:", db.lastError().text())
            return

        query = QSqlQuery(db)
        filter_input = self.submit_or_renew_book_id_input.text().strip()
        filter_query = "SELECT * FROM book_issues"

        if filter_input:
            filter_query += " WHERE book_id LIKE :book_id OR member_id LIKE :member_id"
            query.prepare(filter_query)

            query.bindValue(":book_id", f"%{filter_input}%")
            query.bindValue(":member_id", f"%{filter_input}%")
        else:
            query.prepare(filter_query)  # Prepare only if needed

        if not query.exec():
            QMessageBox.critical(None, "Query execution error:", query.lastError().text())
            return

        self.issued_books_info.setRowCount(0)
        self.issued_books_info.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        row = 0
        while query.next():
            self.issued_books_info.insertRow(row)
            for col in range(5):
                item = QTableWidgetItem(str(query.value(col)))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # Centering text
                self.issued_books_info.setItem(row, col, item)
            row += 1

    def enable_submit_and_renew_buttons(self):
        selected_rows = self.issued_books_info.selectionModel().selectedRows()
        self.renew_book_button.setEnabled(bool(selected_rows))
        self.submit_book_button.setEnabled(bool(selected_rows))

    def submit_book(self):
        selected_rows = self.issued_books_info.selectionModel().selectedRows()
        if not selected_rows:
            return

        selected_row = selected_rows[0].row()
        issue_id_item = self.issued_books_info.item(selected_row, 0)  # Get Issue ID column (first column)

        if issue_id_item:
            issue_id = issue_id_item.text()

            db = QSqlDatabase.database()
            if not db.isValid():
                db = QSqlDatabase.addDatabase('QSQLITE')
                db.setDatabaseName('library.db')

            if not db.open():
                QMessageBox.critical(None, "Database Error:", db.lastError().text())
                return

            query = QSqlQuery(db)
            query.prepare("UPDATE book_issues SET returned = 1 WHERE id = :issue_id")
            query.bindValue(":issue_id", issue_id)

            if query.exec():
                self.display_book_issues()
            else:
                QMessageBox.critical(None, "Error updating book return status:", query.lastError().text())

            db.close()

    def renew_book_issue(self):
        selected_rows = self.issued_books_info.selectionModel().selectedRows()
        if not selected_rows:
            return

        selected_row = selected_rows[0].row()
        issue_id_item = self.issued_books_info.item(selected_row, 0)  # Get Issue ID column (first column)

        if issue_id_item:
            issue_id = issue_id_item.text()

            dialog = QDialog()
            ui = Renew_Issue_Dialog()
            ui.setupUi(dialog)

            if dialog.exec() == QDialog.DialogCode.Accepted:
                new_return_datetime = ui.new_return_date_input.dateTime()
                new_return_date = new_return_datetime.toString("dd/MM/yy")
                new_return_time = new_return_datetime.toString("hh:mm AP")

                db = QSqlDatabase.database()
                if not db.open():
                    QMessageBox.critical(None, "Database Error:", db.lastError().text())
                    return

                query = QSqlQuery(db)
                query.prepare("""
                    UPDATE book_issues 
                    SET return_date = :new_date, 
                        return_time = :new_time,
                        renew_counts = renew_counts + 1 
                    WHERE id = :issue_id
                """)
                query.bindValue(":new_date", new_return_date)
                query.bindValue(":new_time", new_return_time)
                query.bindValue(":issue_id", issue_id)

                if query.exec():
                    QMessageBox.information(None, "Renew Successful:", "Book issue renewed successfully!")
                    self.display_book_issues()
                else:
                    QMessageBox.critical(None, "Error renewing book issue:", query.lastError().text())
                    return

                db.close()

                

