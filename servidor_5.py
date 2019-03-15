import socket

def clientHandler(connection, client_address):
    print ('Connected by',client_address)
    while True :
        data = (connection.recv(1024)).decode()

        if data == "exit":
            reply = "Gracias por todo"
            connection.sendall(reply.encode())
            connection.close()
            print("Conexion con ", client_address," cerrada")
            break

        print ("Recibido", repr(data))
        reply = input("Respuesta: ")
        connection.sendall(reply.encode())

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host= socket.gethostname()
port=8086

s.bind(('127.0.0.1',port))

s.listen(10)

print("Server is running")
while True:
    connection, client_address=s.accept()
    clientHandler(connection, client_address)
s.close()
