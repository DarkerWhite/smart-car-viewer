import cv2
import socket

server_working = False
client_working = False

server_data_is_ready = False

server_data = None
client_data = None

def udp_server(address):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.settimout(1.0)
    try:
        server_socket.bind(address)
    except:
        return "Error: bind address failed."

    while server_working:
        try:
            server_data, address = server_socket.recvfrom(2048)            
        except socket.timeout:
            continue
        server_img_data = cv2.imdecode(server_data, cv2.IMREAD_COLOR)
        server_data_is_ready = True

def udp_client(address):
    # init camera
    try:
        cap = cv2.VideoCapture(0)
    except:
        return "Error: Failed to open camera."
    
    while client_working:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.settimeout(1)
        _, frame = cap.read()
        frame = cv2.imencode(".jpg", frame)[1]
        client_socket.sendto(frame, address)
