import time
import json
import socket
import numpy as np

bufferSize = 2048
device = {
    'pc': ('0.0.0.0', 5000)
}
server_data_is_ready = False
server_is_working = True

def getTime():
    return time.strftime("%Y-%m-%d %x")

def printT(text):
    print(f"[{getTime()}]: {text}")

def sendMsg(device, msg, output_edit=None, output=True, wait_reply=False):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)

            if output:
                output_edit.append(f"{getTime()}: Try to make connection to {device.text()}")
            device = device.text().split(":")
            device = device[0], int(device[1])

            s.connect(device)
            try:
                s.sendall(msg.encode())
                if wait_reply:
                    msg = s.recv(1024)
                    if not msg:
                        return -1
                    return msg.decode()
            except:
                output_edit.append(f"{getTime()}: Timeout while waiting for reply.")
                return -1
    except:
        output_edit.append(f"{getTime()}: Failed to establish tcp connection.")
        return -1


#def server_side():
#    global server_data_is_ready
#    global server_data
#
#    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serversocket:
#        serversocket.bind(device['pc'])
#        serversocket.settimeout(3.0)
#        serversocket.listen(0)  # max listen num: only listen one connection to avoid data seperation
#
#        printT(f"Listening to {device['server']}.")
#        while server_is_working:
#            try:
#                try:
#                    clientsocket, addr = serversocket.accept()
#                except socket.timeout:
#                    continue
#                printT(f"Client addr: {addr}")
#
#                server_data = clientsocket.recv(1000).decode()
#                printT(f"Received data length: {len(server_data)}")
#                server_data_is_ready = True
#
#                clientsocket.close()
#                printT(f"Listening to {device['pc']}.")
#
#            except socket.timeout:
#                printT("Error: Connection timeout.")
#            except KeyboardInterrupt:
#                printT("Server terminated by user.")
#                break
