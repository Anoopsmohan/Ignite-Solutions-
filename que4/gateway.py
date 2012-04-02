import socket
import thread
mutex = thread.allocate_lock()
data = ''
def main():
	tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	udp_socket.bind(("127.0.0.1",5000))
	tcp_socket.bind(("127.0.0.1",1234))
	tcp_socket.listen(20)
	
	print "TCPServer Waiting for client on port 1234"
	while 1:
		reader_socket,address = tcp_socket.accept()
		thread.start_new_thread(reader,(reader_socket,address))
		thread.start_new_thread(writer,(udp_socket,address))

def reader(reader_socket,address,*args):
	global data
	global mutex
	while 1:
		data = reader_socket.recv(4096)
		mutex.release_lock()
		print "got data :" + data

def writer(writer_socket,address,*args):
	global data
	global mutex
	while 1:
		mutex.acquire_lock()
		writer_socket.sendto(data,("127.0.0.1",6000))
main()
