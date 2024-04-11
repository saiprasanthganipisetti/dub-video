""" audio_from_video.py
    INPUT  : URL or path of the English video 
    OUTPUT : Seperated English audio file
"""

# pip install moviepy
# pip install pytube
# pip install gdown

#for downloading 
from moviepy.editor import *
#for downloading from youtube
import datetime
from pytube import YouTube
from pytube.innertube import _default_clients
import re
#for downloading from google drive
# import gdown
# _default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID"]

class ExtractAudio:
    def extract_from_sys(self,path):
        video = VideoFileClip(path)
        audio = video.audio
        timestamp = str(datetime.datetime.now())[:19]
        audio_file_title = "media/english_audio"+".mp3"
        audio.write_audiofile(audio_file_title)
        
    def extract_from_yt(self,url):
        yt = YouTube(url,use_oauth=True, allow_oauth_cache=True) #creating object
        timestamp = str(datetime.datetime.now())[:19] #for assigning unique title to each audio file we extract
        audio_file_title = timestamp + yt.author 
        audio_file_title = "media/" + re.sub(r"[-:. ]","",audio_file_title)+'.mp3'
        # To get audio file from the url
        audio = yt.streams.filter(only_audio=True, file_extension='mp4').first()
        audio.download(output_path='.',filename=audio_file_title)
        return audio_file_title
    # def extract_from_drive(self,url):
    #     timestamp = str(datetime.datetime.now())[:19]
    #     timestamp = re.sub(r"[: -]","",timestamp)
    #     file_name = "drive"+timestamp+".mp3"
    #     gdown.download(url,file_name,quiet=False)
