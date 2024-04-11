""" combine_audios.py
    INPUT  : An array(audios_list) returned by tts.py in the form : [[1,'00.0','04.0',"audios/gtts1.mp3"]]
    OUTPUT : Final Audio(media/translated_audio.mp3)
"""
from moviepy.editor import *

class CombineAudios:
    def makeFinalAudio(self,audios_list,lang):
        audio_clips = []
        for audio in audios_list:
            path = audio[3]
            clip = AudioFileClip(path)
            audio_clips.append(clip)
        final_audio = concatenate_audioclips(audio_clips)
        filename = "media/"+lang+"_audio.mp3"
        final_audio.write_audiofile(filename,codec='mp3')
        return filename