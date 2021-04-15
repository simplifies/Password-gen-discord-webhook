import Motivo_senha
import sys, time, os 
from gerador_senha import gera_senha
from Motivo_senha import Motivo

message = '\n Senha gerada: " ' + gera_senha() + ' " por motivo: ' + Motivo + '\n'

def typewriter():
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char !="\n":
            time.sleep(0.02)
        else:
            time.sleep(1)



typewriter()

time.sleep(5)
input("\n \n \n Pressiona qualquer tecla para sair.")
