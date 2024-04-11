""" srt.py
    INPUT : Audio      
    OUTPUT: English srt file(english_srt.srt)
    It generates srt file in ENGLISH language taking an audio
"""
import warnings

# Filter out the specific warning
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")
import whisper
model = whisper.load_model("base")

class SRTGeneration:
    def generateSRT(self,audio):
        transcription = model.transcribe(audio)
        f = open('transcripts/english-transcript.txt','w',encoding='utf-8')
        f.write(transcription['text'])
        count = 1
        flag = 0
        temp_text = ""
        with open("subtitles/english_srt.srt", "w", encoding='utf-8') as srt_file:
            for segment in transcription["segments"]:
                text = segment["text"]
                if text[-1] == '.':
                    if flag == 0:
                        start_time = str(0) + str(segment["start"])
                        end_time = str(0) + str(segment["end"])
                        srt_file.write(f"{count}\n{start_time} --> {end_time}\n{text}\n\n")
                        count += 1
                    else:
                        end_time = str(0) + str(segment["end"])
                        srt_file.write(f"{count}\n{start_time} --> {end_time}\n{temp_text+text}\n\n")
                        count += 1
                        flag = 0
                        temp_text = ""
                else:
                    start_time = str(0) + str(segment["start"])
                    temp_text += text
                    flag = 1

        return "subtitles/english_srt.srt"



