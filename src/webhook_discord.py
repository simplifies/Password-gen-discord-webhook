import requests
from gerador_senha import gera_senha
from Motivo_senha import Motivo
import os

url = "url-webhook"

data = {
    "username" : "Palavras-pass"
}

data["embeds"] = [
    {
        "description" : "Senha gerada: "+ gera_senha() + ' por motivo: '+ Motivo,
        "title" : "Nova senha!"
    }
]

result = requests.post(url, json = data)

if __name__ == '__main__':
    webhook()