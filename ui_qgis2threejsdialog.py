# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\minorua\.qgis2\python\developing_plugins\Qgis2threejs\qgis2threejsdialog.ui'
#
# Created: Wed Mar 26 10:57:07 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Qgis2threejsDialog(object):
    def setupUi(self, Qgis2threejsDialog):
        Qgis2threejsDialog.setObjectName(_fromUtf8("Qgis2threejsDialog"))
        Qgis2threejsDialog.resize(533, 542)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Qgis2threejsDialog.sizePolicy().hasHeightForWidth())
        Qgis2threejsDialog.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(Qgis2threejsDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(Qgis2threejsDialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabDEM = QtGui.QWidget()
        self.tabDEM.setObjectName(_fromUtf8("tabDEM"))
        self.gridLayout_18 = QtGui.QGridLayout(self.tabDEM)
        self.gridLayout_18.setObjectName(_fromUtf8("gridLayout_18"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.checkBox_useDEM = QtGui.QCheckBox(self.tabDEM)
        self.checkBox_useDEM.setChecked(True)
        self.checkBox_useDEM.setTristate(False)
        self.checkBox_useDEM.setObjectName(_fromUtf8("checkBox_useDEM"))
        self.horizontalLayout_17.addWidget(self.checkBox_useDEM)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_17 = QtGui.QLabel(self.tabDEM)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_17)
        self.spinBox_demtransp = QtGui.QSpinBox(self.tabDEM)
        self.spinBox_demtransp.setEnabled(True)
        self.spinBox_demtransp.setPrefix(_fromUtf8(""))
        self.spinBox_demtransp.setMinimum(0)
        self.spinBox_demtransp.setMaximum(100)
        self.spinBox_demtransp.setSingleStep(10)
        self.spinBox_demtransp.setProperty("value", 0)
        self.spinBox_demtransp.setObjectName(_fromUtf8("spinBox_demtransp"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.spinBox_demtransp)
        self.horizontalLayout_17.addLayout(self.formLayout)
        self.verticalLayout_8.addLayout(self.horizontalLayout_17)
        self.formLayout_6 = QtGui.QFormLayout()
        self.formLayout_6.setObjectName(_fromUtf8("formLayout_6"))
        self.label_2 = QtGui.QLabel(self.tabDEM)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.comboBox_DEMLayer = QtGui.QComboBox(self.tabDEM)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_DEMLayer.sizePolicy().hasHeightForWidth())
        self.comboBox_DEMLayer.setSizePolicy(sizePolicy)
        self.comboBox_DEMLayer.setObjectName(_fromUtf8("comboBox_DEMLayer"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox_DEMLayer)
        self.verticalLayout_8.addLayout(self.formLayout_6)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.groupBox = QtGui.QGroupBox(self.tabDEM)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(10, -1, -1, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalSlider_Resolution = QtGui.QSlider(self.groupBox)
        self.horizontalSlider_Resolution.setEnabled(True)
        self.horizontalSlider_Resolution.setMinimum(1)
        self.horizontalSlider_Resolution.setMaximum(6)
        self.horizontalSlider_Resolution.setSingleStep(1)
        self.horizontalSlider_Resolution.setPageStep(1)
        self.horizontalSlider_Resolution.setProperty("value", 2)
        self.horizontalSlider_Resolution.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_Resolution.setTickPosition(QtGui.QSlider.TicksBelow)
        self.horizontalSlider_Resolution.setTickInterval(1)
        self.horizontalSlider_Resolution.setObjectName(_fromUtf8("horizontalSlider_Resolution"))
        self.horizontalLayout.addWidget(self.horizontalSlider_Resolution)
        self.label_Resolution = QtGui.QLabel(self.groupBox)
        self.label_Resolution.setMinimumSize(QtCore.QSize(80, 0))
        self.label_Resolution.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Resolution.setObjectName(_fromUtf8("label_Resolution"))
        self.horizontalLayout.addWidget(self.label_Resolution)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit_Width = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_Width.setEnabled(True)
        self.lineEdit_Width.setReadOnly(True)
        self.lineEdit_Width.setObjectName(_fromUtf8("lineEdit_Width"))
        self.horizontalLayout_3.addWidget(self.lineEdit_Width)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.lineEdit_Height = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_Height.setEnabled(True)
        self.lineEdit_Height.setReadOnly(True)
        self.lineEdit_Height.setObjectName(_fromUtf8("lineEdit_Height"))
        self.horizontalLayout_3.addWidget(self.lineEdit_Height)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_4.addWidget(self.label_8)
        self.lineEdit_HRes = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_HRes.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_HRes.sizePolicy().hasHeightForWidth())
        self.lineEdit_HRes.setSizePolicy(sizePolicy)
        self.lineEdit_HRes.setReadOnly(True)
        self.lineEdit_HRes.setObjectName(_fromUtf8("lineEdit_HRes"))
        self.horizontalLayout_4.addWidget(self.lineEdit_HRes)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_4.addWidget(self.label_9)
        self.lineEdit_VRes = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_VRes.setEnabled(True)
        self.lineEdit_VRes.setReadOnly(True)
        self.lineEdit_VRes.setObjectName(_fromUtf8("lineEdit_VRes"))
        self.horizontalLayout_4.addWidget(self.lineEdit_VRes)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.radioButton_Advanced = QtGui.QRadioButton(self.groupBox)
        self.radioButton_Advanced.setObjectName(_fromUtf8("radioButton_Advanced"))
        self.gridLayout_2.addWidget(self.radioButton_Advanced, 2, 0, 1, 1)
        self.radioButton_Simple = QtGui.QRadioButton(self.groupBox)
        self.radioButton_Simple.setChecked(True)
        self.radioButton_Simple.setObjectName(_fromUtf8("radioButton_Simple"))
        self.gridLayout_2.addWidget(self.radioButton_Simple, 0, 0, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(10, -1, -1, -1)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_5.addWidget(self.label_11)
        self.spinBox_Height = QtGui.QSpinBox(self.groupBox)
        self.spinBox_Height.setEnabled(False)
        self.spinBox_Height.setMinimum(1)
        self.spinBox_Height.setMaximum(8)
        self.spinBox_Height.setProperty("value", 5)
        self.spinBox_Height.setObjectName(_fromUtf8("spinBox_Height"))
        self.horizontalLayout_5.addWidget(self.spinBox_Height)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_5.addWidget(self.label_10)
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_5.addWidget(self.lineEdit)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_Focus = QtGui.QLabel(self.groupBox)
        self.label_Focus.setObjectName(_fromUtf8("label_Focus"))
        self.horizontalLayout_8.addWidget(self.label_Focus)
        self.toolButton_switchFocusMode = QtGui.QToolButton(self.groupBox)
        self.toolButton_switchFocusMode.setEnabled(False)
        self.toolButton_switchFocusMode.setObjectName(_fromUtf8("toolButton_switchFocusMode"))
        self.horizontalLayout_8.addWidget(self.toolButton_switchFocusMode)
        self.toolButton_PointTool = QtGui.QToolButton(self.groupBox)
        self.toolButton_PointTool.setObjectName(_fromUtf8("toolButton_PointTool"))
        self.horizontalLayout_8.addWidget(self.toolButton_PointTool)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_xmax = QtGui.QLabel(self.groupBox)
        self.label_xmax.setObjectName(_fromUtf8("label_xmax"))
        self.horizontalLayout_6.addWidget(self.label_xmax)
        self.lineEdit_xmax = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_xmax.setEnabled(False)
        self.lineEdit_xmax.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_xmax.setReadOnly(True)
        self.lineEdit_xmax.setObjectName(_fromUtf8("lineEdit_xmax"))
        self.horizontalLayout_6.addWidget(self.lineEdit_xmax)
        self.label_ymax = QtGui.QLabel(self.groupBox)
        self.label_ymax.setObjectName(_fromUtf8("label_ymax"))
        self.horizontalLayout_6.addWidget(self.label_ymax)
        self.lineEdit_ymax = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_ymax.setEnabled(False)
        self.lineEdit_ymax.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_ymax.setReadOnly(True)
        self.lineEdit_ymax.setObjectName(_fromUtf8("lineEdit_ymax"))
        self.horizontalLayout_6.addWidget(self.lineEdit_ymax)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_xmin = QtGui.QLabel(self.groupBox)
        self.label_xmin.setEnabled(True)
        self.label_xmin.setObjectName(_fromUtf8("label_xmin"))
        self.horizontalLayout_9.addWidget(self.label_xmin)
        self.lineEdit_xmin = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_xmin.setEnabled(False)
        self.lineEdit_xmin.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_xmin.setReadOnly(True)
        self.lineEdit_xmin.setObjectName(_fromUtf8("lineEdit_xmin"))
        self.horizontalLayout_9.addWidget(self.lineEdit_xmin)
        self.label_ymin = QtGui.QLabel(self.groupBox)
        self.label_ymin.setObjectName(_fromUtf8("label_ymin"))
        self.horizontalLayout_9.addWidget(self.label_ymin)
        self.lineEdit_ymin = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_ymin.setEnabled(False)
        self.lineEdit_ymin.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_ymin.setReadOnly(True)
        self.lineEdit_ymin.setObjectName(_fromUtf8("lineEdit_ymin"))
        self.horizontalLayout_9.addWidget(self.lineEdit_ymin)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 3, 0, 1, 1)
        self.verticalLayout_9.addWidget(self.groupBox)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.label_15 = QtGui.QLabel(self.tabDEM)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_18.addWidget(self.label_15)
        self.lineEdit_zFactor = QtGui.QLineEdit(self.tabDEM)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_zFactor.sizePolicy().hasHeightForWidth())
        self.lineEdit_zFactor.setSizePolicy(sizePolicy)
        self.lineEdit_zFactor.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_zFactor.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_zFactor.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_zFactor.setObjectName(_fromUtf8("lineEdit_zFactor"))
        self.horizontalLayout_18.addWidget(self.lineEdit_zFactor)
        self.label_16 = QtGui.QLabel(self.tabDEM)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_18.addWidget(self.label_16)
        self.spinBox_sidetransp = QtGui.QSpinBox(self.tabDEM)
        self.spinBox_sidetransp.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_sidetransp.sizePolicy().hasHeightForWidth())
        self.spinBox_sidetransp.setSizePolicy(sizePolicy)
        self.spinBox_sidetransp.setPrefix(_fromUtf8(""))
        self.spinBox_sidetransp.setMinimum(0)
        self.spinBox_sidetransp.setMaximum(100)
        self.spinBox_sidetransp.setSingleStep(10)
        self.spinBox_sidetransp.setProperty("value", 0)
        self.spinBox_sidetransp.setObjectName(_fromUtf8("spinBox_sidetransp"))
        self.horizontalLayout_18.addWidget(self.spinBox_sidetransp)
        self.verticalLayout_9.addLayout(self.horizontalLayout_18)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem4)
        self.gridLayout_18.addLayout(self.verticalLayout_9, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabDEM, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.treeWidget_VectorLayers = QtGui.QTreeWidget(self.tab_2)
        self.treeWidget_VectorLayers.setObjectName(_fromUtf8("treeWidget_VectorLayers"))
        self.treeWidget_VectorLayers.headerItem().setText(0, _fromUtf8("1"))
        self.gridLayout_6.addWidget(self.treeWidget_VectorLayers, 0, 0, 1, 1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.scrollArea = QtGui.QScrollArea(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(240, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 238, 368))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_10 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.groupBox_zCoordinate = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_zCoordinate.setObjectName(_fromUtf8("groupBox_zCoordinate"))
        self.gridLayout_9 = QtGui.QGridLayout(self.groupBox_zCoordinate)
        self.gridLayout_9.setMargin(3)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.verticalLayout_zCoordinate = QtGui.QVBoxLayout()
        self.verticalLayout_zCoordinate.setObjectName(_fromUtf8("verticalLayout_zCoordinate"))
        self.gridLayout_9.addLayout(self.verticalLayout_zCoordinate, 1, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_zCoordinate, 0, 0, 1, 1)
        self.groupBox_Styles = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_Styles.sizePolicy().hasHeightForWidth())
        self.groupBox_Styles.setSizePolicy(sizePolicy)
        self.groupBox_Styles.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_Styles.setObjectName(_fromUtf8("groupBox_Styles"))
        self.gridLayout_8 = QtGui.QGridLayout(self.groupBox_Styles)
        self.gridLayout_8.setMargin(3)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.verticalLayout_Styles = QtGui.QVBoxLayout()
        self.verticalLayout_Styles.setObjectName(_fromUtf8("verticalLayout_Styles"))
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.label_ObjectType = QtGui.QLabel(self.groupBox_Styles)
        self.label_ObjectType.setMinimumSize(QtCore.QSize(60, 0))
        self.label_ObjectType.setObjectName(_fromUtf8("label_ObjectType"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_ObjectType)
        self.comboBox_ObjectType = QtGui.QComboBox(self.groupBox_Styles)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_ObjectType.sizePolicy().hasHeightForWidth())
        self.comboBox_ObjectType.setSizePolicy(sizePolicy)
        self.comboBox_ObjectType.setObjectName(_fromUtf8("comboBox_ObjectType"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox_ObjectType)
        self.verticalLayout_Styles.addLayout(self.formLayout_4)
        self.gridLayout_8.addLayout(self.verticalLayout_Styles, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_Styles, 1, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem5, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_5.addWidget(self.scrollArea)
        self.gridLayout_6.addLayout(self.verticalLayout_5, 0, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_MapCanvasExtent = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_MapCanvasExtent.setEnabled(True)
        self.lineEdit_MapCanvasExtent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_MapCanvasExtent.setReadOnly(True)
        self.lineEdit_MapCanvasExtent.setObjectName(_fromUtf8("lineEdit_MapCanvasExtent"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_MapCanvasExtent)
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_MapCanvasSize = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_MapCanvasSize.setEnabled(True)
        self.lineEdit_MapCanvasSize.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_MapCanvasSize.setReadOnly(True)
        self.lineEdit_MapCanvasSize.setObjectName(_fromUtf8("lineEdit_MapCanvasSize"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_MapCanvasSize)
        self.gridLayout_3.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 0, 0, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem6, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.label_3 = QtGui.QLabel(Qgis2threejsDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEdit_OutputFilename = QtGui.QLineEdit(Qgis2threejsDialog)
        self.lineEdit_OutputFilename.setObjectName(_fromUtf8("lineEdit_OutputFilename"))
        self.horizontalLayout_2.addWidget(self.lineEdit_OutputFilename)
        self.toolButton_Browse = QtGui.QToolButton(Qgis2threejsDialog)
        self.toolButton_Browse.setObjectName(_fromUtf8("toolButton_Browse"))
        self.horizontalLayout_2.addWidget(self.toolButton_Browse)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.progressBar = QtGui.QProgressBar(Qgis2threejsDialog)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout_7.addWidget(self.progressBar)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.pushButton_Run = QtGui.QPushButton(Qgis2threejsDialog)
        self.pushButton_Run.setDefault(True)
        self.pushButton_Run.setObjectName(_fromUtf8("pushButton_Run"))
        self.horizontalLayout_7.addWidget(self.pushButton_Run)
        self.pushButton_Close = QtGui.QPushButton(Qgis2threejsDialog)
        self.pushButton_Close.setObjectName(_fromUtf8("pushButton_Close"))
        self.horizontalLayout_7.addWidget(self.pushButton_Close)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label = QtGui.QLabel(Qgis2threejsDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.comboBox_Template = QtGui.QComboBox(Qgis2threejsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_Template.sizePolicy().hasHeightForWidth())
        self.comboBox_Template.setSizePolicy(sizePolicy)
        self.comboBox_Template.setObjectName(_fromUtf8("comboBox_Template"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox_Template)
        self.gridLayout.addLayout(self.formLayout_3, 2, 0, 1, 1)

        self.retranslateUi(Qgis2threejsDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Qgis2threejsDialog)

    def retranslateUi(self, Qgis2threejsDialog):
        Qgis2threejsDialog.setWindowTitle(_translate("Qgis2threejsDialog", "Qgis2threejs", None))
        self.checkBox_useDEM.setText(_translate("Qgis2threejsDialog", "Use a DEM Layer", None))
        self.label_17.setText(_translate("Qgis2threejsDialog", "DEM transparency (%)", None))
        self.label_2.setText(_translate("Qgis2threejsDialog", "DEM Layer", None))
        self.groupBox.setTitle(_translate("Qgis2threejsDialog", "Resampling", None))
        self.label_Resolution.setText(_translate("Qgis2threejsDialog", "about 200 x 200 px", None))
        self.label_4.setText(_translate("Qgis2threejsDialog", "Columns", None))
        self.label_5.setText(_translate("Qgis2threejsDialog", "Rows", None))
        self.label_8.setText(_translate("Qgis2threejsDialog", "X resolution", None))
        self.label_9.setText(_translate("Qgis2threejsDialog", "Y resolution", None))
        self.radioButton_Advanced.setText(_translate("Qgis2threejsDialog", "Advanced (multiple resolutions)", None))
        self.radioButton_Simple.setText(_translate("Qgis2threejsDialog", "Simple", None))
        self.label_11.setText(_translate("Qgis2threejsDialog", "Quad tree height", None))
        self.label_10.setText(_translate("Qgis2threejsDialog", "Quad size", None))
        self.lineEdit.setText(_translate("Qgis2threejsDialog", "64", None))
        self.label_Focus.setText(_translate("Qgis2threejsDialog", "Focus point", None))
        self.toolButton_switchFocusMode.setText(_translate("Qgis2threejsDialog", "switch selection mode", None))
        self.toolButton_PointTool.setText(_translate("Qgis2threejsDialog", "Get point from map canvas", None))
        self.label_xmax.setText(_translate("Qgis2threejsDialog", "x", None))
        self.label_ymax.setText(_translate("Qgis2threejsDialog", "y", None))
        self.label_xmin.setText(_translate("Qgis2threejsDialog", "xmin", None))
        self.label_ymin.setText(_translate("Qgis2threejsDialog", "ymin", None))
        self.label_15.setText(_translate("Qgis2threejsDialog", "Vertical exaggeration", None))
        self.lineEdit_zFactor.setText(_translate("Qgis2threejsDialog", "1.5", None))
        self.label_16.setText(_translate("Qgis2threejsDialog", "Sides transparency (%)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDEM), _translate("Qgis2threejsDialog", "DEM", None))
        self.groupBox_zCoordinate.setTitle(_translate("Qgis2threejsDialog", "Z coordinate", None))
        self.groupBox_Styles.setTitle(_translate("Qgis2threejsDialog", "Styles", None))
        self.label_ObjectType.setText(_translate("Qgis2threejsDialog", "Object type", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Qgis2threejsDialog", "Vector", None))
        self.groupBox_2.setTitle(_translate("Qgis2threejsDialog", "Current map canvas", None))
        self.label_6.setText(_translate("Qgis2threejsDialog", "Extent", None))
        self.label_7.setText(_translate("Qgis2threejsDialog", "Size", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Qgis2threejsDialog", "Information", None))
        self.label_3.setText(_translate("Qgis2threejsDialog", "Output HTML file path", None))
        self.toolButton_Browse.setText(_translate("Qgis2threejsDialog", "Browse...", None))
        self.progressBar.setFormat(_translate("Qgis2threejsDialog", "%p%", None))
        self.pushButton_Run.setText(_translate("Qgis2threejsDialog", "Run", None))
        self.pushButton_Close.setText(_translate("Qgis2threejsDialog", "Close", None))
        self.label.setText(_translate("Qgis2threejsDialog", "Template file", None))

