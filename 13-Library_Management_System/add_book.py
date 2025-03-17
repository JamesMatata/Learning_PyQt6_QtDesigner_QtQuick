from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFrame, QMessageBox
from PyQt6.QtSql import QSqlDatabase,QSqlQuery


class Add_Book_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 418)
        Dialog.setStyleSheet("""
                QDialog {
                        background-color: #393A3F;
                }
                QLineEdit {
                        padding: 10px;
                        border-radius: 2px;
                        border: 1px solid black;
                        color: black;
                        background-color: white;
                        font-size: 14px;
                }
                #cancel_book_add, #add_new_book_button {
                        padding: 10px 20px;
                        color: white;
                        font-size: 14px;
                        border: none;
                }
                #add_new_book_button {
                        background-color: blue;
                }
                #cancel_book_add {
                        background-color: red;              
                }
        """)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setStyleSheet("font-weight: bold;font-size: 20px;color: white;")
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_5.addWidget(self.label)
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_5.addWidget(line)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_5.addItem(spacerItem)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setStyleSheet("font-size: 14px;color:white;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.book_title_input = QtWidgets.QLineEdit(parent=Dialog)
        self.book_title_input.setStyleSheet("")
        self.book_title_input.setObjectName("book_title_input")
        self.verticalLayout_4.addWidget(self.book_title_input)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setStyleSheet("font-size: 14px;color:white;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.new_book_id_input = QtWidgets.QLineEdit(parent=Dialog)
        self.new_book_id_input.setObjectName("new_book_id_input")
        self.verticalLayout_3.addWidget(self.new_book_id_input)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setStyleSheet("font-size: 14px;color:white;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.book_author_input = QtWidgets.QLineEdit(parent=Dialog)
        self.book_author_input.setObjectName("book_author_input")
        self.verticalLayout_2.addWidget(self.book_author_input)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setStyleSheet("font-size: 14px;color:white;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.book_publisher_input = QtWidgets.QLineEdit(parent=Dialog)
        self.book_publisher_input.setObjectName("book_publisher_input")
        self.verticalLayout.addWidget(self.book_publisher_input)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.add_new_book_button = QtWidgets.QPushButton(parent=Dialog)
        self.add_new_book_button.setStyleSheet("padding: 10px 20px;color: white;background-color: blue;font-size: 14px;border: none;")
        self.add_new_book_button.setObjectName("add_new_book_button")
        self.add_new_book_button.clicked.connect(self.insert_book)
        self.horizontalLayout.addWidget(self.add_new_book_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def insert_book(self):
        db = QSqlDatabase.database()
        if not db.isValid():
                db = QSqlDatabase.addDatabase('QSQLITE')
                db.setDatabaseName('library.db')

        if db.open():
                id = self.new_book_id_input.text()
                title = self.book_title_input.text()
                author = self.book_author_input.text()
                publisher = self.book_publisher_input.text()

                if not id or not title or not author or not publisher:
                        QMessageBox.critical(None, "Empty Fields:", "All fields must be filled!")
                else:
                        query = QSqlQuery()
                        insert_member_query = "INSERT INTO books(id, name, author, publisher) VALUES(:id, :name, :author, :publisher)"
                        query.prepare(insert_member_query)
                        query.bindValue(':id', id)
                        query.bindValue(':name', title)
                        query.bindValue(':author', author)
                        query.bindValue(':publisher', publisher)

                        if query.exec():
                                self.new_book_id_input.clear()
                                self.book_title_input.clear()
                                self.book_author_input.clear()
                                self.book_publisher_input.clear()
                                QMessageBox.information(None, "Book Added:", "Book added successfully")
                        else:
                                QMessageBox.critical(None, "Error adding Book:", query.lastError().text())
                                return
                              
        else:
             QMessageBox.critical(None, "Database Error:", db.lastError().text())
             return
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Add Book"))
        self.label_2.setText(_translate("Dialog", "Book Title:"))
        self.label_3.setText(_translate("Dialog", "Book ID:"))
        self.label_4.setText(_translate("Dialog", "Book Author:"))
        self.label_5.setText(_translate("Dialog", "Book Publisher:"))
        self.add_new_book_button.setText(_translate("Dialog", "Add Book"))
