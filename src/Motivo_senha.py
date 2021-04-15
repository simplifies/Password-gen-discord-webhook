import sys, time, os 

messagem = ("\n Para que queres a senha? ")

def typewriter():
    for char in messagem:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char !="\n":
            time.sleep(0.02)
        else:
            time.sleep(1)


typewriter()
Motivo = input("")
