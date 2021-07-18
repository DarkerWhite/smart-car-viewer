import time
import json
import struct
import socket
import numpy as np

bufferSize = 2048
device = {
    'pc': ('0.0.0.0', 5000)
}
server_data_is_ready = False
server_is_working = True

destination_to_index = {
    "CON": 0,
    "CAM": 1
}



def getTime():
    return time.strftime("%H:%M:%S")

def printT(text):
    print(f"[{getTime()}]: {text}")

def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = b""
    while len(data) < n:
        packet = sock.recv(n - len(data))
        print("packet", packet)
        if not packet:
            return None
        data += packet
        print(f"!!!!!!!!!!!{len(data)}!!!!!!!!!!!")
    return data


# reply msg must end with \n
def sendMsg(device, status, msg, output_edit=None, wait_reply=False):
    msg = msg.split("@")
    status = status[destination_to_index[msg[0]]]
    device = device[destination_to_index[msg[0]]]
    msg = msg[1]#[:-1] + "\r\n"

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)

            if output_edit:
                output_edit.append(f"{getTime()}: Send {msg[:-1]}")
            device = device.text().split(":")
            device = device[0], int(device[1])

            print("making connection")
            try:
                s.connect(device)
            except:
                if output_edit:
                    output_edit.append(f"{getTime()}: Failed to connect.")
                return -1
            #s.setblocking(False)

            try:
                print("sending message")
                s.sendall(msg.encode())
            except:
                print("failed when sending")
                if output_edit:
                    output_edit.append(f"{getTime()}: Timeout while sending.")
                return -1

            if wait_reply:
                print("waiting for reply")
                retry_time = 0
                #wait_time = 0
                recv_msg = ""
                while True:
                    msg_length = None
                    for i in range(20):
                        print("try to find start signal")
                        try:
                            recv = s.recv(1)
                            print("start", recv)
                            if recv == b"#":
                                msg_length = int(recvall(s, 4).decode())
                                print(f"got msg length {msg_length}")
                                break
                        except ConnectionAbortedError:
                            if output_edit:
                                output_edit.append(f"{getTime()}: Connection is aborted.")
                                return -1
                        #except socket.timeout:
                        #    if output_edit:
                        #        output_edit.append(f"{getTime()}: Timeout when receiving start signal.")
                        #        return -1
                    if not msg_length:
                        print(f"msg_length: {msg_length}")
                        if output_edit:
                            output_edit.append(f"{getTime()}: Failed to find start signal")
                        return -1

                    try:
                        recv_msg = recvall(s, msg_length).decode()
                        output_edit.append(f"{getTime()}: {recv_msg[:-1]}.")
                        return recv_msg
                    except socket.timeout:
                        if retry_time < 5:
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
