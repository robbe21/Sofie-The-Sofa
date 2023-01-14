import speech_recognition as sr
from gtts import gTTS
import os
import openai
import serial
import time

r = sr.Recognizer()
mic = sr.Microphone()
test = sr.AudioFile('test.flac')



## Hey isabel hier kan je dingentjes aanpassen#

lichtsensorthreshold = 200


###
# set up the serial line
lichtsensor = 1000

# Read and record the data
while lichtsensor > lichtsensorthreshold:
    ser = serial.Serial('/dev/cu.usbmodem2101', 9600)
    data =[]                       # empty list to store the data
    for i in range(1):
        b = ser.readline()         # read a byte string
        string_n = b.decode()  # decode byte string into Unicode  
        string = string_n.rstrip() # remove \n and \r
        flt = float(string)        # convert string to float
        print(flt)
        data.append(flt)           # add to the end of data list
        lichtsensor = data[0]

    ser.close()
##AI
language = 'en'
# if data[0] > lichtsensorthreshold:
myobj = gTTS(text="Hey how are you? Got any questions for me?", lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("mpg321 welcome.mp3")
# print("KOM OP MIJ ZITTEN")
# exit()

print("Start talking")
with mic as source:
    audio = r.listen(source)

result = r.recognize_google(audio)

print(result)


openai.api_key = "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"

response = openai.Completion.create(model="text-davinci-003", prompt="You are a chair you are made from wool and your creators name is Isabel Brems. please answer this: " + result + "?", temperature=0, max_tokens=4097 - (result.__len__()+20))

answer = response["choices"][0]["text"]
print(answer)
###


language = 'en'
myobj = gTTS(text=answer, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("mpg321 welcome.mp3")
