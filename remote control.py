import time
import serial
import pygame
import threading
import subprocess
from sys import exit
from clear_screen import clear

#from datetime import datetime

port = 'COM6'
exeLoc = "./build/laneDetect.exe"

throttle_break = 0
left_right = 0
command = None
"""
command     note
-----------------------
1           take pic
2           stop car
3           spin left
4           spin right
5           move forward
6           move backward
"""

working = True

x_is_down = False
o_is_down = False
up_is_down = False
down_is_down = False
left_is_down = False
right_is_down = False

pygame.init()
clock = pygame.time.Clock()
pygame.joystick.init()
sensitivity = 120
analyzeTimes = 1

j = pygame.joystick.Joystick(0)
j.init()

def joystick_thread():
    global command
    global left_right
    global throttle_break
    global analyzeTimes

    global x_is_down
    global o_is_down
    global up_is_down
    global down_is_down
    global left_is_down
    global right_is_down


    while working:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                print("event.button",event.button)
                if event.button == 0:   # x down
                    if not x_is_down:
                        x_is_down = True
                        command = '1'.encode()      # take pic

                if event.button == 1:   # o down
                    o_is_down = True
                    command = '2'.encode()

                if event.button == 3:   # break remote
                    # o_is_down = True
                    command = '7'.encode()
                
                if event.button == 2:   # take photo to PC
                    # o_is_down = True
                    command = '8'.encode()

                if event.button == 11:  # up 
                    if not up_is_down:
                        up_is_down = True
                        analyzeTimes += 1
                        print(f"analyzeTimes: {analyzeTimes}")

                if event.button == 12:  # down 
                    if not down_is_down:
                        down_is_down = True
                        analyzeTimes -= 1
                        if (analyzeTimes < 0):
                            analyzeTimes = 0
                        print(f"analyzeTimes: {analyzeTimes}")

                if event.button == 13:  # left 
                    if not left_is_down:
                        left_is_down = True
                        analyzeTimes -= 5
                        if (analyzeTimes < 0):
                            analyzeTimes = 0
                        print(f"analyzeTimes: {analyzeTimes}")

                if event.button == 14:  # right 
                    if not right_is_down:
                        right_is_down = True
                        analyzeTimes += 5
                        print(f"analyzeTimes: {analyzeTimes}")


            elif event.type == pygame.JOYBUTTONUP:
                if event.button == 0:   # x up
                    x_is_down = False

                if event.button == 1:   # o up
                    o_is_down = False

                if event.button == 11:  # up
                    up_is_down = False

                if event.button == 12:  # down
                    down_is_down = False

                if event.button == 13:  # left
                    left_is_down = False

                if event.button == 14:  # right
                    right_is_down = False

            elif event.type == pygame.JOYAXISMOTION:
                # print("event.axis",event.axis)
                if (event.axis == 0):   # x axis of left stick
                    if (event.value < -0.4):
                        left_right = '3'.encode()

                    elif (event.value > 0.4):
                        left_right = '4'.encode()

                    else:
                        left_right = None
                # elif(event.axis == 3):  # right triger
                #     if (event.value > 0):
                #         throttle_break = '3'.encode()

                elif(event.axis == 5):  # right triger
                    if (event.value > 0):
                        throttle_break = '5'.encode()

                elif(event.axis == 4):  # left triger
                    if (event.value > 0):
                        if (throttle_break != b'5'):
                            throttle_break = '6'.encode()
                        else:
                            throttle_break = None

        clock.tick(sensitivity)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def displayImage(dataDict):
    # for item in dataDict:
    #     map(lambda x: int.from_bytes(x, byteorder='big'))
    for iterRow in range(50):
        if (int(dataDict["detectLeft"][iterRow]) and int(dataDict["detectRight"][iterRow])):
            print(f"AL {format(iterRow, '2d')}", end="")
        elif (int(dataDict["detectLeft"][iterRow]) and not int(dataDict["detectRight"][iterRow])):
            print(f"NR {format(iterRow, '2d')}", end="")
        elif (not int(dataDict["detectLeft"][iterRow]) and int(dataDict["detectRight"][iterRow])):
            print(f"NL {format(iterRow, '2d')}", end="")
        elif (not int(dataDict["detectLeft"][iterRow]) and not int(dataDict["detectRight"][iterRow])):
            print(f"NA {format(iterRow, '2d')}", end="")

        for iterCol in range(188):
            if iterCol == int(dataDict["laneLeft"][iterRow]):
                print("L", end="")
            elif iterCol == int(dataDict["laneRight"][iterRow]):
                print("R", end="")
            elif iterCol == int(dataDict["laneCenter"][iterRow]):
                print("|", end="")
            else: 
                print(" ", end="")
        print("")


def serial_thread():
    global command
    global throttle_break
    global left_right

    ser = serial.Serial(port, 115200)

    def int2fixedStr(value):
        return str(int(value)).rjust(3, '0')

    def sendCommand(command):
        print("sendCommand",command)
        for i in range(20):
            ser.write(command)
        if command == '1'.encode():
            #a=datetime.now()
            print("take pic")
            t = 0
            time.sleep(0.2)
            command = '0'.encode()  
            while working:
                time.sleep(0.5)
                count = ser.inWaiting()
                print("count",count)

                if count > 0:
                    recvData = ser.readline()
                    # print("recvData")
                    # print(recvData)
                    #if (len(recv) != 9401):
                    #print("COM received invalid data.")
                    #return
                    print("len",len(recvData))
                    if len(recvData) >= 900:
                        clear()
                        recv = recvData.decode()
                        print(recv)
                        recv = recv[:-1].split(",")
                        print(recv)
                        dataDict = {
                                    "laneLeft": recv[0][:-1].split(" "),
                                    "laneRight": recv[1][:-1].split(" "),
                                    "laneCenter": recv[2][:-1].split(" "),
                                    "detectLeft": recv[3][:-1].split(" "),
                                    "detectRight": recv[4][:-1].split(" ")
                                }
                        print(f"analyzeTimes: {analyzeTimes}")
                        displayImage(dataDict)
                        break
                    else:
                        t = t + 1
                        if t > 30:
                            clear()
                            print("restart")
                            break
                else:
                    #command = '1'.encode()
                    t = t + 1
                    print("error")
                    for i in range(20):
                        ser.write(command)
                    if t > 30:
                        clear()
                        print("restart")
                        break
        else:
            time.sleep(0.2)
            command = '0'.encode()

        if command == '0'.encode():
            print("stop")
            for i in range(20):
                ser.write('0'.encode())  

    while working:
        if throttle_break:
            sendCommand(throttle_break)
            throttle_break = None

        if left_right:
            sendCommand(left_right)
            left_right = None

        if command:
            sendCommand(command)
            if (command == b'2'):
                if (o_is_down):
                    continue
            command = None


t_joy = threading.Thread(target = joystick_thread)
t_ser = threading.Thread(target = serial_thread)

# t_joy.daemon = True
# t_ser.daemon = True

t_joy.start()
t_ser.start()

try:
    while True:
        time.sleep(1)
except:
    working = False
    print("Program exit.")
    
