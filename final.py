import pyttsx3  # text to speech
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import cv2
import numpy as np
from requests import get
import pywhatkit
import smtplib
import sys
import pyjokes
import pyautogui
import time
import requests
from instadownloader import instaloader
import PyPDF2
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import urllib.request
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from chitti import Ui_chitti


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',180)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def DateConverter(Query):
   
    Query=Query.replace("and","-")
    Query=Query.replace(":","-")
    Query=Query.replace(".","-")
    Query=Query.replace("and","-")
    Query=Query.replace("and","-")
    Query=Query.replace(" ","")
    return str(Query)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello sir,I  am chitti")
    speak("reloaded version 2.O") 
    speak("Your personal AI assistant") 
    speak("how may i help you")      

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.Task()



    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            speak("Listening...")
            audio=r.listen(source,timeout=8,phrase_time_limit=7)

        try:
            print("Recognizing...")
            #speak("Recognizing...")     
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e: 
            #speak("Say that again please...")  
            return "None"
        query=query.lower()
        return query


    def TaskExecution(self):
        pyautogui.press('esc')
        speak("Face verification is successfull")
        speak("Welcome back sir")
        wishMe()
        while True:
            self.query = self.takeCommand()
            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("search", "")
                self.query = self.query.replace("on", "")
                self.query = self.query.replace(" wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in self.query or 'youtube' in self.query:
                speak("what should i search")
                self.query=self.takeCommand()
                self.query=self.query.replace('search','')
                speak("opening Youtube")
                web='https://www.youtube.com/results?search_query='+self.query
                webbrowser.open(web)

            elif 'google' in self.query:
                speak("sir,what's should i search on google")
                cm = self.takeCommand()
                speak("opening google")
                speak(f"searching {cm} on google")
                webbrowser.open(f'{cm}')


                    
            elif 'open stack overflow' in self.query:
                speak('opening stackoverflow')
                webbrowser.open("stackoverflow.com")   


            elif 'play music' in self.query or 'music' in self.query:
                music_dir = "E:\\music"
                songs = os.listdir(music_dir)
                speak("playing song ! enjoy your music")
                ran = random.choice(songs)
                os.startfile(os.path.join(music_dir, ran)) 

            elif 'visual' in self.query or 'vs code'in self.query:
                speak("opening visual studio")
                codePath = "C:\\Users\\Ranveer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
                    
            elif ' find my Ip' in self.query or 'ip' in self.query:
                speak('finding your ip address')
                ip = get('https://api.ipify.org').text
                speak(f"your Ip address is {ip}")


            elif 'you can sleep' in self.query or 'sleep' in self.query:
                speak("sleeping sir")
                sys.exit()

            
            elif 'cmd' in self.query or 'open command prompt' in self.query:
                speak("opening command prompt")
                os.system("start cmd")

            
            elif 'song on youtube' in self.query:
                speak("which song would you like to listen")
                cm=self.takeCommand()
                speak("playing song on youtube")
                pywhatkit.playonyt(f"{cm}")


            elif 'tell me a joke' in self.query or 'joke' in self.query:
                speak("let me tell you a joke")
                my_joke = pyjokes.get_joke(language="en", category="neutral")
        
                speak(my_joke)
                speak("did you laugh")
            
            elif ' where i am' in self.query or 'location'  in self.query:
                speak("please  wait sir,let me check")
                try:
                    ip_address = get('https://api.ipify.org').text
                    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
                    region = response.get("region")
                    city=response.get('city')

                    country = response.get("country_name")
                    print(city)
                    speak(f"sir,i am not sure, but i think we are in{city} of {region} of {country}")
                except Exception as e:
                    speak("sorry sir,Due to network issue i am not able to find our current location")



            elif 'switch tab' in self.query or 'switch the window'in self.query:
                speak("switching tab")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
            

            elif 'open insta' in self.query or 'instagram' in self.query:
                speak("opening instagram")
                speak("sir,please enter the username correctly")
                user_name = input("Enter username here:")
                webbrowser.open(f"www.instagram.com/{user_name}")
                time.sleep(5)
                mod = instaloader.Instaloader()
                mod.download_profile(user_name, profile_pic_only=True)
                speak("profile is saved successfully in main folder.  Now i am ready for your next command")
                
                
            elif ' take screenshot' in self.query or 'screenshot' in self.query:
                speak("taking screenshot")
                speak("sir,please tell me  the name of this screenshot file")
                name = self.takeCommand()
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("screenshot is saved successfully in main folder")
            
            elif 'open camera' in self.query :
                
                speak("opening camera")
                speak("for capturing image press space bar and for closing press Escape")
                cam = cv2.VideoCapture(0)
                count = 0
                while True:
                    ret, img = cam.read()
                    cv2.imshow("Test", img)
                    if not ret:
                        break
                    k=cv2.waitKey(1)
                    if k%256==27:
                        #For Esc key
                        speak("Closing camera")
                        break
                    elif k%256==32:
                        #For Space key
                        print("Image "+str(count)+"saved")
                        file='C:/Users/Ranveer/Desktop/docs/img'+str(count)+'.jpg'
                        cv2.imwrite(file, img)
                        count +=1
                        speak("image is captured")
                        
                cam.release
                cv2.destroyAllWindows


            elif'restart the system' in self.query or 'restart' in self.query:
                speak("Restarting the system")
                os.system("shutdown /r /t 5")

            
            elif 'shutdown' in self.query: 
                speak('closing system')  
                os.system("shutdown /s /t 5")
            
            elif 'hello' in self.query or 'hey' in self.query:
                speak("hello sir,may i help you")

            elif 'how are you' in self.query or 'are you' in self.query:
                speak("i am fine sir,what's about you")
            
            elif 'also good' in self.query or 'fine' in self.query:
                speak("that's great to hear from you")
            
            elif 'thank you' in self.query or 'thanks' in self.query:
                speak("pleasure is mine ,sir")
            
            elif 'temperature' in self.query or 'weather' in self.query:
                try:  
                    speak("tell me the place name")
                    cd=self.takeCommand()
                    speak("please wait let me check")
                    url=f'https://www.google.com/search?q=temperature in {cd}'
                    r=requests.get(url)
                    data=BeautifulSoup(r.text,"html.parser")
                    temp=data.find("div",class_="BNeawe").text
                    speak(f"current temperature  in {cd} is {temp}")
                except Exception as e:
                    speak("sorry sir Due to network issue i am not able to find current temperature")


            
            elif ' to do mode' in self.query or 'to do' in self.query:
                speak("how to do mode is activated")
                while True:
                    speak("please tell me what you want to know")
                    cd=self.takeCommand()
                    try:
                        if 'exit' in cd or ' close ' in cd:
                            speak("okay sir, how to do mode is closed")
                            break
                        else:
                            max_results=1
                            how_to=search_wikihow(cd,max_results)
                            assert len(how_to) == 1
                            how_to[0].print()
                            speak(how_to[0].summary)
                    except Exception as e:
                        speak("sorry sir, i am not able to find this")

            
            elif ' volume up' in self.query :
                speak("volume is up")
                pyautogui.press("volumeup")

            elif ' volume down' in self.query or 'down' in self.query:
                speak("volume is down")
                pyautogui.press("volumedown")

            elif 'volume mute' in self.query or ' mute' in self.query:
                speak("muting")
                pyautogui.press("volumemute")
            
            elif 'mobile' in self.query :
                try:
                    speak("opening mobile cam, for closing press q")
                    URL="http://10.1.42.19:8080/shot.jpg"
                    while True:
                        img_arr=np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                        img=cv2.imdecode(img_arr,-1)
                        cv2.imshow('IPWebcam',img)
                        q=cv2.waitKey(1)
                        if q==ord("q"):
                            speak("closing mobile webcam")
                            break;
                    cv2.destroyAllWindows()
                except Exception as e:
                    speak("sorry sir ,mobile cam is not responding")

            elif 'send message' in self.query or 'open whatsapp' in self.query or 'whatsapp' in self.query:
                from datetime import datetime
                now = datetime.now()
                hou = now.strftime("%H")
                min = now.strftime("%M")
                d=int(min)+2
                e=int(hou)
                speak(" please tell me the name of the person")
                name=self.takeCommand()
                if "suman" in name:
                    speak("tell me the message")
                    msg=self.takeCommand()
                    pywhatkit.sendwhatmsg("+919122283635",f'{msg}',e,d,20)
                    speak("okay sir ,message is sent successfully")
                
                elif 'anirudh' in name or 'aniruddh' in name:
                    speak("tell me the message")
                    msg=self.takeCommand()
                    pywhatkit.sendwhatmsg("+919406119726",f'{msg}',e,d,20)
                    speak("okay sir ,message is sent successfully")

                elif 'sunny' in name :
                    speak("tell me the message")
                    msg=self.takeCommand()
                    pywhatkit.sendwhatmsg("+9779809242787",f'{msg}',e,d,20)
                    speak("okay sir ,message is sent successfully")
                else:
                    pass
            
            elif 'remember ' in self.query :
                remeberMsg = self.query.replace("remember that","")
                remeberMsg = remeberMsg.replace("remember this","")
                speak("You Tell Me To Remind You That :"+remeberMsg)
                remeber = open('data.txt','w')
                remeber.write(remeberMsg)
                remeber.close()
            
            elif 'what do you remember' in self.query:
                remeber = open('data.txt','r')
                speak("You Tell Me That" + remeber.read())

            elif 'space news' in self.query or 'nasa news' in self.query:
                speak("please tell me the date")
                try:
                    Date=self.takeCommand()
                    
                    value=DateConverter(Date)

                    from nasa import NasaNews
                    NasaNews(value)
                except Exception as e:
                    speak("sorry sir,please Date format was incorrect")

            
            elif 'mars' in self.query or 'image' in self.query:
                speak("please tell me the date")
                try:
                    Date=self.takeCommand()
                    
                    value=DateConverter(Date)

                    from nasa import mar
                    mar(value)
                except Exception as e:
                    speak("sorry sir,Date format was incorrect")
            
            elif 'open notepad' in self.query:
                path="C:\\Windows\\notepad.exe"
                os.startfile(path)
           

    
                

            
    def Task(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
        recognizer.read('trainer/trainer.yml')   #load trained model
        cascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

        font = cv2.FONT_HERSHEY_SIMPLEX 


        id = 2 

        names = ['','Ranveer']  

        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
        cam.set(3, 640) # set video FrameWidht
        cam.set(4, 480) # set video FrameHeight

        # Define min window size to be recognized as a face
        minW = 0.1*cam.get(3)
        minH = 0.1*cam.get(4)

        # flag = True

        while True:

            ret, img =cam.read() #read the frames using the above created object

            converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

            faces = faceCascade.detectMultiScale( 
                converted_image,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize = (int(minW), int(minH)),
            )

            for(x,y,w,h) in faces:

                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

                id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

                # Check if accuracy is less them 100 ==> "0" is perfect match 
                if (accuracy < 100):
                    id = names[id]
                    accuracy = "  {0}%".format(round(100 - accuracy))
                    self.TaskExecution()

                else:
                    id = "unknown"
                    accuracy = "  {0}%".format(round(100 - accuracy))
                
                cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
            
            cv2.imshow('camera',img) 

            k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
            if k == 27:
                break

        # Do a bit of cleanup
        print("Thanks for using this program, have a good day.")
        cam.release()
        cv2.destroyAllWindows()



startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_chitti()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):

        self.ui.movie = QtGui.QMovie("../../PythonProj_GUI/Intercept_Echo_v2-3.5MB-2-1542062294.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../PythonProj_GUI/ini.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../PythonProj_GUI/result.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)
    

app = QApplication(sys.argv)
chitti = Main()
chitti.show()
sys.exit(app.exec_())



