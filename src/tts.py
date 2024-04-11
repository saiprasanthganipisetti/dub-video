""" tts.py
    INPUT  : Array returned by ttt(srt_array) in the form [[1,'00.0','04.0',"Welcome, everyone."]]
    OUTPUT : Individual audio clips for each subtitle present in the subtitles/translated_srt.srt
"""
# import ttt
from gtts import gTTS
# tt = ttt.Translate()
class AudioGeneration:
    def generateAudioFiles(self, source, lang):
        count = 1
        audios_list = source
        d = {"Hindi": "hi","Bengali": "bn","Telugu": "te","Tamil": "ta","Marathi": "mr","Urdu": "ur","Gujarati": "gu","Kannada": "kn","Odia": "or","Malayalam": "ml","Punjabi": "pa","Assamese": "as","Maithili": "mai","Santali": "sat","Kashmiri": "ks","Nepali": "ne","Konkani": "kok","Sindhi": "sd","Manipuri": "mni","Dogri": "dgo","Bodo": "brx","Sanskrit": "sa"}
        for i in range(len(source)):
            text = source[i][3]
            title = "./audios/"+lang+str(count)+".mp3"
            tts = gTTS(text=text, lang=d[lang]) 
            tts.save(title)
            audios_list[i][3] = title 
            count += 1
        return audios_list

# source = tt.translate_text('subtitles/english_srt.srt','te')
# AudioGeneration().generateAudioFiles(source)