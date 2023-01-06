import speech_recognition as sr
from gtts import gTTS
import os
import openai
import serial
import time

r = sr.Recognizer()

mic = sr.Microphone()
test = sr.AudioFile('test.flac')
print("Start talking")
with mic as source:
    audio = r.listen(source)

result = r.recognize_google(audio)


print(result)

##    ## 

# set up the serial line
ser = serial.Serial('/dev/cu.usbmodem2101', 9600)
time.sleep(2)


# Read and record the data
data =[]                       # empty list to store the data
for i in range(5):
    b = ser.readline()         # read a byte string
    string_n = b.decode()  # decode byte string into Unicode  
    string = string_n.rstrip() # remove \n and \r
    flt = float(string)        # convert string to float
    print(flt)
    data.append(flt)           # add to the end of data list
    # time.sleep(0.1)            # wait (sleep) 0.1 seconds

ser.close()
##AI
language = 'en'
if data[0] > 200:
    myobj = gTTS(text="Please sit on me to talk", lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("mpg321 welcome.mp3")
    print("KOM OP MIJ ZITTEN")
    exit()
openai.api_key = "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"

response = openai.Completion.create(model="text-davinci-003", prompt="You are a chair please answer this: " + "?"+ result, temperature=0, max_tokens=4097 - (result.__len__()+20))

answer = response["choices"][0]["text"]
print(answer)
###


language = 'en'
myobj = gTTS(text=answer, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("mpg321 welcome.mp3")
