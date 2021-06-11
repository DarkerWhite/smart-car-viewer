import cv2
import sys
import time
import socket
import numpy as np
from pathlib import Path
from remote_ui import Ui_RemoteCamera
from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class remoteCamera(QMainWindow, Ui_RemoteCamera):
    def __init__(self):
        super(remoteCamera, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        self.timer_update_camera = QtCore.QTimer()
        self.init_slot()

        # for main thread
        self.server_is_started = False
        self.client_is_started = False
        # for working thread
        self.server_is_working = False
        self.client_is_working = False
        self.server_data_is_ready = False

    def show_remote_camera_window(self):
        self.show()

    def init_slot(self):
        self.button_remote_listen_address.clicked.connect(self.toggle_server)
        self.button_remote_send_address.clicked.connect(self.toggle_client)

        self.timer_update_camera.timeout.connect(self.update_camera)

    def toggle_server(self):
        if not self.server_is_started:
            self.server_is_started = True
            self.server_is_working = True

            self.button_remote_listen_address.setText("Stop Listening")
            #self.button_remote_send_address.setEnabled(False)
            self.edit_remote_listen_address.setEnabled(False)

            self.timer_update_camera.start(100)
            t_server = Thread(target=self.udp_server)
            t_server.start()
        else:
            self.button_remote_listen_address.setText("Start Listening")
            self.button_remote_send_address.setEnabled(True)
            self.edit_remote_listen_address.setEnabled(True)

            self.timer_update_camera.stop()

            self.server_is_started = False
            self.server_is_working = False

    def toggle_client(self):
        if not self.client_is_started:
            self.client_is_started = True
            self.client_is_working = True

            self.button_remote_send_address.setText("Stop Sending")
            #self.button_remote_listen_address.setEnabled(False)
            self.edit_remote_send_address.setEnabled(False)

            t_client = Thread(target=self.udp_client)
            t_client.start()
        else:
            self.button_remote_send_address.setText("Start Sending")
            self.button_remote_listen_address.setEnabled(True)
            self.edit_remote_send_address.setEnabled(True)

            self.client_is_started = False
            self.client_is_working = False

    def update_camera(self):
        if self.server_data_is_ready:
            show = cv2.cvtColor(self.server_img_data, cv2.COLOR_BGR2RGB)
            showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
            self.label_get_remote.setPixmap(QtGui.QPixmap.fromImage(showImage))
            self.server_data_is_ready = False

    def udp_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.settimeout(1.0)
        address = self.edit_remote_listen_address.text().split(":")
        address[1] = int(address[1])
        address = address[0], address[1]

        try:
            server_socket.bind(address)
        except:
            return "Error: bind address failed."

        while self.server_is_working:
            try:
                server_data, address = server_socket.recvfrom(65000)
            except socket.timeout:
                continue
            #print(len(server_data))
            #print(type(server_data))
            server_data = np.frombuffer(server_data, dtype=np.uint8)
            self.server_img_data = cv2.imdecode(server_data, cv2.IMREAD_COLOR)
            self.server_data_is_ready = True
            #print(f"server got data, shape: {self.server_img_data.shape}")
        print("server stopped working")

    def udp_client(self):
        address = self.edit_remote_send_address.text().split(":")
        address[1] = int(address[1])
        address = address[0], address[1]

        # init camera
        try:
            cap = cv2.VideoCapture(1)
        except:
            return "Error: Failed to open camera."

        while self.client_is_working:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            client_socket.settimeout(3)
            _, frame = cap.read()
            frame = cv2.imencode(".jpg", frame)[1]
            client_socket.sendto(frame, address)
            #print(f"sending img, len: {len(frame)}")
            time.sleep(0.1)
        print("client stopped working")
