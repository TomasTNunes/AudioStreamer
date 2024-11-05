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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

from coverlabel import CoverLabel
from elidedlabel import ElidedLabel
import resources_rc

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
        SearchTrackWidgetBase.setMaximumSize(QSize(16777215, 56))
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
        self.gridLayout_2.setContentsMargins(9, 8, 16, 8)
        self.iconLabel = CoverLabel(self.SearchTrackWidget)
        self.iconLabel.setObjectName(u"iconLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.iconLabel.sizePolicy().hasHeightForWidth())
        self.iconLabel.setSizePolicy(sizePolicy1)
        self.iconLabel.setMinimumSize(QSize(40, 40))
        self.iconLabel.setMaximumSize(QSize(40, 40))
        self.iconLabel.setStyleSheet(u"background-color: none;\n"
"border-radius: 4px;")

        self.gridLayout_2.addWidget(self.iconLabel, 0, 0, 2, 1)

        self.musicLabel = ElidedLabel(self.SearchTrackWidget)
        self.musicLabel.setObjectName(u"musicLabel")
        sizePolicy.setHeightForWidth(self.musicLabel.sizePolicy().hasHeightForWidth())
        self.musicLabel.setSizePolicy(sizePolicy)
        self.musicLabel.setMinimumSize(QSize(0, 21))
        self.musicLabel.setMaximumSize(QSize(16777215, 21))
        font = QFont()
        font.setFamilies([u"Segoe UI Black"])
        font.setPointSize(11)
        font.setBold(True)
        self.musicLabel.setFont(font)
        self.musicLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: None;\n"
"")

        self.gridLayout_2.addWidget(self.musicLabel, 0, 1, 1, 1)

        self.STWHLayout = QHBoxLayout()
        self.STWHLayout.setSpacing(16)
        self.STWHLayout.setObjectName(u"STWHLayout")
        self.STWHLayout.setContentsMargins(0, -1, -1, -1)
        self.durationLabel = QLabel(self.SearchTrackWidget)
        self.durationLabel.setObjectName(u"durationLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.durationLabel.sizePolicy().hasHeightForWidth())
        self.durationLabel.setSizePolicy(sizePolicy2)
        self.durationLabel.setMinimumSize(QSize(0, 19))
        self.durationLabel.setMaximumSize(QSize(16777215, 19))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        self.durationLabel.setFont(font1)
        self.durationLabel.setStyleSheet(u"QLabel {\n"
"   color: rgb(180, 180, 180);\n"
"	background-color: none;\n"
"}")

        self.STWHLayout.addWidget(self.durationLabel)

        self.optiosnsButton = QPushButton(self.SearchTrackWidget)
        self.optiosnsButton.setObjectName(u"optiosnsButton")
        self.optiosnsButton.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.optiosnsButton.sizePolicy().hasHeightForWidth())
        self.optiosnsButton.setSizePolicy(sizePolicy1)
        self.optiosnsButton.setMinimumSize(QSize(16, 32))
        self.optiosnsButton.setMaximumSize(QSize(16, 32))
        self.optiosnsButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.optiosnsButton.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"	border-radius: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"    icon: url(:/assets/buttons/options_hover.png);\n"
"}\n"
"QPushButton:pressed  {\n"
"    icon: url(:/assets/buttons/options_pressed.png);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/assets/buttons/options.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.optiosnsButton.setIcon(icon)
        self.optiosnsButton.setIconSize(QSize(16, 32))

        self.STWHLayout.addWidget(self.optiosnsButton)


        self.gridLayout_2.addLayout(self.STWHLayout, 0, 8, 2, 1)

        self.artistLabel = ElidedLabel(self.SearchTrackWidget)
        self.artistLabel.setObjectName(u"artistLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.artistLabel.sizePolicy().hasHeightForWidth())
        self.artistLabel.setSizePolicy(sizePolicy3)
        self.artistLabel.setMinimumSize(QSize(0, 19))
        self.artistLabel.setMaximumSize(QSize(16777215, 19))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setUnderline(False)
        self.artistLabel.setFont(font2)
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

        self.Hspacer = QSpacerItem(302, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.Hspacer, 0, 2, 2, 1)

        self.gridLayout_2.setColumnStretch(1, 2)
        self.gridLayout_2.setColumnStretch(2, 1)

        self.gridLayout.addWidget(self.SearchTrackWidget, 0, 0, 1, 1)


        self.retranslateUi(SearchTrackWidgetBase)

        QMetaObject.connectSlotsByName(SearchTrackWidgetBase)
    # setupUi

    def retranslateUi(self, SearchTrackWidgetBase):
        SearchTrackWidgetBase.setWindowTitle(QCoreApplication.translate("SearchTrackWidgetBase", u"Form", None))
        self.iconLabel.setText("")
        self.musicLabel.setText(QCoreApplication.translate("SearchTrackWidgetBase", u"TextLabel", None))
        self.durationLabel.setText(QCoreApplication.translate("SearchTrackWidgetBase", u"--:--", None))
        self.optiosnsButton.setText("")
        self.artistLabel.setText(QCoreApplication.translate("SearchTrackWidgetBase", u"TextLabel", None))
    # retranslateUi

