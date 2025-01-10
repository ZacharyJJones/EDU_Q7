print("day 26 - more libraries")

## This one starts with a template
import os
import time

import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
sound.play()

def pause():
  pygame.mixer.pause()

pause()

def play():
  # Play the sound until user stops it.
  pygame.mixer.unpause()
  print("You can exit at any time by pressing the enter key.")
  input()
  pause()

while True:
  # clear the screen 
  os.system("clear")

  # Show the menu
  print("Options:")
  print("--------")
  print("[1] Play Song")
  print()
  print("[0] Exit Program")
  print()
  print()

  # take user's input
  num = input("Enter a number according to the above menu: ")

  # check whether you should call the play() subroutine depending on user's input
  if num == "1":
    play()
  elif num == "0":
    break