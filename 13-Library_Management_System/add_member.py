from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFrame, QLabel, QMessageBox
from PyQt6.QtSql import QSqlDatabase,QSqlQuery


class Add_Member_Dialog(object):
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
                #cancel_member_add, #add_new_member_button {
                        padding: 10px 20px;
                        color: white;
                        font-size: 14px;
                        border: none;
                }
                #add_new_member_button {
                        background-color: blue;
                }
                #cancel_member_add {
                        background-color: red;
                }""")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setStyleSheet("font-weight: bold;font-size: 20px;color:white;")
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
        self.label_2.setStyleSheet("font-size: 14px;color: white;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.new_member_full_name = QtWidgets.QLineEdit(parent=Dialog)
        self.new_member_full_name.setStyleSheet("")
        self.new_member_full_name.setObjectName("new_member_full_name")
        self.verticalLayout_4.addWidget(self.new_member_full_name)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setStyleSheet("font-size: 14px;color: white;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.new_member_id = QtWidgets.QLineEdit(parent=Dialog)
        self.new_member_id.setObjectName("new_member_id")
        self.verticalLayout_3.addWidget(self.new_member_id)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setStyleSheet("font-size: 14px;color: white;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.new_member_number = QtWidgets.QLineEdit(parent=Dialog)
        self.new_member_number.setObjectName("new_member_number")
        self.verticalLayout_2.addWidget(self.new_member_number)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setStyleSheet("font-size: 14px;color: white;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.new_member_email = QtWidgets.QLineEdit(parent=Dialog)
        self.new_member_email.setObjectName("new_member_email")
        self.verticalLayout.addWidget(self.new_member_email)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.add_new_member_button = QtWidgets.QPushButton(parent=Dialog)
        self.add_new_member_button.setStyleSheet("padding: 10px 20px;color: white;background-color: blue;font-size: 14px;border: none;")
        self.add_new_member_button.setObjectName("add_new_member_button")
        self.add_new_member_button.clicked.connect(self.insert_member)
        self.horizontalLayout.addWidget(self.add_new_member_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def insert_member(self):
        db = QSqlDatabase.database()
        if not db.isValid():
                db = QSqlDatabase.addDatabase('QSQLITE')
                db.setDatabaseName('library.db')

        if db.open():
                id = self.new_member_id.text()
                full_name = self.new_member_full_name.text()
                phone_number = self.new_member_number.text()
                email = self.new_member_email.text()

                if not id or not full_name or not phone_number or not email:
                        QMessageBox.critical(None, "Empty Fields:", "All fields must be filled!")
                else:
                        query = QSqlQuery()
                        insert_member_query = "INSERT INTO members(id,full_name,phone_number,email) VALUES(:id,:full_name,:phone_number,:email)"
                        query.prepare(insert_member_query)
                        query.bindValue(':id', id)
                        query.bindValue(':full_name', full_name)
                        query.bindValue(':phone_number', phone_number)
                        query.bindValue(':email', email)

                        if query.exec():
                                self.new_member_id.clear()
                                self.new_member_full_name.clear()
                                self.new_member_number.clear()
                                self.new_member_email.clear()
                                QMessageBox.information(None, "Member Added:", "Member added successfully")
                        else:
                                QMessageBox.critical(None, "Error adding Member:", query.lastError().text())
                                return
                              
        else:
             QMessageBox.critical(None, "Database Error:", db.lastError().text())
             return 

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Add Member"))
        self.label_2.setText(_translate("Dialog", "Member Full Name:"))
        self.label_3.setText(_translate("Dialog", "Member ID:"))
        self.label_4.setText(_translate("Dialog", "Member Mobile Number:"))
        self.label_5.setText(_translate("Dialog", "Member Email:"))
        self.add_new_member_button.setText(_translate("Dialog", "Add Member"))
