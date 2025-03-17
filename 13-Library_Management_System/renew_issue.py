from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFrame

class Renew_Issue_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 217)
        Dialog.setStyleSheet("""
                QDialog {
                        background-color: #393A3F;
                }
                QDateTimeEdit {
                        padding: 10px;
                        border-radius: 2px;
                        border: 1px solid black;
                        color: black;
                        background-color: white;
                        font-size: 14px;
                }
                #renew_book_issue_button {
                        padding: 10px 20px;
                        color: white;
                        font-size: 14px;
                        border: none;
                        background-color: blue;
                }
                #new_return_date_input::down-button, #new_return_date_input::up-button {
                        width: 20px;
                        background: none;
                        border: none;
                        margin-right: 5px;
                }

                #new_return_date_input::up-arrow {
                        image: url("C:/Users/James Matata/Desktop/CodeWizard/Python_Programming/Learning_Python_GUIs_with_PyQt6/13-Library_Management_System/images/up.png");
                        width: 20px;
                        height: 20px;
                }

                #new_return_date_input::down-arrow {
                        image: url("C:/Users/James Matata/Desktop/CodeWizard/Python_Programming/Learning_Python_GUIs_with_PyQt6/13-Library_Management_System/images/down.png");
                        width: 20px;
                        height: 20px;
                }
        """)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setStyleSheet("font-weight: bold;font-size: 20px;color: white;")
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_5.addWidget(self.label)
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_5.addWidget(line)
        spacerItem = QtWidgets.QSpacerItem(
            20,
            10,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        self.verticalLayout_5.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setStyleSheet("font-size: 14px;color: white;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.new_return_date_input = QtWidgets.QDateTimeEdit(parent=Dialog)
        self.new_return_date_input.setObjectName("new_return_date_input")
        self.verticalLayout_2.addWidget(self.new_return_date_input)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout.addItem(spacerItem1)
        self.renew_book_issue_button = QtWidgets.QPushButton(parent=Dialog)
        self.renew_book_issue_button.setObjectName("renew_book_issue_button")
        self.renew_book_issue_button.clicked.connect(Dialog.accept)
        self.horizontalLayout.addWidget(self.renew_book_issue_button)
        spacerItem2 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout_5.addItem(spacerItem3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Renew Book Issue"))
        self.label_4.setText(_translate("Dialog", "New Return Date and Time:"))
        self.renew_book_issue_button.setText(_translate("Dialog", "Renew Issue"))
