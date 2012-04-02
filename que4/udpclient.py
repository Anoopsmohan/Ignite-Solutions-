import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("", 6000))
while 1:
	data, address = server_socket.recvfrom(256)
	print data
