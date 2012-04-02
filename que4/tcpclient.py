import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 1234))
while 1:
        data = raw_input ( ">>" )
        client_socket.send(data)
client_socket.close()
