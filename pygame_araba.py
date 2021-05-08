import pygame
from pygame.locals import *
import sys
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#Motor kontrol
Motor1A = 23
Motor1B = 24
Motor2A = 27
Motor2B = 22
         
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)

class CarControlTest:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((400, 400))
        self.send_inst = True
        self.steer()
    def steer(self):
        complex_cmd = False
        while self.send_inst:
            for event in pygame.event.get():
                if (event.type == KEYDOWN) or (complex_cmd):
                    key_input = pygame.key.get_pressed()
                    complex_cmd = False
                    if key_input[pygame.K_LEFT]:
                        print("sol")
                        GPIO.output(Motor1A,GPIO.HIGH)
                        GPIO.output(Motor1B,GPIO.HIGH)
                        GPIO.output(Motor2A,GPIO.HIGH)
                        GPIO.output(Motor2B,GPIO.LOW)
                    elif key_input[pygame.K_RIGHT]:
                        print("sag")
                        GPIO.output(Motor1A,GPIO.HIGH)
                        GPIO.output(Motor1B,GPIO.HIGH)
                        GPIO.output(Motor2A,GPIO.LOW)
                        GPIO.output(Motor2B,GPIO.HIGH)
                    elif key_input[pygame.K_UP]:
                        print("ileri")
                        GPIO.output(Motor1A,GPIO.HIGH)
                        GPIO.output(Motor1B,GPIO.LOW)
                        GPIO.output(Motor2A,GPIO.HIGH)
                        GPIO.output(Motor2B,GPIO.HIGH)
                    elif key_input[pygame.K_DOWN]:
                        print("geri")
                        GPIO.output(Motor1A,GPIO.LOW)
                        GPIO.output(Motor1B,GPIO.HIGH)
                        GPIO.output(Motor2A,GPIO.HIGH)
                        GPIO.output(Motor2B,GPIO.HIGH)
                    elif key_input[pygame.K_x] or key_input[pygame.K_q]:
                        self.close_serial_connection()
                        break
    def close_serial_connection(self):
        print('Çikis yapıldı.')
        pygame.quit()
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.HIGH)
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.HIGH)
        self.send_inst = False


if __name__ == "__main__":
    CarControlTest()

