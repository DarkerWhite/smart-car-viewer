# -*- coding: utf-8 -*-

import sys
import time
import socket
import configparser
from pathlib import Path
from functools import partial
from main_ui import Ui_MainWindow
from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt

from tcpCommon import sendMsg, server_data_is_ready, server_is_working, getTime

class Ui_MainWindow_Son(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        self.timer_key_command = QtCore.QTimer()

        self.slot_init()
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")
        self.get_config_history()

        self.tcp_connection_control = False
        self.tcp_connection_camera = False

        self.flag_get_frame_mode = 0
        self.getting_pic = False
        self.data_is_ready = 0
        self.need_clean = 0

        self.keyboard_command_dict = {
            Qt.Key_W: "CON@Forward\n",        # w - forward
            Qt.Key_A: "CON@Left\n",           # a - left
            Qt.Key_S: "CON@Backward\n",       # s - backward
            Qt.Key_D: "CON@Right\n",          # r - right
            Qt.Key_K: "CON@car_go\n",           # k - start
            Qt.Key_Escape: "CON@car_stop\n",     # esc - exit control mode
            Qt.Key_G: "CAM@Dog\n",          # g - release dog to bite camera!
            Qt.Key_T: "CON@Dog\n",          # t - release dog to bite control!
            Qt.Key_F: "CAM@ClearElement\n",          # f - clear flag
        }

        # bytes type: need to be send
        # function type: [need to be send, key is pressed]
        self.keyboard_status_dict = {
            Qt.Key_W: False,
            Qt.Key_A: False,
            Qt.Key_S: False,
            Qt.Key_D: False,
            Qt.Key_K: False,
            Qt.Key_Escape: False,
            Qt.Key_G: False,
            Qt.Key_T: False,
            Qt.Key_F: False
        }

        self.parameter_button_status_dict = {
            self.button_lane_thres: False,
            self.button_lane_distance: False,
            self.button_turn_p: False,
            self.button_turn_d: False,
            self.button_sharp_jitter_thres: False,
            self.button_roundabout_jitter_thres_curve: False,
            self.button_roundabout_jitter_thres_straight: False,
            self.button_car_speed: False,
            self.button_speed_p: False,
            self.button_speed_i: False,
            self.button_speed_d: False
        }

        self.parameter_button_command_dict = {
            # lane thres
            # uint16 pixelMeanThres
            self.button_lane_thres: lambda: f"CAM@laTh:{int(self.edit_lane_thres.text())}\n",
            # lane distance
            # float detectDistance
            self.button_lane_distance: lambda: f"CAM@laDs:{format(self.edit_lane_distance.text().replace('.', ''), '0>2')[:2]}\n",
            # sharpcurve Jitter Thres
            # int16 sharpCurveJitterThres
            self.button_sharp_jitter_thres: lambda: f"CAM@ch sJTh {format(self.edit_sharpjitter_thres.text(), '0>3')[:3]}\n",
            # car speed
            # int16 basic_speed
            self.button_car_speed: lambda: f"CON@Car_Speed:{int(self.edit_car_speed.text())}\n",

            # turn - kp
            # float kp
            self.button_turn_p: lambda: f"CON@Turn_Kp:{str(int(float(self.edit_turn_p.text())*1000)).replace('.', '')}\n",
            # turn - kd
            self.button_turn_d: lambda: f"CON@Turn_Kd:{str(int(float(self.edit_turn_d.text())*1000)).replace('.', '')}\n",

            # roundabout jitter curve thres
            self.button_roundabout_jitter_thres_curve: lambda: f"CAM@ch roJC {format(self.edit_roundabout_jitter_thres_curve.text(), '0>3')[:3]}\n",
            # roundabout jitter straight thres
            self.button_roundabout_jitter_thres_straight: lambda: f"CAM@ch roJS {format(self.edit_roundabout_jitter_thres_straight.text(), '0>3')[:3]}\n",

            self.button_speed_p: lambda: f"CON@ch spdP {self.edit_speed_p.text()}",
            self.button_speed_i: lambda: f"CON@ch spdI {self.edit_speed_i.text()}",
            self.button_speed_d: lambda: f"CON@ch spdD {self.edit_speed_d.text()}",
        }

        self.button_to_edit_dict = {
            self.button_lane_thres: self.edit_lane_thres,
            self.button_lane_distance: self.edit_lane_distance,
            self.button_turn_p: self.edit_turn_p,
            self.button_turn_d: self.edit_turn_d,
            self.button_sharp_jitter_thres: self.edit_sharpjitter_thres,
            self.button_roundabout_jitter_thres_curve: self.edit_roundabout_jitter_thres_curve,
            self.button_roundabout_jitter_thres_straight: self.edit_roundabout_jitter_thres_straight,
            self.button_car_speed: self.edit_car_speed
        }

        self.button_sharp_jitter_thres.setEnabled(False)
        self.button_roundabout_jitter_thres_curve.setEnabled(False)
        self.button_roundabout_jitter_thres_straight.setEnabled(False)

    def get_config_history(self):
        self.edit_ip_address_control.setText(self.config['ip']['control_core'])
        self.edit_ip_address_camera.setText(self.config['ip']['camera_core'])

        self.edit_lane_thres.setText(self.config['parameter_camera']['lane_thres'])
        self.edit_lane_distance.setText(self.config['parameter_camera']['lane_distance'])
        self.edit_sharpjitter_thres.setText(self.config['parameter_camera']['sharpJitThr'])
        self.edit_roundabout_jitter_thres_curve.setText(self.config['parameter_camera']['rouJitThrCur'])
        self.edit_roundabout_jitter_thres_straight.setText(self.config['parameter_camera']['rouJitThrStr'])

        self.edit_turn_p.setText(self.config['parameter_turning_loop']['turn_kp'])
        self.edit_turn_d.setText(self.config['parameter_turning_loop']['turn_kd'])

        self.edit_speed_p.setText(self.config['parameter_speed_loop']['speed_kp'])
        self.edit_speed_i.setText(self.config['parameter_speed_loop']['speed_ki'])
        self.edit_speed_d.setText(self.config['parameter_speed_loop']['speed_kd'])

        self.edit_car_speed.setText(self.config['parameter_control']['car_speed'])

    def keyPressEvent(self, e):
        if e.key() in self.keyboard_command_dict:
            self.keyboard_status_dict[e.key()] = True
        if e.key() == 81:
            self.flag_get_frame_mode = 1

    def keyReleaseEvent(self, e):
        pass

    def slot_init(self):
        # main panel button
        self.button_connect_control.clicked.connect(self.toggle_connection_control)
        self.button_connect_camera.clicked.connect(self.toggle_connection_camera)
        self.edit_ip_address_control.returnPressed.connect(self.toggle_connection_control)
        self.edit_ip_address_camera.returnPressed.connect(self.toggle_connection_camera)

        self.button_get_one.clicked.connect(self.get_one_frame)

        self.timer_key_command.timeout.connect(self.scan_and_send_command)
        self.timer_key_command.start(50)

        self.button_remote_camera.clicked.connect(self.open_remote_camera)

        # parameter button
        self.button_lane_thres.clicked.connect(partial(self.handle_parameter_key, self.button_lane_thres))
        self.button_lane_distance.clicked.connect(partial(self.handle_parameter_key, self.button_lane_distance))
        self.button_turn_p.clicked.connect(partial(self.handle_parameter_key, self.button_turn_p))
        self.button_turn_d.clicked.connect(partial(self.handle_parameter_key, self.button_turn_d))
        self.button_sharp_jitter_thres.clicked.connect(partial(self.handle_parameter_key, self.button_sharp_jitter_thres))
        self.button_roundabout_jitter_thres_curve.clicked.connect(partial(self.handle_parameter_key, self.button_roundabout_jitter_thres_curve))
        self.button_roundabout_jitter_thres_straight.clicked.connect(partial(self.handle_parameter_key, self.button_roundabout_jitter_thres_straight))
        self.button_car_speed.clicked.connect(partial(self.handle_parameter_key, self.button_car_speed))

        # bind edit to return key
        self.edit_lane_thres.returnPressed.connect(partial(self.handle_parameter_key, self.button_lane_thres))
        self.edit_lane_distance.returnPressed.connect(partial(self.handle_parameter_key, self.button_lane_distance))
        self.edit_turn_p.returnPressed.connect(partial(self.handle_parameter_key, self.button_turn_p))
        self.edit_turn_d.returnPressed.connect(partial(self.handle_parameter_key, self.button_turn_d))
        self.edit_sharpjitter_thres.returnPressed.connect(partial(self.handle_parameter_key, self.button_sharp_jitter_thres))
        self.edit_roundabout_jitter_thres_curve.returnPressed.connect(partial(self.handle_parameter_key, self.button_roundabout_jitter_thres_curve))
        self.edit_roundabout_jitter_thres_straight.returnPressed.connect(partial(self.handle_parameter_key, self.button_roundabout_jitter_thres_straight))
        self.edit_car_speed.returnPressed.connect(partial(self.handle_parameter_key, self.button_car_speed))

    def open_remote_camera(self):
        try:
            from remote_camera import remoteCamera
            self.ui_remote_camera = remoteCamera()
            self.ui_remote_camera.show_remote_camera_window()
        except ImportError:
            self.edit_camera.append(f"[{getTime()}]: Import error, may due to the lack of cv2 in this python environment.")

    def handle_parameter_key(self, btn):
        print(f"pressed {self.parameter_button_command_dict[btn]()}")
        self.parameter_button_status_dict[btn] = True

    def toggle_connection_control(self):
        if not self.tcp_connection_control:
            reply_control = sendMsg(
                (self.edit_ip_address_control, self.edit_ip_address_camera),
                (self.tcp_connection_control, self.tcp_connection_camera),
                "CON@init\n",
                output_edit=self.edit_log_control,
                wait_reply=True
            )

            if reply_control == "control\n":
                self.tcp_connection_control = True
                self.edit_ip_address_control.setEnabled(False)
                self.button_connect_control.setText("Disconnect")
                self.edit_log_control.append(f"{getTime()}: Successfull.")
        else:
            self.tcp_connection_control = False
            self.edit_ip_address_control.setEnabled(True)
            self.button_connect_control.setText("Connect")

    def toggle_connection_camera(self):
        if not self.tcp_connection_camera:
            reply_camera = sendMsg(
                (self.edit_ip_address_control, self.edit_ip_address_camera),
                (self.tcp_connection_control, self.tcp_connection_camera),
                "CAM@init\n",
                output_edit=self.edit_log_control,
                wait_reply=True
            )

            if reply_camera == "camera\n":
                self.tcp_connection_camera = True
                self.edit_ip_address_camera.setEnabled(False)
                self.button_connect_camera.setText("Disconnect")
                self.edit_log_control.append(f"{getTime()}: Successfull.")
                self.button_get_one.setEnabled(True)
        else:
            self.tcp_connection_camera = False
            self.edit_ip_address_camera.setEnabled(True)
            self.button_get_one.setEnabled(False)
            self.button_connect_camera.setText("Connect")

    def get_one_frame(self):
        self.flag_get_frame_mode = 1

    def decode_dataset(self):
        string_list = []
        for row in range(50):
            #print("row", row)
            if (int(self.dataDict['detectLeft'][row]) and int(self.dataDict['detectRight'][row])):
                color_row = '<font color="black">'
            elif (int(self.dataDict['detectLeft'][row]) and not int(self.dataDict['detectRight'][row])):
                color_row = '<font color="red">'
            elif (not int(self.dataDict['detectLeft'][row]) and int(self.dataDict['detectRight'][row])):
                color_row = '<font color="blue">'
            elif (not int(self.dataDict['detectLeft'][row]) and not int(self.dataDict['detectRight'][row])):
                color_row = '<font color="green">'
            if (row < 10):
                string_row_head = color_row + f'<font color="white">0</font>{row}' + "</font>"
            else:
                string_row_head = color_row + f"{row}" + "</font>"

            if int(self.dataDict['laneLeft'][row]) >= 0:
                string_row_body = (int(self.dataDict['laneLeft'][row])) * "&nbsp;" + "L"
            else:
                string_row_body = ""
                self.dataDict['laneLeft'][row] = 0

            if int(self.dataDict['laneCenter'][row]) >= 0:
                string_row_body += (int(self.dataDict['laneCenter'][row]) - int(self.dataDict['laneLeft'][row])) * "&nbsp;" + "|"
            else:
                self.dataDict['laneCenter'][row] = 0

            if int(self.dataDict['laneRight'][row]) >= 0:
                string_row_body += (int(self.dataDict['laneRight'][row]) - int(self.dataDict['laneCenter'][row])) * "&nbsp;" + "R<br>"

            string_list.append(string_row_head + string_row_body)

        self.string_total = "".join(string_list)
        self.data_is_ready = 1

    def get_frame(self):
        self.button_get_one.setEnabled(False)
        self.button_get_one.setText("Getting Frame...")
        recv = sendMsg(
            (self.edit_ip_address_control, self.edit_ip_address_camera),
            (self.tcp_connection_control, self.tcp_connection_camera),
            "CAM@ShowCamera\n",
            output_edit=self.edit_camera,
            wait_reply=True
        )
        if recv != -1:
            print(recv)
            recv = recv[:-1].split(",")
            try:
                self.dataDict = {
                    "laneLeft": recv[0][:-1].split(" "),
                    "laneRight": recv[1][:-1].split(" "),
                    "laneCenter": recv[2][:-1].split(" "),
                    "detectLeft": recv[3][:-1].split(" "),
                    "detectRight": recv[4][:-1].split(" "),
                    "status": recv[5][:-1].split(" ")
                }
            except IndexError:
                self.edit_camera.setText(f"{getTime()}: Get camera frame failed, index error.")
                self.button_get_one.setText("Get One Frame")
                self.button_get_one.setEnabled(True)

                self.flag_get_frame_mode = 0
                return -1
            print(self.dataDict)

            self.decode_dataset()

            self.edit_camera.setText(self.string_total)
            self.edit_error.setText(str(int(self.dataDict['status'][0])))
            self.edit_slope.setText(str(int(self.dataDict['status'][1])))
            self.edit_sharp_curve_row.setText(str(int(self.dataDict['status'][2])))
            self.edit_miss_count.setText(str(int(self.dataDict['status'][3])))
            self.edit_roundabout.setText(str(int(self.dataDict['status'][4])))
            self.edit_three_way_fork.setText(str(int(self.dataDict['status'][5])))
            self.edit_jitter_left.setText(str(float(self.dataDict['status'][6]) / 100))
            self.edit_jitter_right.setText(str(float(self.dataDict['status'][7]) / 100))

            #current_time = time.strftime("%H:%M:%S", time.localtime())
            #self.label_time.setText(current_time)

            self.button_get_one.setText("Get One Frame")
            self.button_get_one.setEnabled(True)

            self.flag_get_frame_mode = 0
        else:
            self.edit_camera.setText(f"{getTime()}: Get camera frame failed.")
            self.button_get_one.setText("Get One Frame")
            self.button_get_one.setEnabled(True)

            self.flag_get_frame_mode = 0

    def scan_and_send_command(self):
        for i in self.keyboard_status_dict:
            if self.keyboard_status_dict[i]:
                sendMsg(
                    (self.edit_ip_address_control, self.edit_ip_address_camera),
                    (self.tcp_connection_control, self.tcp_connection_camera),
                    self.keyboard_command_dict[i],
                    output_edit=self.edit_log_control,
                    wait_reply=True
                )
                self.keyboard_status_dict[i] = False

        for i in self.parameter_button_status_dict:
            if self.parameter_button_status_dict[i]:
                recv = sendMsg(
                    (self.edit_ip_address_control, self.edit_ip_address_camera),
                    (self.tcp_connection_control, self.tcp_connection_camera),
                    self.parameter_button_command_dict[i](),
                    output_edit=self.edit_log_parameter,
                    wait_reply=True
                )
                if recv == -1:
                    print("change parameter failed")
                    #self.button_to_edit_dict[i].setText(str(recv))
                self.parameter_button_status_dict[i] = False

        if self.flag_get_frame_mode == 1:
            self.get_frame()
            self.flag_get_frame_mode = 0

    def closeEvent(self, *args, **kwargs):
        super(QtWidgets.QMainWindow, self).closeEvent(*args, **kwargs)
        self.config['ip']['control_core'] = self.edit_ip_address_control.text()
        self.config['ip']['camera_core'] = self.edit_ip_address_camera.text()

        self.config['parameter_camera']['lane_thres'] = self.edit_lane_thres.text()
        self.config['parameter_camera']['lane_distance'] = self.edit_lane_distance.text()
        self.config['parameter_camera']['sharpJitThr'] = self.edit_sharpjitter_thres.text()
        self.config['parameter_camera']['rouJitThrCur'] = self.edit_roundabout_jitter_thres_curve.text()
        self.config['parameter_camera']['rouJitThrStr'] = self.edit_roundabout_jitter_thres_straight.text()

        self.config['parameter_turning_loop']['turn_kp'] = self.edit_turn_p.text()
        self.config['parameter_turning_loop']['turn_kd'] = self.edit_turn_d.text()

        self.config['parameter_speed_loop']['speed_kp'] = self.edit_speed_p.text()
        self.config['parameter_speed_loop']['speed_ki'] = self.edit_speed_i.text()
        self.config['parameter_speed_loop']['speed_kd'] = self.edit_speed_d.text()

        self.config['parameter_control']['car_speed'] = self.edit_car_speed.text()

        with open("config.ini", "w") as f:
            self.config.write(f)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui_main = Ui_MainWindow_Son()
    ui_main.show()
    sys.exit(app.exec_())
