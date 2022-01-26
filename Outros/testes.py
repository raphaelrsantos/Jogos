
import threading
import time

Flag_saida = 0

class threadEspecial(threading.Thread):
   def __init__(self, threadID, nome, contador):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.nome = nome
      self.contador = contador
   def run(self):
      self


def print_hora(Nome_Thread, contador):
   while contador:
      if Flag_saida:
         Nome_Thread.exit()
      contador -= 1


# Create new threads
thread1 = threadEspecial(1, "Thread-1", 1)
thread2 = threadEspecial(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("Saindo da Thread principal")

