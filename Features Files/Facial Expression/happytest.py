from pygame import mixer
import time
import testpy
import os
# usr = input("how are you")

if testpy.counter.index(testpy.max_value) == "0":
    mixer.init()
    mixer.music.load('file_example_MP3_1MG.mp3')
    mixer.music.play()
