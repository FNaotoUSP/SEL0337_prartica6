# grava informacao na tag
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

# desabilita warnings
GPIO.setwarnings(False)

# objeto "leitor" para a instancia "SimpleMFRC522"
leitor = SimpleMFRC522()

#variavel que contem a informacao a ser gravada
info = "SEL0337_1576"

# grava a info na tag quando aproximada
print('Aproxime a tag')
leitor.write(info)
print('Concuido')
