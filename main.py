# -*- coding: utf-8 -*-

import sys
import time
import serial
from functools import partial
from ui import Ui_MainWindow
from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class Ui_MainWindow_Son(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        #self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.setFixedSize(self.width(), self.height())

        self.timer_checkout = QtCore.QTimer()
        self.timer_update = QtCore.QTimer()
        self.timer_key_command = QtCore.QTimer()
        self.timer_check_serial_available = QtCore.QTimer()
        self.slot_init()

        self.flag_get_frame_mode = 0
        self.working = False
        self.serial_status = False
        self.data_is_ready = 0
        self.need_clean = False

        self.key_command_dict = {
            81: self.get_one_frame,     # q - take a shot
            87: "5".encode(),           # w - forward
            65: "3".encode(),           # a - left
            83: "6".encode(),           # s - backward
            68: "4".encode(),           # r - right
            75: "2".encode(),           # k - stop
            16777216: "7".encode(),     # esc - exit control mode
            80: "8".encode(),           # p - pic to pc
            70: "9".encode(),           # f - clear flag
            self.button_thres_up: "a".encode(),
            self.button_thres_down: "b".encode(),
            self.button_distance_up: "c".encode(),
            self.button_distance_down: "d".encode(),
            self.button_turn_p_up: "e".encode(),           # add p of turning loop
            self.button_turn_p_down: "f".encode(),           # dec p of turning loop
            self.button_turn_d_up: "g".encode(),           # add d of turning loop
            self.button_turn_d_down: "h".encode(),           # dec d of turning loop
            self.button_sharp_curve_thres_up: "i".encode(),
            self.button_sharp_curve_thres_down: "j".encode(),
            self.button_roundabout_thres_curve_up: "k".encode(),
            self.button_roundabout_thres_curve_down: "l".encode(),
            self.button_roundabout_thres_straight_up: "m".encode(),
            self.button_roundabout_thres_straight_down: "n".encode()
        }

        # bytes type: need to be send
        # function type: [need to be send, key is pressed]
        self.key_status_dict = {
            81: [False, False],
            87: False,
            65: False,
            83: False,
            68: False,
            75: False,
            16777216: False,
            80: False,
            70: False,
            self.button_thres_up: False,
            self.button_thres_down: False,
            self.button_distance_up: False,
            self.button_distance_down: False,
            self.button_turn_p_up: False,
            self.button_turn_p_down: False,
            self.button_turn_d_up: False,
            self.button_turn_d_down: False,
            self.button_sharp_curve_thres_up: False,
            self.button_sharp_curve_thres_down: False,
            self.button_roundabout_thres_curve_up: False,
            self.button_roundabout_thres_curve_down: False,
            self.button_roundabout_thres_straight_up: False,
            self.button_roundabout_thres_straight_down: False,
        }

        self.button_to_edit = {
            self.button_thres_up: self.edit_thres,
            self.button_thres_down: self.edit_thres,
            self.button_distance_up: self.edit_distance,
            self.button_distance_down: self.edit_distance,
            self.button_turn_p_up: self.edit_turn_p,
            self.button_turn_p_down: self.edit_turn_p,
            self.button_turn_d_up: self.edit_turn_d,
            self.button_turn_d_down: self.edit_turn_d,
            self.button_sharp_curve_thres_up: self.edit_sharp_curve_thres,
            self.button_sharp_curve_thres_down: self.edit_sharp_curve_thres,
            self.button_roundabout_thres_curve_up: self.edit_roundabout_thres_curve,
            self.button_roundabout_thres_curve_down: self.edit_roundabout_thres_curve,
            self.button_roundabout_thres_straight_up: self.edit_roundabout_thres_straight,
            self.button_roundabout_thres_straight_down: self.edit_roundabout_thres_straight,
        }

    def keyPressEvent(self, e):
        #print(e.key())
        if self.serial_status:
            if e.key() in self.key_command_dict:
                if isinstance(self.key_command_dict[e.key()], bytes):
                    self.key_status_dict[e.key()] = True
                else:
                    self.key_status_dict[e.key()][1] = True
                    self.key_status_dict[e.key()][0] = True

    def keyReleaseEvent(self, e):
        if e.key() in self.key_command_dict:
            if isinstance(self.key_command_dict[e.key()], bytes):
                self.key_status_dict[e.key()] = False
            else:
                self.key_status_dict[e.key()][1] = False

    def send_command(self, command):
        self.ser.flushInput()
        for i in range(20):
            self.ser.write(command)
        time.sleep(0.1)
        for i in range(20):
            self.ser.write("0".encode())
        time.sleep(0.1)

    def send_command_and_echo_back(self, key):
        command = self.key_command_dict[key]
        self.ser.flushInput()
        for i in range(20):
            self.ser.write(command)
        time.sleep(0.1)
        for i in range(20):
            self.ser.write("0".encode())
        time.sleep(0.1)

        for trial_time in range(3):
            count = self.ser.inWaiting()
            if count > 0:
                recvData = self.ser.readline()
                print(len(recvData))
                print(recvData)
                if (len(recvData) == 6):
                    recv = recvData.decode()[:-1]

                    int_list = [self.button_thres_up, self.button_thres_down, self.button_sharp_curve_thres_up, self.button_sharp_curve_thres_down, self.button_roundabout_thres_curve_up, self.button_roundabout_thres_curve_down, self.button_roundabout_thres_straight_up, self.button_roundabout_thres_straight_down]
                    if key in int_list:
                        recv = int(recv)
                    else:
                        recv = int(recv) / 10

                    self.button_to_edit[key].setText(str(recv))
                    self.button_to_edit[key].setStyleSheet("QLineEdit{background : white;}")
                    self.working = False
                    return
        self.working = False
        self.button_to_edit[key].setStyleSheet("QLineEdit{background : red;}")
        return

    # in timer update
    def send_key_command(self):
        if not self.serial_status:
            return
        if self.working:
            return

        for i in self.key_status_dict:
            if isinstance(i, QtWidgets.QPushButton):
                # parameter button
                if self.key_status_dict[i] is True:
                    print(self.key_command_dict[i])
                    self.working = True
                    self.send_command_and_echo_back(i)
                    self.key_status_dict[i] = False
            elif isinstance(self.key_command_dict[i], bytes):
                # keyboard
                if self.key_status_dict[i] is True:
                    self.send_command(self.key_command_dict[i])
                    self.key_status_dict[i] = False
            elif self.key_status_dict[i][0] is True:     # method type
                # pic button
                if self.key_status_dict[i][1] is False and self.working is False:
                    self.working = True
                    self.key_command_dict[i]()

    def slot_init(self):
        self.button_get_one.clicked.connect(self.get_one_frame)
        self.button_serial.clicked.connect(self.toggle_serial)

        self.timer_update.timeout.connect(self.update_ui)
        self.timer_key_command.timeout.connect(self.send_key_command)

        self.timer_key_command.start(50)
        self.timer_check_serial_available.start(200)
        self.timer_update.start(500)

        # parameter button
        self.button_thres_up.clicked.connect(partial(self.handle_paramerter_key, self.button_thres_up))
        self.button_thres_down.clicked.connect(partial(self.handle_paramerter_key, self.button_thres_down))
        self.button_distance_up.clicked.connect(partial(self.handle_paramerter_key, self.button_distance_up))
        self.button_distance_down.clicked.connect(partial(self.handle_paramerter_key, self.button_distance_down))
        self.button_turn_p_up.clicked.connect(partial(self.handle_paramerter_key, self.button_turn_p_up))
        self.button_turn_p_down.clicked.connect(partial(self.handle_paramerter_key, self.button_turn_p_down))
        self.button_turn_d_up.clicked.connect(partial(self.handle_paramerter_key, self.button_turn_d_up))
        self.button_turn_d_down.clicked.connect(partial(self.handle_paramerter_key, self.button_turn_d_down))
        self.button_sharp_curve_thres_up.clicked.connect(partial(self.handle_paramerter_key, self.button_sharp_curve_thres_up))
        self.button_sharp_curve_thres_down.clicked.connect(partial(self.handle_paramerter_key, self.button_sharp_curve_thres_down))
        self.button_roundabout_thres_curve_up.clicked.connect(partial(self.handle_paramerter_key, self.button_roundabout_thres_curve_up))
        self.button_roundabout_thres_curve_down.clicked.connect(partial(self.handle_paramerter_key, self.button_roundabout_thres_curve_down))
        self.button_roundabout_thres_straight_up.clicked.connect(partial(self.handle_paramerter_key, self.button_roundabout_thres_straight_up))
        self.button_roundabout_thres_straight_down.clicked.connect(partial(self.handle_paramerter_key, self.button_roundabout_thres_straight_down))

    def handle_paramerter_key(self, btn):
        if self.serial_status:
            self.key_status_dict[btn] = True

    def toggle_serial(self):
        # init serial
        if (not self.serial_status):
            self.edit_camera.setText(f"Trying to open port {self.edit_port.text()}")
            try:
                self.ser = serial.Serial(self.edit_port.text(), 115200)
            except:
                self.edit_camera.append("Open serial failed")
                return
            self.edit_camera.append(f"Port {self.edit_port.text()} is open")
            self.edit_port.setEnabled(False)
            self.serial_status = True
            self.button_serial.setText("Close Serial")
            self.button_get_one.setEnabled(True)
        else:
            self.ser.close()
            self.serial_status = False
            self.edit_camera.append("Serial is closed")
            self.button_serial.setText("Open Serial")
            self.edit_port.setEnabled(True)
            self.button_get_one.setEnabled(False)

    def get_one_frame(self):
        print("in function get one frame")
        if (self.flag_get_frame_mode == 0):
            self.button_get_one.setEnabled(False)
            #self.button_get_in_realtime.setEnabled(False)
            self.button_get_one.setText("Getting Frame...")

            self.flag_get_frame_mode = 1
            self.working = True

            self.get_frame_thread = Thread(target=self.get_frame)
            self.get_frame_thread.start()

    def get_in_realtime(self):
        if (self.flag_get_frame_mode == 0):
            self.button_get_one.setEnabled(False)
            self.button_get_in_realtime.setText("Stop Getting Frames")

            self.flag_get_frame_mode = 2
            self.working = True

            self.get_frame_thread = Thread(target=self.get_frame)
            self.get_frame_thread.start()

            self.timer_update.start(500)
        elif (self.flag_get_frame_mode == 2):
            self.working = False
            self.flag_get_frame_mode = 0
            time.sleep(0.5)

            self.button_get_one.setEnabled(True)
            self.button_get_in_realtime.setText("Get In Realtime")

    def get_dataset(self):
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


            #print(string_row_body)
            string_list.append(string_row_head + string_row_body)
        self.string_total = "".join(string_list)
        #print(self.string_total)
        self.data_is_ready = 1

    def get_frame(self):
        self.ser.flushInput()
        for i in range(20):
            self.ser.write('1'.encode())
        time.sleep(0.1)
        if (self.flag_get_frame_mode != 2):
            #for i in range(20):
            for i in range(20):
                self.ser.write('0'.encode())
            time.sleep(0.2)

        failed_times = 0
        while self.working:
            count = self.ser.inWaiting()

            if count > 0:
                print("data in buffer: ", count)
                recvData = self.ser.readline()
                if len(recvData) >= 900:
                    failed_times = 0
                    recv = recvData.decode()
                    recv = recv[:-1].split(",")
                    self.dataDict = {
                        "laneLeft": recv[0][:-1].split(" "),
                        "laneRight": recv[1][:-1].split(" "),
                        "laneCenter": recv[2][:-1].split(" "),
                        "detectLeft": recv[3][:-1].split(" "),
                        "detectRight": recv[4][:-1].split(" "),
                        "status": recv[5][:-1].split(" ")
                    }
                    print(self.dataDict)

                    self.get_dataset()
                    current_time = time.strftime("%H:%M:%S", time.localtime())
                    self.label_time.setText(current_time)
                    if (self.flag_get_frame_mode == 1):
                        print("exiting one shot")
                        self.key_status_dict[81][0] = False
                        self.flag_get_frame_mode = 0
                        self.working = False
                        self.need_clean = True
                        return
                else:
                    print(f"Got {len(recvData)} bytes, retrying...")
                    failed_times += 1
            else:
                print(f"Serial received {count} data, retrying...")
                failed_times += 1

            time.sleep(0.5)
            if failed_times > 3:
                print("max trial time reached, stopped getting frame")
                self.data_is_ready = -1
                self.key_status_dict[81][0] = False
                self.flag_get_frame_mode = 0
                self.working = False
                return

        # self.working is False
        for i in range(20):
            self.ser.write('0'.encode())
        time.sleep(0.1)
        self.key_status_dict[69][0] = False
        self.flag_get_frame_mode = 0

    def update_ui(self):
        # send failed, need cleaning 
        if (self.data_is_ready == -1):
            self.button_get_one.setText("Get One Frame")
            self.button_get_one.setEnabled(True)
            #self.button_get_in_realtime.setEnabled(True)
            self.data_is_ready = 0
            self.edit_camera.append("Get pic failed")

        # send successfully, need cleaning
        if (self.need_clean):
            self.button_get_one.setText("Get One Frame")
            self.button_get_one.setEnabled(True)
            #self.button_get_in_realtime.setEnabled(True)
            self.need_clean = False

        # the data is ready
        if (self.data_is_ready == 1):
            self.edit_camera.setText(self.string_total)
            self.edit_error.setText(str(int(self.dataDict['status'][0])))
            self.edit_slope.setText(str(int(self.dataDict['status'][1])))
            self.edit_sharp_curve_row.setText(str(int(self.dataDict['status'][2])))
            self.edit_miss_count.setText(str(int(self.dataDict['status'][3])))
            self.edit_roundabout.setText(str(int(self.dataDict['status'][4])))
            self.edit_three_way_fork.setText(str(int(self.dataDict['status'][5])))
            self.edit_jitter_left.setText(str(float(self.dataDict['status'][6]) / 100))
            self.edit_jitter_right.setText(str(float(self.dataDict['status'][7]) / 100))

            self.data_is_ready = 0

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow_Son()
    ui.show()
    sys.exit(app.exec_())
