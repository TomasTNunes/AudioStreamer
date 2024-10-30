# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

from hoverslider import HoverSlider
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(806, 583)
        MainWindow.setMinimumSize(QSize(800, 570))
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(8, 8, 8, 8)
        self.bottomWidget = QWidget(self.centralwidget)
        self.bottomWidget.setObjectName(u"bottomWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottomWidget.sizePolicy().hasHeightForWidth())
        self.bottomWidget.setSizePolicy(sizePolicy)
        self.bottomWidget.setMinimumSize(QSize(0, 75))
        self.bottomWidget.setStyleSheet(u"/*background-color: rgb(170, 170, 127);*/")
        self.horizontalSlider = HoverSlider(self.bottomWidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(270, 40, 241, 12))
        self.horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"                background: rgb(76, 76, 76); /* Grey for the background */\n"
"                height: 4px; /* Thickness of the slider */\n"
"                border-radius: 2px; /* Rounded edges */\n"
"                }\n"
"\n"
"                QSlider::add-page:horizontal  {\n"
"                background: rgb(76, 76, 76);\n"
"                        height: 4px; /* Thickness of the slider */\n"
"                border-radius: 2px; /* Rounded edges */\n"
"                }\n"
"\n"
"                QSlider::sub-page:horizontal  {\n"
"                background: rgb(255, 255, 255);\n"
"                        height: 4px; /* Thickness of the slider */\n"
"                border-radius: 2px; /* Rounded edges */\n"
"                }\n"
"\n"
"                QSlider::handle:horizontal  {\n"
"                background: transparent; \n"
"                width: 12px;\n"
"                height: 6px;\n"
"                margin: -4px -5;\n"
"                border-radius: 6px;\n"
"   "
                        "             }")
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setTracking(True)
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)

        self.gridLayout.addWidget(self.bottomWidget, 1, 0, 1, 2)

        self.leftVLayout = QVBoxLayout()
        self.leftVLayout.setSpacing(8)
        self.leftVLayout.setObjectName(u"leftVLayout")
        self.homeBackgroundWidget = QWidget(self.centralwidget)
        self.homeBackgroundWidget.setObjectName(u"homeBackgroundWidget")
        self.homeBackgroundWidget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.homeBackgroundWidget.sizePolicy().hasHeightForWidth())
        self.homeBackgroundWidget.setSizePolicy(sizePolicy1)
        self.homeBackgroundWidget.setMinimumSize(QSize(290, 110))
        self.homeBackgroundWidget.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(12)
        self.homeBackgroundWidget.setFont(font)
        self.homeBackgroundWidget.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(18, 18, 18);")
        self.verticalLayout_2 = QVBoxLayout(self.homeBackgroundWidget)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(24, 8, 35, 8)
        self.homeButton = QPushButton(self.homeBackgroundWidget)
        self.homeButton.setObjectName(u"homeButton")
        sizePolicy1.setHeightForWidth(self.homeButton.sizePolicy().hasHeightForWidth())
        self.homeButton.setSizePolicy(sizePolicy1)
        self.homeButton.setMinimumSize(QSize(0, 0))
        self.homeButton.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Black"])
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setUnderline(False)
        font1.setKerning(True)
        self.homeButton.setFont(font1)
        self.homeButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.homeButton.setStyleSheet(u"QPushButton {\n"
"    text-align: left;       /* Align text to the left */\n"
"    padding-left: 0px;      /* Adjust padding as needed */\n"
"    color: rgb(180, 180, 180);\n"
"}\n"
"\n"
"QPushButton::icon {\n"
"    subcontrol-position: left center; /* Icon to the left and centered vertically */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    icon: url(:/assets/buttons/home_hover.png);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    icon: url(:/assets/buttons/home_pressed.png);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/assets/buttons/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homeButton.setIcon(icon)
        self.homeButton.setIconSize(QSize(22, 22))
        self.homeButton.setCheckable(True)
        self.homeButton.setChecked(False)
        self.homeButton.setAutoRepeat(False)
        self.homeButton.setAutoDefault(False)
        self.homeButton.setFlat(False)

        self.verticalLayout_2.addWidget(self.homeButton)

        self.searchButton = QPushButton(self.homeBackgroundWidget)
        self.searchButton.setObjectName(u"searchButton")
        sizePolicy1.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy1)
        self.searchButton.setMaximumSize(QSize(16777215, 40))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Black"])
        font2.setPointSize(11)
        font2.setHintingPreference(QFont.PreferDefaultHinting)
        self.searchButton.setFont(font2)
        self.searchButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.searchButton.setStyleSheet(u"QPushButton {\n"
"    text-align: left;       /* Align text to the left */\n"
"    padding-left: 0px;     /* Adjust padding as needed */\n"
"	color: rgb(180, 180, 180);\n"
"}\n"
"\n"
"QPushButton::icon {\n"
"    subcontrol-position: left center; /* Icon to the left and centered vertically */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    icon: url(:assets/buttons/search_hover.png);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    icon: url(:assets/buttons/search_pressed.png);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/assets/buttons/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.searchButton.setIcon(icon1)
        self.searchButton.setIconSize(QSize(22, 22))
        self.searchButton.setCheckable(True)

        self.verticalLayout_2.addWidget(self.searchButton)


        self.leftVLayout.addWidget(self.homeBackgroundWidget)

        self.libraryBackgroundWidget = QWidget(self.centralwidget)
        self.libraryBackgroundWidget.setObjectName(u"libraryBackgroundWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.libraryBackgroundWidget.sizePolicy().hasHeightForWidth())
        self.libraryBackgroundWidget.setSizePolicy(sizePolicy2)
        self.libraryBackgroundWidget.setMaximumSize(QSize(16777215, 16777215))
        self.libraryBackgroundWidget.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(18, 18, 18);")
        self.verticalLayout_3 = QVBoxLayout(self.libraryBackgroundWidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.libraryHLayout = QHBoxLayout()
        self.libraryHLayout.setSpacing(73)
        self.libraryHLayout.setObjectName(u"libraryHLayout")
        self.libraryHLayout.setContentsMargins(16, 8, 16, 8)
        self.libraryButton = QPushButton(self.libraryBackgroundWidget)
        self.libraryButton.setObjectName(u"libraryButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.libraryButton.sizePolicy().hasHeightForWidth())
        self.libraryButton.setSizePolicy(sizePolicy3)
        self.libraryButton.setMinimumSize(QSize(135, 40))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Black"])
        font3.setPointSize(11)
        self.libraryButton.setFont(font3)
        self.libraryButton.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.libraryButton.setStyleSheet(u"QPushButton {\n"
"    text-align: left;       /* Align text to the left */\n"
"    padding-left: 8px;     /* Adjust padding as needed */\n"
"	color: rgb(180, 180, 180);\n"
"}\n"
"\n"
"QPushButton::icon {\n"
"    subcontrol-position: left center; /* Icon to the left and centered vertically */\n"
"}\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/assets/buttons/library.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.libraryButton.setIcon(icon2)
        self.libraryButton.setIconSize(QSize(22, 22))

        self.libraryHLayout.addWidget(self.libraryButton)

        self.addButton = QPushButton(self.libraryBackgroundWidget)
        self.addButton.setObjectName(u"addButton")
        sizePolicy3.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy3)
        self.addButton.setMinimumSize(QSize(0, 32))
        self.addButton.setMaximumSize(QSize(32, 16777215))
        self.addButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.addButton.setStyleSheet(u"QPushButton {\n"
"	border-radius: 16.4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    icon: url(:assets/buttons/add_hover.png);\n"
"	background-color: rgb(31, 31, 31);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    icon: url(:assets/buttons/add_hover.png);\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/assets/buttons/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addButton.setIcon(icon3)
        self.addButton.setIconSize(QSize(14, 14))

        self.libraryHLayout.addWidget(self.addButton)


        self.verticalLayout_3.addLayout(self.libraryHLayout)

        self.playlistsButtonsHLayout = QHBoxLayout()
        self.playlistsButtonsHLayout.setSpacing(8)
        self.playlistsButtonsHLayout.setObjectName(u"playlistsButtonsHLayout")
        self.playlistsButtonsHLayout.setContentsMargins(16, 8, 0, 8)
        self.playlistsButton = QPushButton(self.libraryBackgroundWidget)
        self.playlistsButton.setObjectName(u"playlistsButton")
        sizePolicy3.setHeightForWidth(self.playlistsButton.sizePolicy().hasHeightForWidth())
        self.playlistsButton.setSizePolicy(sizePolicy3)
        self.playlistsButton.setMinimumSize(QSize(76, 32))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        font4.setBold(True)
        self.playlistsButton.setFont(font4)
        self.playlistsButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.playlistsButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(36, 36, 36);\n"
"	color: rgb(244, 244, 244);\n"
"	border-radius: 16.4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(42, 42, 42);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.playlistsButton.setIconSize(QSize(22, 22))
        self.playlistsButton.setCheckable(True)

        self.playlistsButtonsHLayout.addWidget(self.playlistsButton)

        self.albumsButton = QPushButton(self.libraryBackgroundWidget)
        self.albumsButton.setObjectName(u"albumsButton")
        sizePolicy3.setHeightForWidth(self.albumsButton.sizePolicy().hasHeightForWidth())
        self.albumsButton.setSizePolicy(sizePolicy3)
        self.albumsButton.setMinimumSize(QSize(72, 32))
        self.albumsButton.setMaximumSize(QSize(16777215, 16777215))
        self.albumsButton.setFont(font4)
        self.albumsButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.albumsButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(36, 36, 36);\n"
"	color: rgb(244, 244, 244);\n"
"	border-radius: 16.4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(42, 42, 42);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.albumsButton.setIconSize(QSize(14, 14))
        self.albumsButton.setCheckable(True)

        self.playlistsButtonsHLayout.addWidget(self.albumsButton)

        self.artistsButton = QPushButton(self.libraryBackgroundWidget)
        self.artistsButton.setObjectName(u"artistsButton")
        sizePolicy3.setHeightForWidth(self.artistsButton.sizePolicy().hasHeightForWidth())
        self.artistsButton.setSizePolicy(sizePolicy3)
        self.artistsButton.setMinimumSize(QSize(66, 32))
        self.artistsButton.setFont(font4)
        self.artistsButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.artistsButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(36, 36, 36);\n"
"	color: rgb(244, 244, 244);\n"
"	border-radius: 16.4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(42, 42, 42);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.artistsButton.setCheckable(True)

        self.playlistsButtonsHLayout.addWidget(self.artistsButton)

        self.playlistsButtonsSpacer = QSpacerItem(35, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.playlistsButtonsHLayout.addItem(self.playlistsButtonsSpacer)


        self.verticalLayout_3.addLayout(self.playlistsButtonsHLayout)

        self.libraryScrollArea = QScrollArea(self.libraryBackgroundWidget)
        self.libraryScrollArea.setObjectName(u"libraryScrollArea")
        sizePolicy2.setHeightForWidth(self.libraryScrollArea.sizePolicy().hasHeightForWidth())
        self.libraryScrollArea.setSizePolicy(sizePolicy2)
        self.libraryScrollArea.setStyleSheet(u"background-color: rgb(18, 18, 18);\n"
"\n"
"/*background-color: rgb(170, 0, 0);*/")
        self.libraryScrollArea.setWidgetResizable(True)
        self.libraryScrollAreaWidget = QWidget()
        self.libraryScrollAreaWidget.setObjectName(u"libraryScrollAreaWidget")
        self.libraryScrollAreaWidget.setGeometry(QRect(0, 0, 290, 260))
        self.libraryScrollArea.setWidget(self.libraryScrollAreaWidget)

        self.verticalLayout_3.addWidget(self.libraryScrollArea)


        self.leftVLayout.addWidget(self.libraryBackgroundWidget)


        self.gridLayout.addLayout(self.leftVLayout, 0, 0, 1, 1)

        self.rightStackedWidget = QStackedWidget(self.centralwidget)
        self.rightStackedWidget.setObjectName(u"rightStackedWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.rightStackedWidget.sizePolicy().hasHeightForWidth())
        self.rightStackedWidget.setSizePolicy(sizePolicy4)
        self.rightStackedWidget.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(18, 18, 18);\n"
"")
        self.rightStackedWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.rightStackedWidget.setLineWidth(1)
        self.RSWhomeWidget = QWidget()
        self.RSWhomeWidget.setObjectName(u"RSWhomeWidget")
        self.rightStackedWidget.addWidget(self.RSWhomeWidget)
        self.RSWsearchWidget = QWidget()
        self.RSWsearchWidget.setObjectName(u"RSWsearchWidget")
        self.verticalLayout = QVBoxLayout(self.RSWsearchWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.RSWSsearchHLayout = QHBoxLayout()
        self.RSWSsearchHLayout.setSpacing(6)
        self.RSWSsearchHLayout.setObjectName(u"RSWSsearchHLayout")
        self.RSWSsearchHLayout.setContentsMargins(16, 8, 8, 6)
        self.RSWSbackButton = QPushButton(self.RSWsearchWidget)
        self.RSWSbackButton.setObjectName(u"RSWSbackButton")
        sizePolicy3.setHeightForWidth(self.RSWSbackButton.sizePolicy().hasHeightForWidth())
        self.RSWSbackButton.setSizePolicy(sizePolicy3)
        self.RSWSbackButton.setMinimumSize(QSize(32, 32))
        self.RSWSbackButton.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setWeight(QFont.DemiBold)
        self.RSWSbackButton.setFont(font5)
        self.RSWSbackButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.RSWSbackButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 0, 0);\n"
"	border-radius: 16.4px;\n"
"}\n"
"\n"
"QToolTip {\n"
"    color: rgb(255, 255, 255); \n"
"    background-color: rgb(36, 36, 36); \n"
"    padding: 5px; \n"
"    font: 13px \"Segoe UI\"; \n"
"	font-weight: 600;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/assets/buttons/left.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.RSWSbackButton.setIcon(icon4)
        self.RSWSbackButton.setIconSize(QSize(16, 16))

        self.RSWSsearchHLayout.addWidget(self.RSWSbackButton)

        self.RSWSsearchQLineEdit = QLineEdit(self.RSWsearchWidget)
        self.RSWSsearchQLineEdit.setObjectName(u"RSWSsearchQLineEdit")
        sizePolicy.setHeightForWidth(self.RSWSsearchQLineEdit.sizePolicy().hasHeightForWidth())
        self.RSWSsearchQLineEdit.setSizePolicy(sizePolicy)
        self.RSWSsearchQLineEdit.setMinimumSize(QSize(320, 50))
        self.RSWSsearchQLineEdit.setMaximumSize(QSize(364, 16777215))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(10)
        font6.setWeight(QFont.DemiBold)
        font6.setStrikeOut(False)
        self.RSWSsearchQLineEdit.setFont(font6)
        self.RSWSsearchQLineEdit.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(150, 150, 150);\n"
"	background-color: rgb(36, 36, 36);\n"
"    border-radius: 24.4px;\n"
"	border: 2px solid;\n"
"	border-color: rgb(18, 18, 18);\n"
"	padding-left: 32px;\n"
"	background: url(:/assets/buttons/search16x16.png) no-repeat;\n"
"    background-position: left center;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: rgb(42, 42, 42);\n"
"	border: 2px solid;\n"
"	border-color: rgb(80, 80, 80);\n"
"	background: url(:/assets/buttons/search16x16_hover.png) no-repeat;\n"
"    background-position: left center;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	background: url(:/assets/buttons/search16x16_hover.png) no-repeat;\n"
"    background-position: left center;\n"
"	color: rgb(250, 250, 250);\n"
"}\n"
"\n"
"QLineEdit::clear-button {\n"
"        image: url(:/assets/buttons/search16x16_hover.png);  /* Set your custom icon path */\n"
"        width: 16px;\n"
"        height: 16px;\n"
"    }\n"
"")
        self.RSWSsearchQLineEdit.setClearButtonEnabled(True)

        self.RSWSsearchHLayout.addWidget(self.RSWSsearchQLineEdit)

        self.RSWSsearchHSpacer = QSpacerItem(120, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.RSWSsearchHLayout.addItem(self.RSWSsearchHSpacer)

        self.RSWSsearchHLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.RSWSsearchHLayout)

        self.RSWSscrollArea = QScrollArea(self.RSWsearchWidget)
        self.RSWSscrollArea.setObjectName(u"RSWSscrollArea")
        self.RSWSscrollArea.setStyleSheet(u"QScrollBar:vertical {\n"
"    width: 12px;\n"
"}\n"
"\n"
"/* Style for the scrollbar handle */\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(90, 90, 90);\n"
"    min-height: 20px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"/* Handle color when hovered */\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"/* Handle color when pressed */\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background: rgb(160, 160, 160);\n"
"}\n"
"\n"
"/* Background color for the area above and below the handle */\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: rgb(18, 18, 18);\n"
"}\n"
"")
        self.RSWSscrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.RSWSscrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.RSWSscrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.RSWSscrollArea.setWidgetResizable(True)
        self.RSWSscrollAreaWidget = QWidget()
        self.RSWSscrollAreaWidget.setObjectName(u"RSWSscrollAreaWidget")
        self.RSWSscrollAreaWidget.setGeometry(QRect(0, 0, 478, 420))
        self.RSWSscrollAreaWidget.setStyleSheet(u"")
        self.RSWSscrollVLayout = QVBoxLayout(self.RSWSscrollAreaWidget)
        self.RSWSscrollVLayout.setSpacing(0)
        self.RSWSscrollVLayout.setObjectName(u"RSWSscrollVLayout")
        self.RSWSscrollVLayout.setContentsMargins(16, 0, 4, 16)
        self.RSWSscrollArea.setWidget(self.RSWSscrollAreaWidget)

        self.verticalLayout.addWidget(self.RSWSscrollArea)

        self.rightStackedWidget.addWidget(self.RSWsearchWidget)

        self.gridLayout.addWidget(self.rightStackedWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.homeButton.setDefault(False)
        self.rightStackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"    Home", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"    Search", None))
        self.libraryButton.setText(QCoreApplication.translate("MainWindow", u" Your Library", None))
        self.addButton.setText("")
        self.playlistsButton.setText(QCoreApplication.translate("MainWindow", u"Playlists", None))
        self.albumsButton.setText(QCoreApplication.translate("MainWindow", u"Albums", None))
        self.artistsButton.setText(QCoreApplication.translate("MainWindow", u"Artists", None))
#if QT_CONFIG(tooltip)
        self.RSWSbackButton.setToolTip(QCoreApplication.translate("MainWindow", u"Go back", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.RSWSbackButton.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.RSWSbackButton.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.RSWSbackButton.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.RSWSbackButton.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.RSWSbackButton.setText("")
        self.RSWSsearchQLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"What do you want to play?", None))
    # retranslateUi

