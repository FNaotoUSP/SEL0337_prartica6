
# le informacao na tag
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

# desabilita warnings
GPIO.setwarnings(False)

# objeto "leitor" para a instancia "SimpleMFRC522"
leitor = SimpleMFRC522()

print('Aproxime a tag')

# loop que cria as variaveis id e info, que rcebem a leitura da tag
while True:
	id,info = leitor.read()
	print('ID: {}\nInfo: {}'.format(id,info))
	sleep(3)
