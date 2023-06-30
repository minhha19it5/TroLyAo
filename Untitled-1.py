import speech_recognition as sr
import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound
from datetime import datetime
import wikipedia
import webbrowser as wb
# datetime object containing current date and time
now = datetime.now()



def speak(text):
    tts = gTTS(text=text, lang='vi')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)



def command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        #Thu am
        audio_data = r.record(source, duration=5)
        print("Recording for 4 seconds")
        #Chuyen giong noi sang text
        try:
            text = r.recognize_google(audio_data, language="vi")
        except:
            text =""    
        print(text)
    return text



if __name__  =="__main__":
    

    while True:
        text=command().lower()
        #All the command will store in lower case for easy recognition
        if text =="":
            sara ="Tôi đang lắng nghe bạn nè"
            print(sara)
            speak(sara)
        elif "Xin chào" in text:
            sara ="Xin chào bạn"
            print(sara)
            speak(sara)
        elif "xin chào" in text:
            sara ="Xin chào Bạn"
            print(sara)
            speak(sara)
        elif "ngày bao nhiêu" in text:
            sara =now.strftime("Hôm nay là ngày %d/%m/%Y")
            print(sara)
            speak(sara)
        elif "Ngày bao nhiêu" in text:
            sara =now.strftime("Hôm nay là ngày %d/%m/%Y")
            print(sara)
            speak(sara)
        elif "mấy giờ" in text:
            sara =now.strftime("%H:%M:%S")
            print(sara)
            speak(sara)
        elif "Mấy giờ" in text:
            sara =now.strftime("%H:%M:%S")
            print(sara)
            speak(sara)
        elif "google" in text:
            speak("Bạn muốn tìm kiếm gì trên google")
            search=command().lower()
            url = f"https://google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Kết quả tìm kiếm cho {search} trên google')
        
        elif "youtube" in text:
            speak("Bạn muốn tìm kiếm gì trên youtube")
            search=command().lower()
            url = f"https://youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Kết quả tìm kiếm cho {search} trên youtube')
    
        
        elif "tạm biệt" in text:
            sara ="Sara Tạm biệt bạn"
            print(sara)
            speak(sara)
            break
        elif text:
            wikipedia.set_lang("vi")
            sara = wikipedia.summary(text, sentences=1)
            print(sara)
            speak(sara)
        else:
            sara ="Bạn muốn nói gì với tôi"
            speak(sara)    



        
   


