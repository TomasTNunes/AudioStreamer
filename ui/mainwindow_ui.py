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
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

from coverlabel import CoverLabel
from customscrollarea import CustomScrollArea
from hoverslider import HoverSlider
from loopbutton import LoopButton
from roundbutton import RoundButton
from volumebutton import VolumeButton
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 570)
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
        self.leftVLayout = QVBoxLayout()
        self.leftVLayout.setSpacing(8)
        self.leftVLayout.setObjectName(u"leftVLayout")
        self.homeBackgroundWidget = QWidget(self.centralwidget)
        self.homeBackgroundWidget.setObjectName(u"homeBackgroundWidget")
        self.homeBackgroundWidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.homeBackgroundWidget.sizePolicy().hasHeightForWidth())
        self.homeBackgroundWidget.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.homeButton.sizePolicy().hasHeightForWidth())
        self.homeButton.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.libraryBackgroundWidget.sizePolicy().hasHeightForWidth())
        self.libraryBackgroundWidget.setSizePolicy(sizePolicy1)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.libraryButton.sizePolicy().hasHeightForWidth())
        self.libraryButton.setSizePolicy(sizePolicy2)
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

        self.addButton = RoundButton(self.libraryBackgroundWidget)
        self.addButton.setObjectName(u"addButton")
        sizePolicy2.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy2)
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
        sizePolicy2.setHeightForWidth(self.playlistsButton.sizePolicy().hasHeightForWidth())
        self.playlistsButton.setSizePolicy(sizePolicy2)
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
        sizePolicy2.setHeightForWidth(self.albumsButton.sizePolicy().hasHeightForWidth())
        self.albumsButton.setSizePolicy(sizePolicy2)
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
        sizePolicy2.setHeightForWidth(self.artistsButton.sizePolicy().hasHeightForWidth())
        self.artistsButton.setSizePolicy(sizePolicy2)
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
        sizePolicy1.setHeightForWidth(self.libraryScrollArea.sizePolicy().hasHeightForWidth())
        self.libraryScrollArea.setSizePolicy(sizePolicy1)
        self.libraryScrollArea.setStyleSheet(u"background-color: rgb(18, 18, 18);\n"
"\n"
"/*background-color: rgb(170, 0, 0);*/")
        self.libraryScrollArea.setWidgetResizable(True)
        self.libraryScrollAreaWidget = QWidget()
        self.libraryScrollAreaWidget.setObjectName(u"libraryScrollAreaWidget")
        self.libraryScrollAreaWidget.setGeometry(QRect(0, 0, 290, 250))
        self.libraryScrollArea.setWidget(self.libraryScrollAreaWidget)

        self.verticalLayout_3.addWidget(self.libraryScrollArea)


        self.leftVLayout.addWidget(self.libraryBackgroundWidget)


        self.gridLayout.addLayout(self.leftVLayout, 0, 0, 1, 1)

        self.rightStackedWidget = QStackedWidget(self.centralwidget)
        self.rightStackedWidget.setObjectName(u"rightStackedWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.rightStackedWidget.sizePolicy().hasHeightForWidth())
        self.rightStackedWidget.setSizePolicy(sizePolicy3)
        self.rightStackedWidget.setMinimumSize(QSize(0, 470))
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
        self.RSWsearchWidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.RSWsearchWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.RSWSsearchHLayout = QHBoxLayout()
        self.RSWSsearchHLayout.setSpacing(6)
        self.RSWSsearchHLayout.setObjectName(u"RSWSsearchHLayout")
        self.RSWSsearchHLayout.setContentsMargins(16, 8, 8, 6)
        self.RSWSbackButton = RoundButton(self.RSWsearchWidget)
        self.RSWSbackButton.setObjectName(u"RSWSbackButton")
        sizePolicy2.setHeightForWidth(self.RSWSbackButton.sizePolicy().hasHeightForWidth())
        self.RSWSbackButton.setSizePolicy(sizePolicy2)
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
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.RSWSsearchQLineEdit.sizePolicy().hasHeightForWidth())
        self.RSWSsearchQLineEdit.setSizePolicy(sizePolicy4)
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

        self.RSWSsearchHSpacer = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.RSWSsearchHLayout.addItem(self.RSWSsearchHSpacer)

        self.RSWSsearchHLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.RSWSsearchHLayout)

        self.RSWSscrollArea = CustomScrollArea(self.RSWsearchWidget)
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
"    background: rgb(180, 180, 180);\n"
"}\n"
"\n"
"/* Background color for the area above and below the handle */\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: rgb(18, 18, 18);\n"
"}\n"
"")
        self.RSWSscrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.RSWSscrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.RSWSscrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.RSWSscrollArea.setWidgetResizable(True)
        self.RSWSscrollAreaWidget = QWidget()
        self.RSWSscrollAreaWidget.setObjectName(u"RSWSscrollAreaWidget")
        self.RSWSscrollAreaWidget.setGeometry(QRect(0, 0, 484, 410))
        self.RSWSscrollAreaWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.RSWSscrollAreaWidget.setAutoFillBackground(False)
        self.RSWSscrollAreaWidget.setStyleSheet(u"")
        self.RSWSscrollVLayout = QVBoxLayout(self.RSWSscrollAreaWidget)
        self.RSWSscrollVLayout.setSpacing(0)
        self.RSWSscrollVLayout.setObjectName(u"RSWSscrollVLayout")
        self.RSWSscrollVLayout.setContentsMargins(16, 0, 4, 16)
        self.RSWSscrollAreaSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.RSWSscrollVLayout.addItem(self.RSWSscrollAreaSpacer)

        self.RSWSscrollArea.setWidget(self.RSWSscrollAreaWidget)

        self.verticalLayout.addWidget(self.RSWSscrollArea)

        self.rightStackedWidget.addWidget(self.RSWsearchWidget)

        self.gridLayout.addWidget(self.rightStackedWidget, 0, 1, 1, 1)

        self.bottomWidget = QWidget(self.centralwidget)
        self.bottomWidget.setObjectName(u"bottomWidget")
        sizePolicy4.setHeightForWidth(self.bottomWidget.sizePolicy().hasHeightForWidth())
        self.bottomWidget.setSizePolicy(sizePolicy4)
        self.bottomWidget.setMinimumSize(QSize(0, 72))
        self.bottomWidget.setMaximumSize(QSize(16777215, 72))
        self.bottomWidget.setStyleSheet(u"/*background-color: rgb(170, 170, 127);*/")
        self.horizontalLayout_3 = QHBoxLayout(self.bottomWidget)
        self.horizontalLayout_3.setSpacing(16)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.BWleftWidget = QWidget(self.bottomWidget)
        self.BWleftWidget.setObjectName(u"BWleftWidget")
        sizePolicy4.setHeightForWidth(self.BWleftWidget.sizePolicy().hasHeightForWidth())
        self.BWleftWidget.setSizePolicy(sizePolicy4)
        self.BWleftWidget.setMinimumSize(QSize(230, 0))
        self.BWleftWidget.setMaximumSize(QSize(16777215, 75))
        self.BWleftWidget.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.BWleftWidget)
        self.horizontalLayout_4.setSpacing(12)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(8, 6, 0, 10)
        self.iconLabel = CoverLabel(self.BWleftWidget)
        self.iconLabel.setObjectName(u"iconLabel")
        sizePolicy2.setHeightForWidth(self.iconLabel.sizePolicy().hasHeightForWidth())
        self.iconLabel.setSizePolicy(sizePolicy2)
        self.iconLabel.setMinimumSize(QSize(56, 56))
        self.iconLabel.setMaximumSize(QSize(56, 56))
        self.iconLabel.setStyleSheet(u"background-color: rgb(0, 170, 0);\n"
"border-radius: 4px;")

        self.horizontalLayout_4.addWidget(self.iconLabel)

        self.BWLrightWidget = QWidget(self.BWleftWidget)
        self.BWLrightWidget.setObjectName(u"BWLrightWidget")
        sizePolicy.setHeightForWidth(self.BWLrightWidget.sizePolicy().hasHeightForWidth())
        self.BWLrightWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.BWLrightWidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 4)
        self.musicLabel = QLabel(self.BWLrightWidget)
        self.musicLabel.setObjectName(u"musicLabel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.musicLabel.sizePolicy().hasHeightForWidth())
        self.musicLabel.setSizePolicy(sizePolicy5)
        self.musicLabel.setMinimumSize(QSize(0, 22))
        self.musicLabel.setMaximumSize(QSize(16777215, 22))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI Black"])
        font7.setPointSize(11)
        font7.setBold(True)
        self.musicLabel.setFont(font7)
        self.musicLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")

        self.verticalLayout_5.addWidget(self.musicLabel)

        self.artistLabel = QLabel(self.BWLrightWidget)
        self.artistLabel.setObjectName(u"artistLabel")
        sizePolicy5.setHeightForWidth(self.artistLabel.sizePolicy().hasHeightForWidth())
        self.artistLabel.setSizePolicy(sizePolicy5)
        self.artistLabel.setMinimumSize(QSize(0, 20))
        self.artistLabel.setMaximumSize(QSize(16777215, 20))
        font8 = QFont()
        font8.setPointSize(10)
        font8.setBold(True)
        font8.setUnderline(False)
        self.artistLabel.setFont(font8)
        self.artistLabel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.artistLabel.setStyleSheet(u"QLabel {\n"
"   color: rgb(180, 180, 180);\n"
"	background-color: none;\n"
"}\n"
"\n"
"\n"
"QLabel:hover {\n"
"	color: rgb(255, 255, 255)\n"
"}")

        self.verticalLayout_5.addWidget(self.artistLabel)


        self.horizontalLayout_4.addWidget(self.BWLrightWidget)


        self.horizontalLayout_3.addWidget(self.BWleftWidget)

        self.BWcenterWidget = QWidget(self.bottomWidget)
        self.BWcenterWidget.setObjectName(u"BWcenterWidget")
        sizePolicy.setHeightForWidth(self.BWcenterWidget.sizePolicy().hasHeightForWidth())
        self.BWcenterWidget.setSizePolicy(sizePolicy)
        self.BWcenterWidget.setMaximumSize(QSize(700, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.BWcenterWidget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.BWCtopWidget = QWidget(self.BWcenterWidget)
        self.BWCtopWidget.setObjectName(u"BWCtopWidget")
        self.horizontalLayout = QHBoxLayout(self.BWCtopWidget)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, 8, 8, 8)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.shuffleButton = RoundButton(self.BWCtopWidget)
        self.shuffleButton.setObjectName(u"shuffleButton")
        self.shuffleButton.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.shuffleButton.sizePolicy().hasHeightForWidth())
        self.shuffleButton.setSizePolicy(sizePolicy2)
        self.shuffleButton.setMinimumSize(QSize(32, 32))
        self.shuffleButton.setMaximumSize(QSize(32, 32))
        self.shuffleButton.setFont(font5)
        self.shuffleButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.shuffleButton.setStyleSheet(u"QPushButton {\n"
"	background-color: trasnparent;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    icon: url(:/assets/buttons/shuffle_hover.png);\n"
"}\n"
"\n"
"QPushButton:pressed  {\n"
"    icon: url(:/assets/buttons/shuffle_pressed2.png);\n"
"}\n"
"\n"
"QPushButton:checked  {\n"
"    icon: url(:/assets/buttons/shuffle_pressed.png);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    icon: url(:/assets/buttons/shuffle_disabled.png);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/assets/buttons/shuffle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.shuffleButton.setIcon(icon5)
        self.shuffleButton.setIconSize(QSize(32, 32))
        self.shuffleButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.shuffleButton)

        self.previousTrackButton = RoundButton(self.BWCtopWidget)
        self.previousTrackButton.setObjectName(u"previousTrackButton")
        self.previousTrackButton.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.previousTrackButton.sizePolicy().hasHeightForWidth())
        self.previousTrackButton.setSizePolicy(sizePolicy2)
        self.previousTrackButton.setMinimumSize(QSize(32, 32))
        self.previousTrackButton.setMaximumSize(QSize(32, 32))
        self.previousTrackButton.setFont(font5)
        self.previousTrackButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.previousTrackButton.setStyleSheet(u"QPushButton {\n"
"	background-color: trasnparent;\n"
"	border-radius: 16px;\n"
"	padding-left: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    icon: url(:/assets/buttons/previousTrack_hover.png);\n"
"}\n"
"\n"
"QPushButton:pressed  {\n"
"    icon: url(:/assets/buttons/previousTrack_pressed.png);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    icon: url(:/assets/buttons/previousTrack_disabled.png);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/assets/buttons/previousTrack.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.previousTrackButton.setIcon(icon6)
        self.previousTrackButton.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.previousTrackButton)

        self.horizontalSpacer_3 = QSpacerItem(8, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.playButton = RoundButton(self.BWCtopWidget)
        self.playButton.setObjectName(u"playButton")
        self.playButton.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.playButton.sizePolicy().hasHeightForWidth())
        self.playButton.setSizePolicy(sizePolicy2)
        self.playButton.setMinimumSize(QSize(32, 32))
        self.playButton.setMaximumSize(QSize(32, 32))
        self.playButton.setFont(font5)
        self.playButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.playButton.setStyleSheet(u"QPushButton {\n"
"	/*background-color: rgb(255, 255, 255);*/\n"
"	border-radius: 16px;\n"
"	padding-left: 3px;\n"
"	background-color: transparent;\n"
"    background: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius: 0.5,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 rgba(255, 255, 255, 255),\n"
"        stop:0.94 rgba(255, 255, 255, 255),\n"
"		 stop:0.99 rgba(255, 255, 255, 0),\n"
"        stop:1 rgba(255, 255, 255, 0)\n"
"    );\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed  {\n"
"	background-color: transparent;\n"
"    background: qradialgradient(\n"
"        cx:0.5, cy:0.5, radius: 0.5,\n"
"        fx:0.5, fy:0.5,\n"
"        stop:0 rgba(180, 180, 180, 180),\n"
"        stop:0.94 rgba(180, 180, 180, 180),\n"
"		 stop:0.99 rgba(180, 180, 180, 0),\n"
"        stop:1 rgba(180, 180, 180, 0)\n"
"    );\n"
"}\n"
"\n"
"QPushButton:checked  {\n"
"    icon: url(:/assets/buttons/pause.png);\n"
"	padding-left: 0px;\n"
"}\n"
"\n"
"QPushButton:disab"
                        "led {\n"
"    background-color: rgb(20, 20, 20);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/assets/buttons/play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/assets/buttons/play.png", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        self.playButton.setIcon(icon7)
        self.playButton.setIconSize(QSize(16, 16))
        self.playButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.playButton)

        self.horizontalSpacer_4 = QSpacerItem(8, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.nextTrackButton = RoundButton(self.BWCtopWidget)
        self.nextTrackButton.setObjectName(u"nextTrackButton")
        self.nextTrackButton.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.nextTrackButton.sizePolicy().hasHeightForWidth())
        self.nextTrackButton.setSizePolicy(sizePolicy2)
        self.nextTrackButton.setMinimumSize(QSize(32, 32))
        self.nextTrackButton.setMaximumSize(QSize(32, 32))
        self.nextTrackButton.setFont(font5)
        self.nextTrackButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.nextTrackButton.setStyleSheet(u"QPushButton {\n"
"	background-color: trasnparent;\n"
"	border-radius: 16px;\n"
"	padding-left: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    icon: url(:/assets/buttons/nextTrack_hover.png);\n"
"}\n"
"\n"
"QPushButton:pressed  {\n"
"    icon: url(:/assets/buttons/nextTrack_pressed.png);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    icon: url(:/assets/buttons/nextTrack_disabled.png);\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/assets/buttons/nextTrack.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.nextTrackButton.setIcon(icon8)
        self.nextTrackButton.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.nextTrackButton)

        self.loopButton = LoopButton(self.BWCtopWidget)
        self.loopButton.setObjectName(u"loopButton")
        self.loopButton.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.loopButton.sizePolicy().hasHeightForWidth())
        self.loopButton.setSizePolicy(sizePolicy2)
        self.loopButton.setMinimumSize(QSize(32, 32))
        self.loopButton.setMaximumSize(QSize(32, 32))
        self.loopButton.setFont(font5)
        self.loopButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.loopButton.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"	border-radius: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"    icon: url(:/assets/buttons/loop_hover.png);\n"
"}\n"
"QPushButton:pressed  {\n"
"    icon: url(:/assets/buttons/loop_pressed.png);\n"
"}\n"
"QPushButton:checked  {\n"
"    icon: url(:/assets/buttons/loop_checked.png);\n"
"}\n"
"QPushButton:disabled {\n"
"    icon: url(:/assets/buttons/loop_disabled.png);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/assets/buttons/loop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.loopButton.setIcon(icon9)
        self.loopButton.setIconSize(QSize(32, 32))
        self.loopButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.loopButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addWidget(self.BWCtopWidget)

        self.BWCbottomWidget = QWidget(self.BWcenterWidget)
        self.BWCbottomWidget.setObjectName(u"BWCbottomWidget")
        self.BWCbottomWidget.setStyleSheet(u"QLabel:disabled {\n"
"    color: transparent;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.BWCbottomWidget)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(8, 0, 8, 10)
        self.timeLabel = QLabel(self.BWCbottomWidget)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.timeLabel.sizePolicy().hasHeightForWidth())
        self.timeLabel.setSizePolicy(sizePolicy5)
        self.timeLabel.setMinimumSize(QSize(0, 17))
        self.timeLabel.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.timeLabel)

        self.playTimeSlider = HoverSlider(self.BWCbottomWidget)
        self.playTimeSlider.setObjectName(u"playTimeSlider")
        self.playTimeSlider.setEnabled(True)
        self.playTimeSlider.setMinimumSize(QSize(0, 17))
        self.playTimeSlider.setMaximumSize(QSize(700, 17))
        self.playTimeSlider.setStyleSheet(u"QSlider {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
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
"                mar"
                        "gin: -4px -3px;\n"
"                border-radius: 6px;\n"
"				}\n"
"				 QSlider::groove:horizontal:disabled {\n"
"                background: rgb(20, 20, 20); /* Grey for the background */\n"
"                }\n"
"\n"
"                QSlider::add-page:horizontal:disabled  {\n"
"                background: rgb(20, 20, 20);\n"
"                }\n"
"\n"
"                QSlider::sub-page:horizontal:disabled  {\n"
"                background: rgb(20, 20, 20);\n"
"                }\n"
"\n"
"")
        self.playTimeSlider.setMaximum(100)
        self.playTimeSlider.setTracking(True)
        self.playTimeSlider.setOrientation(Qt.Orientation.Horizontal)
        self.playTimeSlider.setInvertedAppearance(False)
        self.playTimeSlider.setInvertedControls(False)

        self.horizontalLayout_2.addWidget(self.playTimeSlider)

        self.durationLabel = QLabel(self.BWCbottomWidget)
        self.durationLabel.setObjectName(u"durationLabel")
        self.durationLabel.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.durationLabel.sizePolicy().hasHeightForWidth())
        self.durationLabel.setSizePolicy(sizePolicy5)
        self.durationLabel.setMinimumSize(QSize(0, 17))
        self.durationLabel.setStyleSheet(u"QLabel:disabled {\n"
"    color: transparent;\n"
"}")

        self.horizontalLayout_2.addWidget(self.durationLabel)


        self.verticalLayout_4.addWidget(self.BWCbottomWidget)


        self.horizontalLayout_3.addWidget(self.BWcenterWidget)

        self.BWrightWidget = QWidget(self.bottomWidget)
        self.BWrightWidget.setObjectName(u"BWrightWidget")
        sizePolicy4.setHeightForWidth(self.BWrightWidget.sizePolicy().hasHeightForWidth())
        self.BWrightWidget.setSizePolicy(sizePolicy4)
        self.BWrightWidget.setMinimumSize(QSize(230, 75))
        self.BWrightWidget.setMaximumSize(QSize(16777215, 75))
        self.BWrightWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout_5 = QHBoxLayout(self.BWrightWidget)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(8, 0, 16, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.queueButton = RoundButton(self.BWrightWidget)
        self.queueButton.setObjectName(u"queueButton")
        self.queueButton.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.queueButton.sizePolicy().hasHeightForWidth())
        self.queueButton.setSizePolicy(sizePolicy2)
        self.queueButton.setMinimumSize(QSize(32, 32))
        self.queueButton.setMaximumSize(QSize(32, 32))
        self.queueButton.setFont(font5)
        self.queueButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.queueButton.setStyleSheet(u"QPushButton {\n"
"	background-color: trasnparent;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    icon: url(:/assets/buttons/queue_hover.png);\n"
"}\n"
"\n"
"QPushButton:pressed  {\n"
"    icon: url(:/assets/buttons/queue_pressed.png);\n"
"}\n"
"\n"
"QPushButton:checked  {\n"
"    icon: url(:/assets/buttons/queue_clicked.png);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/assets/buttons/queue.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.queueButton.setIcon(icon10)
        self.queueButton.setIconSize(QSize(32, 32))
        self.queueButton.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.queueButton)

        self.volumeButton = VolumeButton(self.BWrightWidget)
        self.volumeButton.setObjectName(u"volumeButton")
        self.volumeButton.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.volumeButton.sizePolicy().hasHeightForWidth())
        self.volumeButton.setSizePolicy(sizePolicy2)
        self.volumeButton.setMinimumSize(QSize(32, 32))
        self.volumeButton.setMaximumSize(QSize(32, 32))
        self.volumeButton.setFont(font5)
        self.volumeButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.volumeButton.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"	border-radius: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"    icon: url(:/assets/buttons/volumeLow_hover.png);\n"
"}\n"
"QPushButton:pressed  {\n"
"    icon: url(:/assets/buttons/volumeLow_pressed.png);\n"
"}\n"
"QPushButton:checked  {\n"
"    icon: url(:/assets/buttons/volumeMute.png);\n"
"}\n"
"QPushButton:checked:hover  {\n"
"    icon: url(:/assets/buttons/volumeMute_hover.png);\n"
"}\n"
"QPushButton:checked:pressed  {\n"
"    icon: url(:/assets/buttons/volumeMute_pressed.png);\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/assets/buttons/volumeLow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.volumeButton.setIcon(icon11)
        self.volumeButton.setIconSize(QSize(32, 32))
        self.volumeButton.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.volumeButton)

        self.volumeSlider = HoverSlider(self.BWrightWidget)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setEnabled(True)
        self.volumeSlider.setMinimumSize(QSize(0, 17))
        self.volumeSlider.setMaximumSize(QSize(100, 17))
        self.volumeSlider.setStyleSheet(u"QSlider {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
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
"                mar"
                        "gin: -4px -3px;\n"
"                border-radius: 6px;\n"
"				}\n"
"				 QSlider::groove:horizontal:disabled {\n"
"                background: rgb(20, 20, 20); /* Grey for the background */\n"
"                }\n"
"\n"
"                QSlider::add-page:horizontal:disabled  {\n"
"                background: rgb(20, 20, 20);\n"
"                }\n"
"\n"
"                QSlider::sub-page:horizontal:disabled  {\n"
"                background: rgb(20, 20, 20);\n"
"                }\n"
"\n"
"")
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setTracking(True)
        self.volumeSlider.setOrientation(Qt.Orientation.Horizontal)
        self.volumeSlider.setInvertedAppearance(False)
        self.volumeSlider.setInvertedControls(False)

        self.horizontalLayout_5.addWidget(self.volumeSlider)


        self.horizontalLayout_3.addWidget(self.BWrightWidget)

        self.horizontalLayout_3.setStretch(1, 1)

        self.gridLayout.addWidget(self.bottomWidget, 1, 0, 1, 2)

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
        self.RSWSbackButton.setToolTip("")
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
        self.iconLabel.setText("")
        self.musicLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.artistLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
#if QT_CONFIG(tooltip)
        self.shuffleButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.shuffleButton.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.shuffleButton.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.shuffleButton.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.shuffleButton.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.shuffleButton.setText("")
#if QT_CONFIG(tooltip)
        self.previousTrackButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.previousTrackButton.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.previousTrackButton.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.previousTrackButton.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.previousTrackButton.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.previousTrackButton.setText("")
#if QT_CONFIG(tooltip)
        self.playButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.playButton.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.playButton.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.playButton.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.playButton.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.playButton.setText("")
#if QT_CONFIG(tooltip)
        self.nextTrackButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.nextTrackButton.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.nextTrackButton.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.nextTrackButton.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.nextTrackButton.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.nextTrackButton.setText("")
#if QT_CONFIG(tooltip)
        self.loopButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.loopButton.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.loopButton.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.loopButton.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.loopButton.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.loopButton.setText("")
        self.timeLabel.setText(QCoreApplication.translate("MainWindow", u"--:--", None))
        self.durationLabel.setText(QCoreApplication.translate("MainWindow", u"--:--", None))
#if QT_CONFIG(tooltip)
        self.queueButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.queueButton.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.queueButton.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.queueButton.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.queueButton.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.queueButton.setText("")
#if QT_CONFIG(tooltip)
        self.volumeButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.volumeButton.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.volumeButton.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.volumeButton.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.volumeButton.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.volumeButton.setText("")
    # retranslateUi

