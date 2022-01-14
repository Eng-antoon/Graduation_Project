# first start the program and ask the child of his name
# second get the child's name and say hello to him
# gestures game and check if the child moved right
# play the fruit game and if he got it right the move to next game if else retry it
# sing a song with the kid and encourage the kid to sing with him
# start the directions game
# ask him to make some excersices using the dune game by ahmed tarek



import speech_recognition as sr
r = sr.Recognizer()
harvard = sr.AudioFile('audio_files/test.wav')
with harvard as source:
    audio = r.record(source)

type(audio)

print(r.recognize_google(audio))