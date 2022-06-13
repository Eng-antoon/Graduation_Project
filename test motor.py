import sys
import Motor
from gtts import gTTS
import os
import pygame
import spacy
import time
import testpy
from Motor import GPIO


def start_project():
    import testpy


def start_game():
    myText = f"We are glad you are happy ,So we will start our main program. "
    language = "en"
    output = gTTS(text=myText, lang=language, slow=False)
    output.save("audio/file.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("audio/file.mp3")
    pygame.mixer.music.play()
    time.sleep(5)

    import SpinGame
while(True):

    start_project()

    max_value = max(testpy.counter)
    max_index = testpy.counter.index(max_value)

    if max_index == 0:

        start_game()

        time.sleep(3)
        from Motor import motor1_forward

        ######### start learn program