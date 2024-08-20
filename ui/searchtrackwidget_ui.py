# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'searchtrackwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_SearchTrackWidgetBase(object):
    def setupUi(self, SearchTrackWidgetBase):
        if not SearchTrackWidgetBase.objectName():
            SearchTrackWidgetBase.setObjectName(u"SearchTrackWidgetBase")
        SearchTrackWidgetBase.resize(458, 56)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SearchTrackWidgetBase.sizePolicy().hasHeightForWidth())
        SearchTrackWidgetBase.setSizePolicy(sizePolicy)
        SearchTrackWidgetBase.setStyleSheet(u"border-radius: 4px;")
        self.gridLayout = QGridLayout(SearchTrackWidgetBase)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.SearchTrackWidget = QWidget(SearchTrackWidgetBase)
        self.SearchTrackWidget.setObjectName(u"SearchTrackWidget")
        sizePolicy.setHeightForWidth(self.SearchTrackWidget.sizePolicy().hasHeightForWidth())
        self.SearchTrackWidget.setSizePolicy(sizePolicy)
        self.SearchTrackWidget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.SearchTrackWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(8)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(8, 8, 16, 8)
        self.iconLabel = QLabel(self.SearchTrackWidget)
        self.iconLabel.setObjectName(u"iconLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.iconLabel.sizePolicy().hasHeightForWidth())
        self.iconLabel.setSizePolicy(sizePolicy1)
        self.iconLabel.setMinimumSize(QSize(40, 40))
        self.iconLabel.setStyleSheet(u"background-color: rgb(0, 170, 0);\n"
"border-radius: 4px;")

        self.gridLayout_2.addWidget(self.iconLabel, 0, 0, 2, 1)

        self.musicLabel = QLabel(self.SearchTrackWidget)
        self.musicLabel.setObjectName(u"musicLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.musicLabel.sizePolicy().hasHeightForWidth())
        self.musicLabel.setSizePolicy(sizePolicy2)
        self.musicLabel.setMinimumSize(QSize(0, 22))
        self.musicLabel.setMaximumSize(QSize(16777215, 22))
        font = QFont()
        font.setFamilies([u"Segoe UI Black"])
        font.setPointSize(11)
        font.setBold(True)
        self.musicLabel.setFont(font)
        self.musicLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: none;")

        self.gridLayout_2.addWidget(self.musicLabel, 0, 1, 1, 1)

        self.Hspacer = QSpacerItem(302, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.Hspacer, 0, 2, 2, 1)

        self.artistLabel = QLabel(self.SearchTrackWidget)
        self.artistLabel.setObjectName(u"artistLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.artistLabel.sizePolicy().hasHeightForWidth())
        self.artistLabel.setSizePolicy(sizePolicy3)
        self.artistLabel.setMinimumSize(QSize(0, 20))
        self.artistLabel.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setUnderline(False)
        self.artistLabel.setFont(font1)
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

        self.gridLayout_2.addWidget(self.artistLabel, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.SearchTrackWidget, 0, 0, 1, 1)


        self.retranslateUi(SearchTrackWidgetBase)

        QMetaObject.connectSlotsByName(SearchTrackWidgetBase)
    # setupUi

    def retranslateUi(self, SearchTrackWidgetBase):
        SearchTrackWidgetBase.setWindowTitle(QCoreApplication.translate("SearchTrackWidgetBase", u"Form", None))
        self.iconLabel.setText("")
        self.musicLabel.setText(QCoreApplication.translate("SearchTrackWidgetBase", u"TextLabel", None))
        self.artistLabel.setText(QCoreApplication.translate("SearchTrackWidgetBase", u"TextLabel", None))
    # retranslateUi

