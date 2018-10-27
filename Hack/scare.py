import pygame.mixer
import random
from time import sleep
pygame.mixer.init()




file = random.randrange(1,6)

if file == 1:
    pygame.mixer.music.load(open("ghost.mp3","rb"))
if file == 2:
    pygame.mixer.music.load(open("curse.mp3","rb"))
if file == 3:
    pygame.mixer.music.load(open("spook.mp3","rb"))
if file == 4:
    pygame.mixer.music.load(open("haunt.mp3","rb"))
if file == 5:
    pygame.mixer.music.load(open("lost.mp3","rb"))
print ("")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    sleep(1)
    #stp = input("Wanna Stop it?")
    #if stp == "s":
    #   break
print ("done")