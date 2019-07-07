import socket
import sys
host = 'localhost'     # Endereco IP do Servidor
port = 8880           # Porta que o Servidor esta
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (host, port)

s.connect(dest)
print("Espectador: Conectado ao servidor")

ganhouUm= "Jogador 1 GANHOU!!!"
ganhouDois= "Jogador 2 GANHOU!!!"

while True:
	msgm = s.recv(1024).decode()

	if ((msgm==ganhouUm) or (msgm==ganhouDois)):
		print(msgm)
		break
		
	print(msgm)
s.close                
	

