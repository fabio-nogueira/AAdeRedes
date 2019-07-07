import socket
import random
import sys

host = 'localhost'
port = 8880

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket criado")

try:
  s.bind((host,port))
except socket.error:
  print ("Binding falhou")
  sys.exit

print("Socket foi designado")

s.listen(3)

print("Socket esta pronto")


conn1, addr1 = s.accept()
print("Conectado com " + addr1[0] + ":" + str(addr1[1]))
print("Esperando o jogador 2")
conn2, addr2 = s.accept()
print("Conectado com " + addr2[0] + ":" + str(addr2[1]))
print("Aguardando Espectador")
conn3, addr3 = s.accept()
print("Conectado com " + addr3[0] + ":" + str(addr3[1]))
numero = random.randint(1,10)
print("Numero sorteado: ", numero)
terminou=0

msgmEspect=("Todos os jogadores ja estao conectados ao servidor, o jogo comecou!").encode()
conn3.send(msgmEspect)


while True:
	print("----Rodada do Jogador 1----")
	jogadaUm = '1'
	conn1.send(jogadaUm.encode())
	palpite = int(conn1.recv(1024))
	print("Palpite do Jogador 1: ", palpite)

	msgmEspect = ("Palpite do Jogador 1: " + str(palpite)).encode()
	conn3.send(msgmEspect)
	

	
	if(palpite==numero):
		msgGanhou='1'
		conn1.send(msgGanhou.encode())
		print("Jogador 1 GANHOU!!!!")
		msgmEspect = ("Jogador 1 GANHOU!!!")
		conn3.send(msgmEspect.encode())
		
          
		break
    
	msgGanhou='0'          
	conn1.send(msgGanhou.encode())
	jogadaUm = '0'
	conn1.send(jogadaUm.encode())


	print("----Rodada do Jogador 2----")
	jogadaDois = '1'
	conn2.send(jogadaDois.encode())
	palpite = int(conn2.recv(1024))
	


	print("Palpite do Jogador 2: ", palpite)


	msgmEspect = ("Palpite do Jogador 2: " + str(palpite)).encode()
	conn3.send(msgmEspect)

	if(palpite==numero):
		msgGanhou='1'
		conn2.send(msgGanhou.encode())
		print("Jogador 2 GANHOU!!!!")
		
		msgmEspect = ("Jogador 2 GANHOU!!!")
		conn3.send(msgmEspect.encode())

		break
	conn2.send(msgGanhou.encode())
	jogadaDois='0'
	conn2.send(jogadaDois.encode())


s.close()
