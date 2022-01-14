import time

from testpy import *
from gtts import gTTS
import os
import pygame

max_value = max(counter)
max_index = counter.index(max_value)

if max_index == 0:
    myText = "بما انك مستمتع فهيا بنا نلعب لعبة التخمين فهذة اللعبة تعتمد علي ..."
    language = "ar"
    output = gTTS(text=myText, lang=language, slow=False)
    output.save("file.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("file.mp3")
    pygame.mixer.music.play()
    time.sleep(5)
    from SpinBall import SpinGame

    time.sleep(10)


# elif max_value == 1:
#
# elif max_value== 2:
#
# elif max_value == 3:
#
# elif max_value == 4:
#
# elif max_value == 5:
else:
    print("try another thing")
    # max_index = counter.index(max_value)
    # print(f"max index is {max_index}")
