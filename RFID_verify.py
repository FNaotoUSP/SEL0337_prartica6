
# Verifica a tag e permite ou nao acesso
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

LED_red = 3
LED_green = 5

# objeto "leitor" para a instancia "SimpleMFRC522"
leitor = SimpleMFRC522()

def led_on (led):
	GPIO.setup(led, GPIO.OUT)
	GPIO.output(led, GPIO.HIGH)

def led_off (led):
	GPIO.setup(led, GPIO.OUT)
	GPIO.output(led, GPIO.LOW)

def red_on ():
	led_off(LED_green)
	led_on(LED_red)

def green_on ():
	led_off(LED_red)
	led_on(LED_green)

def off ():
	led_off(LED_red)
	led_off(LED_green)

# loop que cria as variaveis id e info, que rcebem a leitura da tag
while True:
	print('\n\n Aproxime a tag')
	id,info = leitor.read()
	print('ID: {}\nInfo: {}'.format(id,info))
	if id == 426883519919:
		print('Acesso liberado')
		green_on()
	else:
		print('Acesso negado')
		red_on()
	sleep(5)
	off()
