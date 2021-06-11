# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1160, 880)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMouseTracking(False)
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1151, 851))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_camera = QtWidgets.QWidget()
        self.tab_camera.setObjectName("tab_camera")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_camera)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(980, 0, 160, 436))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_error = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_error.setFont(font)
        self.label_error.setObjectName("label_error")
        self.verticalLayout.addWidget(self.label_error)
        self.edit_error = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_error.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.edit_error.setFont(font)
        self.edit_error.setObjectName("edit_error")
        self.verticalLayout.addWidget(self.edit_error)
        self.label_slope = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_slope.setFont(font)
        self.label_slope.setObjectName("label_slope")
        self.verticalLayout.addWidget(self.label_slope)
        self.edit_slope = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_slope.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.edit_slope.setFont(font)
        self.edit_slope.setObjectName("edit_slope")
        self.verticalLayout.addWidget(self.edit_slope)
        self.label_sharp_curve_row = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_sharp_curve_row.setFont(font)
        self.label_sharp_curve_row.setObjectName("label_sharp_curve_row")
        self.verticalLayout.addWidget(self.label_sharp_curve_row)
        self.edit_sharp_curve_row = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_sharp_curve_row.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.edit_sharp_curve_row.setFont(font)
        self.edit_sharp_curve_row.setObjectName("edit_sharp_curve_row")
        self.verticalLayout.addWidget(self.edit_sharp_curve_row)
        self.label_miss_count = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_miss_count.setFont(font)
        self.label_miss_count.setObjectName("label_miss_count")
        self.verticalLayout.addWidget(self.label_miss_count)
        self.edit_miss_count = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_miss_count.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.edit_miss_count.setFont(font)
        self.edit_miss_count.setObjectName("edit_miss_count")
        self.verticalLayout.addWidget(self.edit_miss_count)
        self.label_roundabout = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_roundabout.setFont(font)
        self.label_roundabout.setObjectName("label_roundabout")
        self.verticalLayout.addWidget(self.label_roundabout)
        self.edit_roundabout = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_roundabout.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.edit_roundabout.setFont(font)
        self.edit_roundabout.setObjectName("edit_roundabout")
        self.verticalLayout.addWidget(self.edit_roundabout)
        self.label_three_way_fork = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_three_way_fork.setFont(font)
        self.label_three_way_fork.setObjectName("label_three_way_fork")
        self.verticalLayout.addWidget(self.label_three_way_fork)
        self.edit_three_way_fork = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_three_way_fork.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.edit_three_way_fork.setFont(font)
        self.edit_three_way_fork.setObjectName("edit_three_way_fork")
        self.verticalLayout.addWidget(self.edit_three_way_fork)
        self.label_jitter_left = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_jitter_left.setFont(font)
        self.label_jitter_left.setObjectName("label_jitter_left")
        self.verticalLayout.addWidget(self.label_jitter_left)
        self.edit_jitter_left = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_jitter_left.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.edit_jitter_left.setFont(font)
        self.edit_jitter_left.setObjectName("edit_jitter_left")
        self.verticalLayout.addWidget(self.edit_jitter_left)
        self.label_jitter_right = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_jitter_right.setFont(font)
        self.label_jitter_right.setObjectName("label_jitter_right")
        self.verticalLayout.addWidget(self.label_jitter_right)
        self.edit_jitter_right = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_jitter_right.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.edit_jitter_right.setFont(font)
        self.edit_jitter_right.setObjectName("edit_jitter_right")
        self.verticalLayout.addWidget(self.edit_jitter_right)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_camera)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(980, 650, 160, 170))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_ip = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_ip.setFont(font)
        self.label_ip.setStyleSheet("")
        self.label_ip.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ip.setObjectName("label_ip")
        self.verticalLayout_3.addWidget(self.label_ip)
        self.edit_ip_address = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.edit_ip_address.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.edit_ip_address.setFont(font)
        self.edit_ip_address.setText("")
        self.edit_ip_address.setObjectName("edit_ip_address")
        self.verticalLayout_3.addWidget(self.edit_ip_address)
        self.button_connect = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_connect.setFont(font)
        self.button_connect.setObjectName("button_connect")
        self.verticalLayout_3.addWidget(self.button_connect)
        self.button_get_one = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.button_get_one.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_get_one.setFont(font)
        self.button_get_one.setObjectName("button_get_one")
        self.verticalLayout_3.addWidget(self.button_get_one)
        self.label_time = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_time.setFont(font)
        self.label_time.setStyleSheet("")
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.setObjectName("label_time")
        self.verticalLayout_3.addWidget(self.label_time)
        self.edit_camera = QtWidgets.QTextEdit(self.tab_camera)
        self.edit_camera.setEnabled(False)
        self.edit_camera.setGeometry(QtCore.QRect(0, 0, 971, 821))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.edit_camera.setFont(font)
        self.edit_camera.setObjectName("edit_camera")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_camera)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(980, 510, 160, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_w = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_w.setFont(font)
        self.label_w.setFrameShape(QtWidgets.QFrame.Box)
        self.label_w.setAlignment(QtCore.Qt.AlignCenter)
        self.label_w.setObjectName("label_w")
        self.gridLayout.addWidget(self.label_w, 1, 1, 1, 1)
        self.label_Q = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Q.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_Q.setFont(font)
        self.label_Q.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Q.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Q.setObjectName("label_Q")
        self.gridLayout.addWidget(self.label_Q, 1, 0, 1, 1)
        self.label_D = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_D.setFont(font)
        self.label_D.setFrameShape(QtWidgets.QFrame.Box)
        self.label_D.setAlignment(QtCore.Qt.AlignCenter)
        self.label_D.setObjectName("label_D")
        self.gridLayout.addWidget(self.label_D, 2, 2, 1, 1)
        self.label_S = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_S.setFont(font)
        self.label_S.setFrameShape(QtWidgets.QFrame.Box)
        self.label_S.setAlignment(QtCore.Qt.AlignCenter)
        self.label_S.setObjectName("label_S")
        self.gridLayout.addWidget(self.label_S, 2, 1, 1, 1)
        self.label_A = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_A.setFont(font)
        self.label_A.setFrameShape(QtWidgets.QFrame.Box)
        self.label_A.setAlignment(QtCore.Qt.AlignCenter)
        self.label_A.setObjectName("label_A")
        self.gridLayout.addWidget(self.label_A, 2, 0, 1, 1)
        self.label_Esc = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Esc.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_Esc.setFont(font)
        self.label_Esc.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Esc.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Esc.setObjectName("label_Esc")
        self.gridLayout.addWidget(self.label_Esc, 0, 0, 1, 1)
        self.label_k = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_k.setFont(font)
        self.label_k.setFrameShape(QtWidgets.QFrame.Box)
        self.label_k.setAlignment(QtCore.Qt.AlignCenter)
        self.label_k.setObjectName("label_k")
        self.gridLayout.addWidget(self.label_k, 0, 2, 1, 1)
        self.label_f = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_f.setFont(font)
        self.label_f.setFrameShape(QtWidgets.QFrame.Box)
        self.label_f.setAlignment(QtCore.Qt.AlignCenter)
        self.label_f.setObjectName("label_f")
        self.gridLayout.addWidget(self.label_f, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab_camera, "")
        self.tab_paramerter = QtWidgets.QWidget()
        self.tab_paramerter.setObjectName("tab_paramerter")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_paramerter)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 20, 271, 31))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_lane_thres = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_lane_thres.sizePolicy().hasHeightForWidth())
        self.label_lane_thres.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_lane_thres.setFont(font)
        self.label_lane_thres.setFrameShape(QtWidgets.QFrame.Box)
        self.label_lane_thres.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lane_thres.setObjectName("label_lane_thres")
        self.gridLayout_2.addWidget(self.label_lane_thres, 0, 1, 1, 1)
        self.edit_lane_thres = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.edit_lane_thres.setEnabled(True)
        self.edit_lane_thres.setObjectName("edit_lane_thres")
        self.gridLayout_2.addWidget(self.edit_lane_thres, 0, 2, 1, 1)
        self.button_lane_thres = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.button_lane_thres.setObjectName("button_lane_thres")
        self.gridLayout_2.addWidget(self.button_lane_thres, 0, 3, 1, 1)
        self.gridLayoutWidget_9 = QtWidgets.QWidget(self.tab_paramerter)
        self.gridLayoutWidget_9.setGeometry(QtCore.QRect(30, 70, 271, 31))
        self.gridLayoutWidget_9.setObjectName("gridLayoutWidget_9")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_lane_distance = QtWidgets.QLabel(self.gridLayoutWidget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_lane_distance.sizePolicy().hasHeightForWidth())
        self.label_lane_distance.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_lane_distance.setFont(font)
        self.label_lane_distance.setFrameShape(QtWidgets.QFrame.Box)
        self.label_lane_distance.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lane_distance.setObjectName("label_lane_distance")
        self.gridLayout_9.addWidget(self.label_lane_distance, 0, 1, 1, 1)
        self.edit_lane_distance = QtWidgets.QLineEdit(self.gridLayoutWidget_9)
        self.edit_lane_distance.setEnabled(True)
        self.edit_lane_distance.setObjectName("edit_lane_distance")
        self.gridLayout_9.addWidget(self.edit_lane_distance, 0, 2, 1, 1)
        self.button_lane_distance = QtWidgets.QPushButton(self.gridLayoutWidget_9)
        self.button_lane_distance.setObjectName("button_lane_distance")
        self.gridLayout_9.addWidget(self.button_lane_distance, 0, 3, 1, 1)
        self.gridLayoutWidget_10 = QtWidgets.QWidget(self.tab_paramerter)
        self.gridLayoutWidget_10.setGeometry(QtCore.QRect(30, 120, 271, 31))
        self.gridLayoutWidget_10.setObjectName("gridLayoutWidget_10")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_turn_p = QtWidgets.QLabel(self.gridLayoutWidget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_turn_p.sizePolicy().hasHeightForWidth())
        self.label_turn_p.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_turn_p.setFont(font)
        self.label_turn_p.setFrameShape(QtWidgets.QFrame.Box)
        self.label_turn_p.setAlignment(QtCore.Qt.AlignCenter)
        self.label_turn_p.setObjectName("label_turn_p")
        self.gridLayout_10.addWidget(self.label_turn_p, 0, 1, 1, 1)
        self.edit_turn_p = QtWidgets.QLineEdit(self.gridLayoutWidget_10)
        self.edit_turn_p.setEnabled(True)
        self.edit_turn_p.setObjectName("edit_turn_p")
        self.gridLayout_10.addWidget(self.edit_turn_p, 0, 2, 1, 1)
        self.button_turn_p = QtWidgets.QPushButton(self.gridLayoutWidget_10)
        self.button_turn_p.setObjectName("button_turn_p")
        self.gridLayout_10.addWidget(self.button_turn_p, 0, 3, 1, 1)
        self.gridLayoutWidget_11 = QtWidgets.QWidget(self.tab_paramerter)
        self.gridLayoutWidget_11.setGeometry(QtCore.QRect(30, 170, 271, 31))
        self.gridLayoutWidget_11.setObjectName("gridLayoutWidget_11")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_turn_d = QtWidgets.QLabel(self.gridLayoutWidget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_turn_d.sizePolicy().hasHeightForWidth())
        self.label_turn_d.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_turn_d.setFont(font)
        self.label_turn_d.setFrameShape(QtWidgets.QFrame.Box)
        self.label_turn_d.setAlignment(QtCore.Qt.AlignCenter)
        self.label_turn_d.setObjectName("label_turn_d")
        self.gridLayout_11.addWidget(self.label_turn_d, 0, 1, 1, 1)
        self.edit_turn_d = QtWidgets.QLineEdit(self.gridLayoutWidget_11)
        self.edit_turn_d.setEnabled(True)
        self.edit_turn_d.setObjectName("edit_turn_d")
        self.gridLayout_11.addWidget(self.edit_turn_d, 0, 2, 1, 1)
        self.button_turn_d = QtWidgets.QPushButton(self.gridLayoutWidget_11)
        self.button_turn_d.setObjectName("button_turn_d")
        self.gridLayout_11.addWidget(self.button_turn_d, 0, 3, 1, 1)
        self.gridLayoutWidget_12 = QtWidgets.QWidget(self.tab_paramerter)
        self.gridLayoutWidget_12.setGeometry(QtCore.QRect(30, 220, 271, 31))
        self.gridLayoutWidget_12.setObjectName("gridLayoutWidget_12")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.gridLayoutWidget_12)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_sharp_jitter_thres = QtWidgets.QLabel(self.gridLayoutWidget_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_sharp_jitter_thres.sizePolicy().hasHeightForWidth())
        self.label_sharp_jitter_thres.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_sharp_jitter_thres.setFont(font)
        self.label_sharp_jitter_thres.setFrameShape(QtWidgets.QFrame.Box)
        self.label_sharp_jitter_thres.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sharp_jitter_thres.setObjectName("label_sharp_jitter_thres")
        self.gridLayout_12.addWidget(self.label_sharp_jitter_thres, 0, 1, 1, 1)
        self.edit_sharpjitter_thres = QtWidgets.QLineEdit(self.gridLayoutWidget_12)
        self.edit_sharpjitter_thres.setEnabled(True)
        self.edit_sharpjitter_thres.setObjectName("edit_sharpjitter_thres")
        self.gridLayout_12.addWidget(self.edit_sharpjitter_thres, 0, 2, 1, 1)
        self.button_sharp_jitter_thres = QtWidgets.QPushButton(self.gridLayoutWidget_12)
        self.button_sharp_jitter_thres.setObjectName("button_sharp_jitter_thres")
        self.gridLayout_12.addWidget(self.button_sharp_jitter_thres, 0, 3, 1, 1)
        self.gridLayoutWidget_13 = QtWidgets.QWidget(self.tab_paramerter)
        self.gridLayoutWidget_13.setGeometry(QtCore.QRect(30, 270, 271, 31))
        self.gridLayoutWidget_13.setObjectName("gridLayoutWidget_13")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.gridLayoutWidget_13)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_roundabout_jitter_thres_curve = QtWidgets.QLabel(self.gridLayoutWidget_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_roundabout_jitter_thres_curve.sizePolicy().hasHeightForWidth())
        self.label_roundabout_jitter_thres_curve.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_roundabout_jitter_thres_curve.setFont(font)
        self.label_roundabout_jitter_thres_curve.setFrameShape(QtWidgets.QFrame.Box)
        self.label_roundabout_jitter_thres_curve.setAlignment(QtCore.Qt.AlignCenter)
        self.label_roundabout_jitter_thres_curve.setObjectName("label_roundabout_jitter_thres_curve")
        self.gridLayout_13.addWidget(self.label_roundabout_jitter_thres_curve, 0, 1, 1, 1)
        self.edit_roundabout_jitter_thres_curve = QtWidgets.QLineEdit(self.gridLayoutWidget_13)
        self.edit_roundabout_jitter_thres_curve.setEnabled(True)
        self.edit_roundabout_jitter_thres_curve.setObjectName("edit_roundabout_jitter_thres_curve")
        self.gridLayout_13.addWidget(self.edit_roundabout_jitter_thres_curve, 0, 2, 1, 1)
        self.button_roundabout_jitter_thres_curve = QtWidgets.QPushButton(self.gridLayoutWidget_13)
        self.button_roundabout_jitter_thres_curve.setObjectName("button_roundabout_jitter_thres_curve")
        self.gridLayout_13.addWidget(self.button_roundabout_jitter_thres_curve, 0, 3, 1, 1)
        self.gridLayoutWidget_14 = QtWidgets.QWidget(self.tab_paramerter)
        self.gridLayoutWidget_14.setGeometry(QtCore.QRect(30, 320, 271, 31))
        self.gridLayoutWidget_14.setObjectName("gridLayoutWidget_14")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.gridLayoutWidget_14)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.label_roundabout_jitter_thres_straight = QtWidgets.QLabel(self.gridLayoutWidget_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_roundabout_jitter_thres_straight.sizePolicy().hasHeightForWidth())
        self.label_roundabout_jitter_thres_straight.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_roundabout_jitter_thres_straight.setFont(font)
        self.label_roundabout_jitter_thres_straight.setFrameShape(QtWidgets.QFrame.Box)
        self.label_roundabout_jitter_thres_straight.setAlignment(QtCore.Qt.AlignCenter)
        self.label_roundabout_jitter_thres_straight.setObjectName("label_roundabout_jitter_thres_straight")
        self.gridLayout_14.addWidget(self.label_roundabout_jitter_thres_straight, 0, 1, 1, 1)
        self.edit_roundabout_jitter_thres_straight = QtWidgets.QLineEdit(self.gridLayoutWidget_14)
        self.edit_roundabout_jitter_thres_straight.setEnabled(True)
        self.edit_roundabout_jitter_thres_straight.setObjectName("edit_roundabout_jitter_thres_straight")
        self.gridLayout_14.addWidget(self.edit_roundabout_jitter_thres_straight, 0, 2, 1, 1)
        self.button_roundabout_jitter_thres_straight = QtWidgets.QPushButton(self.gridLayoutWidget_14)
        self.button_roundabout_jitter_thres_straight.setObjectName("button_roundabout_jitter_thres_straight")
        self.gridLayout_14.addWidget(self.button_roundabout_jitter_thres_straight, 0, 3, 1, 1)
        self.gridLayoutWidget_15 = QtWidgets.QWidget(self.tab_paramerter)
        self.gridLayoutWidget_15.setGeometry(QtCore.QRect(30, 370, 271, 31))
        self.gridLayoutWidget_15.setObjectName("gridLayoutWidget_15")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.gridLayoutWidget_15)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.label_car_speed = QtWidgets.QLabel(self.gridLayoutWidget_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_car_speed.sizePolicy().hasHeightForWidth())
        self.label_car_speed.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_car_speed.setFont(font)
        self.label_car_speed.setFrameShape(QtWidgets.QFrame.Box)
        self.label_car_speed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_car_speed.setObjectName("label_car_speed")
        self.gridLayout_15.addWidget(self.label_car_speed, 0, 1, 1, 1)
        self.edit_car_speed = QtWidgets.QLineEdit(self.gridLayoutWidget_15)
        self.edit_car_speed.setEnabled(True)
        self.edit_car_speed.setObjectName("edit_car_speed")
        self.gridLayout_15.addWidget(self.edit_car_speed, 0, 2, 1, 1)
        self.button_car_speed = QtWidgets.QPushButton(self.gridLayoutWidget_15)
        self.button_car_speed.setObjectName("button_car_speed")
        self.gridLayout_15.addWidget(self.button_car_speed, 0, 3, 1, 1)
        self.tabWidget.addTab(self.tab_paramerter, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Smart Car Camera Viewer"))
        self.label_error.setText(_translate("MainWindow", "Error:"))
        self.label_slope.setText(_translate("MainWindow", "slope:"))
        self.label_sharp_curve_row.setText(_translate("MainWindow", "Sharp Curve Row:"))
        self.label_miss_count.setText(_translate("MainWindow", "Miss Count:"))
        self.label_roundabout.setText(_translate("MainWindow", "FlagRoundabout:"))
        self.label_three_way_fork.setText(_translate("MainWindow", "FlagThreeWayFork:"))
        self.label_jitter_left.setText(_translate("MainWindow", "laneJitterLeft"))
        self.label_jitter_right.setText(_translate("MainWindow", "laneJitterRight"))
        self.label_ip.setText(_translate("MainWindow", "IP Address:"))
        self.button_connect.setText(_translate("MainWindow", "Connect"))
        self.button_get_one.setText(_translate("MainWindow", "Get One Frame (Q)"))
        self.label_time.setText(_translate("MainWindow", "Time of Sending"))
        self.edit_camera.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:11pt;\"><br /></p></body></html>"))
        self.label_w.setText(_translate("MainWindow", "W"))
        self.label_Q.setText(_translate("MainWindow", "Q"))
        self.label_D.setText(_translate("MainWindow", "D"))
        self.label_S.setText(_translate("MainWindow", "S"))
        self.label_A.setText(_translate("MainWindow", "A"))
        self.label_Esc.setText(_translate("MainWindow", "Esc"))
        self.label_k.setText(_translate("MainWindow", "K"))
        self.label_f.setText(_translate("MainWindow", "F"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_camera), _translate("MainWindow", "Camera"))
        self.label_lane_thres.setText(_translate("MainWindow", "lane_thres"))
        self.edit_lane_thres.setText(_translate("MainWindow", "110"))
        self.button_lane_thres.setText(_translate("MainWindow", "Change"))
        self.label_lane_distance.setText(_translate("MainWindow", "lane_distance"))
        self.edit_lane_distance.setText(_translate("MainWindow", "1.7"))
        self.button_lane_distance.setText(_translate("MainWindow", "Change"))
        self.label_turn_p.setText(_translate("MainWindow", "turn_p"))
        self.edit_turn_p.setText(_translate("MainWindow", "0.5"))
        self.button_turn_p.setText(_translate("MainWindow", "Change"))
        self.label_turn_d.setText(_translate("MainWindow", "turn_d"))
        self.edit_turn_d.setText(_translate("MainWindow", "0.2"))
        self.button_turn_d.setText(_translate("MainWindow", "Change"))
        self.label_sharp_jitter_thres.setText(_translate("MainWindow", "sharpJitThr"))
        self.edit_sharpjitter_thres.setText(_translate("MainWindow", "15"))
        self.button_sharp_jitter_thres.setText(_translate("MainWindow", "Change"))
        self.label_roundabout_jitter_thres_curve.setText(_translate("MainWindow", "rouJitThrCur"))
        self.edit_roundabout_jitter_thres_curve.setText(_translate("MainWindow", "-15"))
        self.button_roundabout_jitter_thres_curve.setText(_translate("MainWindow", "Change"))
        self.label_roundabout_jitter_thres_straight.setText(_translate("MainWindow", "rouJitThrStr"))
        self.edit_roundabout_jitter_thres_straight.setText(_translate("MainWindow", "3"))
        self.button_roundabout_jitter_thres_straight.setText(_translate("MainWindow", "Change"))
        self.label_car_speed.setText(_translate("MainWindow", "car_speed"))
        self.edit_car_speed.setText(_translate("MainWindow", "30"))
        self.button_car_speed.setText(_translate("MainWindow", "Change"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_paramerter), _translate("MainWindow", "Parameter"))
