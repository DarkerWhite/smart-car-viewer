import socket

device = {
    'pc': ('0.0.0.0', 5100)
}

def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serversocket:
        serversocket.bind(device['pc'])
        serversocket.settimeout(3.0)
        serversocket.listen(0)  # max listen num: only listen one connection to avoid data seperation

        print(f"Listening to {device['pc']}.")
        while True:
            try:
                try:
                    clientsocket, addr = serversocket.accept()
                except socket.timeout:
                    continue
                print(f"Client addr: {addr}")

                server_data = clientsocket.recv(1000).decode()
                if server_data == "init":
                    clientsocket.sendall("init".encode())
                print(f"Received data length: {len(server_data)}")
                print(f"Recvived: {server_data}")

                clientsocket.close()
                print(f"Listening to {device['pc']}.")

            except socket.timeout:
                print("Error: Connection timeout.")
            except KeyboardInterrupt:
                print("Server terminated by user.")
                break

server()
