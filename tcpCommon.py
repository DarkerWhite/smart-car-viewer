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
    return time.strftime("%H:%M:%S")

def printT(text):
    print(f"[{getTime()}]: {text}")

# reply msg must end with \n
def sendMsg(device, msg, output_edit=None, wait_reply=False):
    time.sleep(0.1)
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)

            if output_edit:
                output_edit.append(f"{getTime()}: Try to send {msg}")
            device = device.text().split(":")
            device = device[0], int(device[1])

            print("making connection")
            s.connect(device)
            s.setblocking(False)

            try:
                print("sending message")
                s.sendall(msg.encode())
            except:
                print("failed when sending")
                if output_edit:
                    output_edit.append(f"{getTime()}: Timeout while sending.")
                return -1

            if wait_reply:
                retry_time = 0
                wait_time = 0
                recv_msg = b""
                while True:
                    try:
                        if recv_msg and recv_msg[-1] == '\n':
                            return recv_msg
                        recv_buffer = s.recv(100)
                        if recv_buffer:
                            recv_msg += recv_buffer.decode()
                    except BlockingIOError:
                        if wait_time < 200:
                            wait_time += 1
                            time.sleep(0.01)
                            print("blocking")
                        else:
                            if retry_time < 10:
                                retry_time += 1
                                print("retrying sending message")
                                wait_time = 0
                                time.sleep(0.01)
                                s.sendall(msg.encode())
                                recv_msg = ""
                            else:
                                print("failed when waiting for reply")
                                if output_edit:
                                    output_edit.append(f"{getTime()}: Timeout while waiting for reply.")
                                return -1
                    except socket.timeout:
                        if retry_time < 3:
                            retry_time += 1
                            print("retrying sending message")
                            s.sendall(msg.encode())
                            recv_msg = ""
                        else:
                            print("failed when waiting for reply")
                            if output_edit:
                                output_edit.append(f"{getTime()}: Timeout while waiting for reply.")
                            return -1
                    except:
                        raise
            # return without waiting for reply
            else:
                return 0
    except socket.timeout:
        output_edit.append(f"{getTime()}: Failed to establish tcp connection.")
        print("connection failed")
        return -1
    except:
        raise
    output_edit.append(f"{getTime()}: Unknown error.")
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
