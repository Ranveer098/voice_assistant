import requests
import os
from PIL import Image
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',180)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


Api_key="3jSdey90Za1E1aBnaxj3xjs5iyUE1pBAvbbhowd1"

def NasaNews(Date):
  speak("Extracting data from Nasa")
  url='https://api.nasa.gov/planetary/apod?api_key='+str(Api_key)
  params={'date':str(Date)}
  r=requests.get(url,params=params)
  Data=r.json()
  Info=Data["explanation"]
  Title=Data['title']
  image_url=Data['url']
  image_r=requests.get(image_url)
  FileName=str(Date)+'.jpg'

  with open (FileName,'wb') as f:
    f.write(image_r.content)

    

    img=Image.open(FileName)
    img.show()
    speak(f"Title:{Title}")
    speak(f"According to Nasa:{Info}")
    speak("news is finished")
    speak("listening.....")



def mar(date):
  name='curiosity'
  speak("Extracting data from Nasa")
  api=str(Api_key)
  url=f'https://api.nasa.gov/mars-photos/api/v1/rovers/{name}/photos?earth_date={date}&api_key={api}'
  params={'date':str(date)}
  r=requests.get(url,params=params)
  Data=r.json()
  photos=Data['photos'][:1]
  try:
      for index,photo in enumerate(photos):
        camera=photo['camera']
        rover=photo['rover']
        rover_name=camera['name']
        full_camera_name=camera['full_name']
        date_of_photo=photo['earth_date']
        # Title=Data['title']
        img_url=photo['img_src']
        p=requests.get(img_url)
        img=f'{index}.jpg'

        with open (img,'wb') as file:
          file.write(p.content)

          img=Image.open(img)
          img.show()
         
          speak(f'this image was captured with :{full_camera_name}')
          speak(f"the date was  :{date_of_photo}")
          speak(f'this image was captured by :{rover_name}')
          speak(f'this image was captured by :{rover}')
  except Exception as e:
    speak("something went wrong")



    


  




