import random
import string

def gera_senha() -> str:
  """
  Gera uma senha aleatória
  """
  chars = string.ascii_letters + string.digits
  tamanho = 13
  senha = ''.join([random.choice(chars) for i in range(tamanho)])
  return senha
  
if __name__ == "__main__":
  main()