import time
import socket
from datetime import datetime

def getTime():
    return time.strftime("%H:%M:%S")

def sendMsg(device, msg, output_edit=None, output=True, wait_reply=False):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)

            if output:
                output_edit.append(f"{getTime()}: Try to send {msg}")
            device = device.split(":")
            device = device[0], int(device[1])

            #print("making connection")
            s.connect(device)
            #s.setblocking(False)

            try:
                #print("sending message")
                s.sendall(msg.encode())
            except:
                print("failed when sending")
                #output_edit.append(f"{getTime()}: Timeout while sending.")
                return -1

            if wait_reply:
                msg = ""
                #print("waiting")
                while True:
                    try:
                        msg_recv = s.recv(100)
                    except BlockingIOError:
                        if msg:
                            if msg[-1] == '\n':
                                return msg
                        continue
                    except:
                        print("failed when waiting for reply")
                        #output_edit.append(f"{getTime()}: Timeout while waiting for reply.")
                        return -1
                    msg += msg_recv.decode()
                else:
                    return -1
            else:
                return 0
    except:
        #output_edit.append(f"{getTime()}: Failed to establish tcp connection.")
        print("connection failed")
        raise
        return -1
    print("exiting")
    return -1


for i in range(100):
    sendMsg("192.168.137.190:502", f"testtesttest{i}\n", output=False, wait_reply=False)
    print(i)
    time.sleep(0.01)
    #now = datetime.now()
    #current_time = now.strftime("%H:%M:%S")
    #print(f"[{current_time}]: {reply[:-1]}")
#    if (reply != "init\n"):
#        print("not ok")
#
    #print(f"received: {reply}")
    # if reply == "init":
    #     print("ok")
    # else:
    #     print("not ok")
    #print(reply)
    #print()
    #time.sleep(1)
