# -*- coding: utf-8 -*-

import sys
import serial
import time
from ui import Ui_MainWindow
from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class Ui_MainWindow_Son(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):

        QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)

        self.timer_checkout = QtCore.QTimer()
        self.timer_update = QtCore.QTimer()
        self.timer_key = QtCore.QTimer()
        self.slot_init()

        self.flag_get_frame_mode = 0
        self.working = False
        self.serial_status = False
        self.data_is_ready = False

        self.key_command_dict = {
            81: "shoot once",    # q
            87: "5".encode(),    # w - forward
            69: "continus shoot",  # e
            65: "3".encode(),    # a - left
            83: "6".encode(),    # s - backward
            68: "4".encode(),    # r - right
            88: "2".encode(),    # space - stop
            16777216: "7".encode()  # esc
        }

        self.key_continus_shoot = False

        self.key_working = False
        self.status_continus_shoot = False

    def keyPressEvent(self, e):
        key = e.key()
        if not self.key_working:
            if key in self.key_command_dict:
                if key == 69:
                    if not self.key_continus_shoot:
                        self.key_continus_shoot = True
                        self.get_in_realtime()
                    return

                if key == 81:
                    self.get_one_frame()
                    return

                send_thread = Thread(target=self.send_command, args=(key,))
                send_thread.start()

    def keyReleaseEvent(self, e):
        if e.key() == 69:
            self.key_continus_shoot = False

    def send_command(self, key):
        print(f"send key {self.key_command_dict[key]}")
        for i in range(20):
            self.ser.write(self.key_command_dict[key])
            #self.ser.write('6'.encode())
        time.sleep(0.1)
        for i in range(20):
            self.ser.write("0".encode())
        self.key_working = False
        print(f"stop sending key {key}")

    def update_keyboard(self):
        pass

    def slot_init(self):
        self.button_get_one.clicked.connect(self.get_one_frame)
        self.button_get_in_realtime.clicked.connect(self.get_in_realtime)
        self.button_sync.clicked.connect(self.sync_parameter)
        self.button_serial.clicked.connect(self.toggle_serial)
        self.timer_checkout.timeout.connect(self.check_timeout)
        self.timer_update.timeout.connect(self.update_ui)

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
        else:
            self.ser.close()
            self.serial_status = False
            self.edit_camera.append("Serial is closed")
            self.button_serial.setText("Open Serial")
            self.edit_port.setEnabled(True)

    def get_one_frame(self):
        if (self.flag_get_frame_mode == 0):
            self.button_get_one.setEnabled(False)
            self.button_get_in_realtime.setEnabled(False)
            self.button_get_one.setText("Getting Frame...")
            self.flag_get_frame_mode = 1
            self.working = True
            self.get_frame_thread = Thread(target=self.get_frame)
            self.get_frame_thread.start()
            self.timer_checkout.start(5000)
            self.timer_update.start(500)

    def get_in_realtime(self):
        if (self.flag_get_frame_mode == 0):
            self.button_get_one.setEnabled(False)
            self.button_get_in_realtime.setText("Stop Getting Frames")
            self.flag_get_frame_mode = 2
            self.working = True
            self.get_frame_thread.start()
            self.timer_update.start(500)
        elif (self.flag_get_frame_mode == 2):
            self.working = False
            time.sleep(0.5)
            self.flag_get_frame_mode = 0
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
            string_row_body = (int(self.dataDict['laneLeft'][row])) * "&nbsp;" + "L"
            string_row_body += (int(self.dataDict['laneCenter'][row]) - int(self.dataDict['laneLeft'][row])) * "&nbsp;" + "|"
            string_row_body += (int(self.dataDict['laneRight'][row]) - int(self.dataDict['laneCenter'][row])) * "&nbsp;" + "R<br>"
            #print(string_row_body)
            string_list.append(string_row_head + string_row_body)
        self.string_total = "".join(string_list)
        #print(self.string_total)
        self.data_is_ready = True

    def get_frame(self):
        command = '1'.encode()

        print("sending get frame")
        for i in range(20):
            self.ser.write(command)

        while self.working is True:
            time.sleep(0.5)
            count = self.ser.inWaiting()

            if count > 0:
                recvData = self.ser.readline()
                if len(recvData) >= 900:
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
                        break
                else:
                    self.edit_camera.append(f"Got {len(recvData)} bytes, retrying...")
            else:
                self.edit_camera.append(f"Serial received {count} data, retrying...")

        time.sleep(0.01)
        print("sending end get frame")
        for i in range(20):
            self.ser.write("0".encode())
        #self.check_timeout()

    def update_ui(self):
        print("trying to update")
        if (self.data_is_ready):
            print("got update")
            self.edit_camera.setText(self.string_total)
            self.edit_error.setText(self.dataDict['status'][0])
            self.edit_slope.setText(self.dataDict['status'][1])
            self.edit_sharp_curve_row.setText(self.dataDict['status'][2])
            self.edit_miss_count.setText(self.dataDict['status'][3])
            self.edit_roundabout.setText(self.dataDict['status'][4])
            self.edit_three_way_fork.setText(self.dataDict['status'][5])

            self.data_is_ready = False
            if (self.flag_get_frame_mode):
                self.timer_update.stop()

    def sync_parameter(self):
        pass

    def check_timeout(self):
        self.working = False
        self.timer_checkout.stop()
        print("sending timeout")
        for i in range(20):
            self.ser.write("0".encode())
        self.button_get_one.setText("Get One Frame")
        self.button_get_one.setEnabled(True)
        self.button_get_in_realtime.setEnabled(True)
        self.flag_get_frame_mode = 0
        self.data_is_ready = False
        self.timer_update.stop()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow_Son()
    ui.show()
    sys.exit(app.exec_())
