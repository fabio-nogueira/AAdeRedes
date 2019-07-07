import socket
host = 'localhost'     # Endereco IP do Servidor
port = 8880            # Porta que o Servidor esta
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (host, port)

s.connect(dest)
print("Cliente.py: Conectado ao servidor")

while True:
    try:
        jogadaDisponivel = int(s.recv(1024))
    except:
        print("Voce perdeu :(")
        break
    
    if(jogadaDisponivel == 1):
        print("Esta na sua rodada, Digite um palpite")
        msg= input()
        s.send(msg.encode())
        jogadaDisponivel = 0
        msgGanhou = int(s.recv(1024))
        if (msgGanhou == 1):
            print("Parabens! Voce Ganhou!!")
            break
s.close()
