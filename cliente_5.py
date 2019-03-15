import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port=8086
s.connect(('127.0.0.1',port))
while True :
	message = input("mensaje:")
	s.send(message.encode())

	print("Esperando respuesta")
	reply = s.recv(1024)
	print("Recibido",repr(reply))
	if message == "exit":
		s.close()
		break
