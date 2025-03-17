
from PyQt6.QtWidgets import QHeaderView, QFrame, QCheckBox
from PyQt6.QtSql import QSqlDatabase,QSqlQuery
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QAbstractItemView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(QtCore.QSize(920, 590))
        MainWindow.showMaximized()
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(
                """
                QMainWindow {
                        background-color: #393A3F;
                }                

                QToolButton {
                        padding: 10px;
                        background-color: #75767B;
                        border-radius: 4px;
                        border: none;
                        color: white;
                }

                QTabWidget::pane {
                        border: 1px solid gray;
                        background: #75767B;
                        border-radius: 4px;
                }

                QTabBar::tab {
                        background: gray;
                        color: black;
                        padding: 5px;
                        width: 180px;
                }

                QTabBar::tab:selected {
                        background-color: blue;
                        color: white;
                }

                #search_book_button, #search_member_button {
                        padding: 10px;
                        background-color: blue;
                        color: white;
                        border: none;
                        border-radius: 2px;
                }

                #book_id_input, #member_id_input, #submit_or_renew_book_id_input {
                        padding: 6px;
                        border: 1px solid black;
                        border-radius: 2px;
                        color: black;
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

                #member_details_widget {
                        padding: 20px;
                        background-color: gray;
                        border-radius: 5px;
                }

                #return_time, #return_date {
                        padding: 10px;
                        font-size: 14px;
                        border: 1px solid black;
                        border-radius: 2px;
                        margin-right: 10px;
                }
                #return_time::down-button, #return_date::down-button, #return_time::up-button, #return_date::up-button {
                        width: 20px;
                        background: none;
                        border: none;
                        margin-right: 5px;
                }

                #return_time::up-arrow, #return_date::up-arrow {
                        image: url("C:/Users/James Matata/Desktop/CodeWizard/Python_Programming/Learning_Python_GUIs_with_PyQt6/13-Library_Management_System/images/up.png");
                        width: 20px;
                        height: 20px;
                }

                #return_time::down-arrow, #return_date::down-arrow {
                        image: url("C:/Users/James Matata/Desktop/CodeWizard/Python_Programming/Learning_Python_GUIs_with_PyQt6/13-Library_Management_System/images/down.png");
                        width: 20px;
                        height: 20px;
                }

                #return_details_widget, #member_details_widget, #book_details_widget {
                        padding: 20px;
                        background-color: gray;
                        border-radius: 5px;
                }
                #renew_book_button, #submit_book_button, #issue_book_button {
                    padding: 10px 20px;
                    background-color: blue;
                    border: none;
                    color: white;
                    border-radius: 2px;
                }
                #renew_book_button:disabled, #submit_book_button:disabled, #issue_book_button:disabled {
                    background-color: gray;
                }
                """
        )
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.book_details_widget = QtWidgets.QWidget(parent=self.tab)
        self.book_details_widget.setObjectName("book_details_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.book_details_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.book_id_input = QtWidgets.QLineEdit(parent=self.book_details_widget)
        self.book_id_input.setMinimumSize(QtCore.QSize(600, 0))
        self.book_id_input.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.book_id_input.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.book_id_input.setFont(font)
        self.book_id_input.setStyleSheet("")
        self.book_id_input.setObjectName("book_id_input")
        self.horizontalLayout_2.addWidget(self.book_id_input)
        self.book_id_input.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        self.book_exists_checkbox = QCheckBox()
        self.book_exists_checkbox.setChecked(False)
        self.book_exists_checkbox.setCheckable(True)
        self.book_exists_checkbox.setEnabled(False)
        self.horizontalLayout_2.addWidget(self.book_exists_checkbox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_2.addWidget(line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.book_details_widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color: black")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_3.addItem(spacerItem1)
        self.book_name_label = QtWidgets.QLabel(parent=self.book_details_widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.book_name_label.setFont(font)
        self.book_name_label.setObjectName("book_name_label")
        self.book_name_label.setStyleSheet("color: black;")
        self.horizontalLayout_3.addWidget(self.book_name_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(
            20,
            4,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(parent=self.book_details_widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: black")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_4.addItem(spacerItem3)
        self.book_author_label = QtWidgets.QLabel(parent=self.book_details_widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.book_author_label.setFont(font)
        self.book_author_label.setObjectName("book_author_label")
        self.book_author_label.setStyleSheet("color: black;")
        self.horizontalLayout_4.addWidget(self.book_author_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.addWidget(self.book_details_widget)
        spacerItem4 = QtWidgets.QSpacerItem(
            20,
            10,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        self.verticalLayout_5.addItem(spacerItem4)
        self.member_details_widget = QtWidgets.QWidget(parent=self.tab)
        self.member_details_widget.setObjectName("member_details_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.member_details_widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.member_id_input = QtWidgets.QLineEdit(parent=self.member_details_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.member_id_input.sizePolicy().hasHeightForWidth()
        )
        self.member_id_input.setSizePolicy(sizePolicy)
        self.member_id_input.setMinimumSize(QtCore.QSize(600, 0))
        self.member_id_input.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.member_id_input.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.member_id_input.setFont(font)
        self.member_id_input.setObjectName("member_id_input")
        self.horizontalLayout_5.addWidget(self.member_id_input)
        self.member_exists_checkbox = QCheckBox()
        self.member_exists_checkbox.setChecked(False)
        self.member_exists_checkbox.setCheckable(True)
        self.member_exists_checkbox.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.member_exists_checkbox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        line2 = QFrame()
        line2.setFrameShape(QFrame.Shape.HLine)
        line2.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_3.addWidget(line2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(parent=self.member_details_widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("color: black")
        self.horizontalLayout_6.addWidget(self.label_3)
        spacerItem6 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_6.addItem(spacerItem6)
        self.member_name_label = QtWidgets.QLabel(parent=self.member_details_widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.member_name_label.setFont(font)
        self.member_name_label.setObjectName("member_name_label")
        self.member_name_label.setStyleSheet("color: black")
        self.horizontalLayout_6.addWidget(self.member_name_label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        spacerItem7 = QtWidgets.QSpacerItem(
            20,
            4,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        self.verticalLayout_3.addItem(spacerItem7)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(parent=self.member_details_widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("color: black")
        self.horizontalLayout_7.addWidget(self.label_4)
        spacerItem8 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_7.addItem(spacerItem8)
        self.contact_info_label = QtWidgets.QLabel(parent=self.member_details_widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.contact_info_label.setFont(font)
        self.contact_info_label.setObjectName("contact_info_label")
        self.contact_info_label.setStyleSheet("color: black")
        self.horizontalLayout_7.addWidget(self.contact_info_label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.verticalLayout_5.addWidget(self.member_details_widget)
        spacerItem9 = QtWidgets.QSpacerItem(
            20,
            10,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        self.verticalLayout_5.addItem(spacerItem9)
        self.return_details_widget = QtWidgets.QWidget(parent=self.tab)
        self.return_details_widget.setObjectName("return_details_widget")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.return_details_widget)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(parent=self.return_details_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.return_date = QtWidgets.QDateEdit(parent=self.return_details_widget)
        self.return_date.setObjectName("return_date")
        self.verticalLayout_6.addWidget(self.return_date)
        self.horizontalLayout_9.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(parent=self.return_details_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.return_time = QtWidgets.QTimeEdit(parent=self.return_details_widget)
        self.return_time.setObjectName("return_time")
        self.verticalLayout_7.addWidget(self.return_time)
        self.horizontalLayout_9.addLayout(self.verticalLayout_7)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)
        self.verticalLayout_5.addWidget(self.return_details_widget)
        self.member_details_widget_2 = QtWidgets.QWidget(parent=self.tab)
        self.member_details_widget_2.setObjectName("member_details_widget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.member_details_widget_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem10 = QtWidgets.QSpacerItem(
            20,
            5,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        self.verticalLayout_4.addItem(spacerItem10)
        self.verticalLayout_5.addWidget(self.member_details_widget_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem11 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_8.addItem(spacerItem11)
        self.issue_book_button = QtWidgets.QPushButton(parent=self.tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.issue_book_button.setFont(font)
        self.issue_book_button.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(
                "C:/Users/James Matata/Desktop/CodeWizard/Python_Programming/Learning_Python_GUIs_with_PyQt6/13-Library_Management_System/images/issue.png"
            ),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.issue_book_button.setIcon(icon1)
        self.issue_book_button.setIconSize(QtCore.QSize(20, 20))
        self.issue_book_button.setObjectName("issue_book_button")
        self.issue_book_button.setDisabled(True)
        self.horizontalLayout_8.addWidget(self.issue_book_button)
        spacerItem12 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_8.addItem(spacerItem12)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        spacerItem13 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout_5.addItem(spacerItem13)
        self.tabWidget.addTab(self.tab, "")
        
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.submit_or_renew_book_id_input = QtWidgets.QLineEdit(parent=self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.submit_or_renew_book_id_input.setFont(font)
        self.submit_or_renew_book_id_input.setObjectName(
            "submit_or_renew_book_id_input"
        )
        self.verticalLayout_8.addWidget(self.submit_or_renew_book_id_input)
        spacerItem14 = QtWidgets.QSpacerItem(
            20,
            5,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        self.verticalLayout_8.addItem(spacerItem14)
        self.issued_books_info = QtWidgets.QTableWidget(parent=self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.issued_books_info.setFont(font)
        self.issued_books_info.setObjectName("issued_books_info")
        self.issued_books_info.setColumnCount(6)
        self.issued_books_info.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.issued_books_info.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.issued_books_info.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.issued_books_info.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.issued_books_info.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.issued_books_info.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.issued_books_info.setHorizontalHeaderItem(5, item)
        self.issued_books_info.horizontalHeader().setCascadingSectionResizes(False)
        self.issued_books_info.horizontalHeader().setStretchLastSection(False)
        self.issued_books_info.verticalHeader().setStretchLastSection(False)
        self.issued_books_info.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.issued_books_info.verticalHeader().setVisible(False)
        self.issued_books_info.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)  # Only one selection at a time
        self.issued_books_info.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)  # Select the entire row

        self.verticalLayout_8.addWidget(self.issued_books_info)
        spacerItem15 = QtWidgets.QSpacerItem(
            20,
            5,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        self.verticalLayout_8.addItem(spacerItem15)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem16 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_11.addItem(spacerItem16)
        self.renew_book_button = QtWidgets.QPushButton(parent=self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.renew_book_button.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(
                "C:/Users/James Matata/Desktop/CodeWizard/Python_Programming/Learning_Python_GUIs_with_PyQt6/13-Library_Management_System/images/renew.png"
            ),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.renew_book_button.setIcon(icon2)
        self.renew_book_button.setIconSize(QtCore.QSize(20, 20))
        self.renew_book_button.setObjectName("renew_book_button")
        self.renew_book_button.setEnabled(False)
        self.horizontalLayout_11.addWidget(self.renew_book_button)
        self.submit_book_button = QtWidgets.QPushButton(parent=self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.submit_book_button.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(
                "C:/Users/James Matata/Desktop/CodeWizard/Python_Programming/Learning_Python_GUIs_with_PyQt6/13-Library_Management_System/images/submit.png"
            ),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.submit_book_button.setIcon(icon3)
        self.submit_book_button.setIconSize(QtCore.QSize(20, 20))
        self.submit_book_button.setObjectName("submit_book_button")
        self.submit_book_button.setEnabled(False)
        self.horizontalLayout_11.addWidget(self.submit_book_button)
        spacerItem17 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_11.addItem(spacerItem17)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tool_button_add_book = QtWidgets.QToolButton(parent=self.centralwidget)
        self.tool_button_add_book.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tool_button_add_book.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap(
                "C:/Users/James Matata/Desktop/CodeWizard/Python_Programming/Learning_Python_GUIs_with_PyQt6/13-Library_Management_System/images/addbook.png"
            ),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.tool_button_add_book.setIcon(icon4)
        self.tool_button_add_book.setIconSize(QtCore.QSize(50, 50))
        self.tool_button_add_book.setToolButtonStyle(
            QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon
        )
        self.tool_button_add_book.setObjectName("tool_button_add_book")
        self.verticalLayout.addWidget(self.tool_button_add_book)
        self.tool_button_add_member = QtWidgets.QToolButton(parent=self.centralwidget)
        self.tool_button_add_member.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tool_button_add_member.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap(
                "C:/Users/James Matata/Desktop/CodeWizard/Python_Programming/Learning_Python_GUIs_with_PyQt6/13-Library_Management_System/images/addMember.png"
            ),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.tool_button_add_member.setIcon(icon5)
        self.tool_button_add_member.setIconSize(QtCore.QSize(50, 50))
        self.tool_button_add_member.setToolButtonStyle(
            QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon
        )
        self.tool_button_add_member.setObjectName("tool_button_add_member")
        self.verticalLayout.addWidget(self.tool_button_add_member)
        self.tool_button_view_books = QtWidgets.QToolButton(parent=self.centralwidget)
        self.tool_button_view_books.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tool_button_view_books.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(
            QtGui.QPixmap(
                "C:/Users/James Matata/Desktop/CodeWizard/Python_Programming/Learning_Python_GUIs_with_PyQt6/13-Library_Management_System/images/viewBooks.png"
            ),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.tool_button_view_books.setIcon(icon6)
        self.tool_button_view_books.setIconSize(QtCore.QSize(50, 50))
        self.tool_button_view_books.setToolButtonStyle(
            QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon
        )
        self.tool_button_view_books.setObjectName("tool_button_view_books")
        self.verticalLayout.addWidget(self.tool_button_view_books)
        self.tool_button_view_members = QtWidgets.QToolButton(parent=self.centralwidget)
        self.tool_button_view_members.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tool_button_view_members.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(
            QtGui.QPixmap(
                "C:/Users/James Matata/Desktop/CodeWizard/Python_Programming/Learning_Python_GUIs_with_PyQt6/13-Library_Management_System/images/viewMembers.png"
            ),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.tool_button_view_members.setIcon(icon7)
        self.tool_button_view_members.setIconSize(QtCore.QSize(50, 50))
        self.tool_button_view_members.setToolButtonStyle(
            QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon
        )
        self.tool_button_view_members.setObjectName("tool_button_view_members")
        self.verticalLayout.addWidget(self.tool_button_view_members)
        spacerItem19 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout.addItem(spacerItem19)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Library Management System"))
        self.book_id_input.setPlaceholderText(
            _translate("MainWindow", "Please enter book id")
        )
        self.label.setText(_translate("MainWindow", "Book Name:"))
        self.book_name_label.setText(_translate("MainWindow", "--------------"))
        self.label_2.setText(_translate("MainWindow", "Book Author:"))
        self.book_author_label.setText(_translate("MainWindow", "--------------"))
        self.member_id_input.setPlaceholderText(
            _translate("MainWindow", "Please enter book id")
        )
        self.label_3.setText(_translate("MainWindow", "Member Name:"))
        self.member_name_label.setText(_translate("MainWindow", "--------------"))
        self.label_4.setText(_translate("MainWindow", "Contact info:"))
        self.contact_info_label.setText(_translate("MainWindow", "--------------"))
        self.label_5.setText(_translate("MainWindow", "Return Date:"))
        self.label_6.setText(_translate("MainWindow", "Return Time:"))
        self.issue_book_button.setText(_translate("MainWindow", "Issue"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Issue book")
        )
        self.submit_or_renew_book_id_input.setPlaceholderText(
            _translate("MainWindow", "Enter book ID")
        )
        item = self.issued_books_info.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Issue ID"))
        item = self.issued_books_info.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Member ID"))
        item = self.issued_books_info.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Book ID"))
        item = self.issued_books_info.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Return Date"))
        item = self.issued_books_info.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Return Time"))
        item = self.issued_books_info.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Renew Count"))
        self.renew_book_button.setText(_translate("MainWindow", "Renew"))
        self.submit_book_button.setText(_translate("MainWindow", "Submit"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            _translate("MainWindow", "Renew/Submit book"),
        )
        self.tool_button_add_book.setText(_translate("MainWindow", "Add Book"))
        self.tool_button_add_member.setText(_translate("MainWindow", "Add Member"))
        self.tool_button_view_books.setText(_translate("MainWindow", "View Books"))
        self.tool_button_view_members.setText(_translate("MainWindow", "View Members"))
