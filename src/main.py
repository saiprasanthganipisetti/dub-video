from moviepy.editor import *
import time
one = time.time()
import download_video
import audio_from_video
import srt
import ttt
import tts
import combine_audios
import attach_audio

two = time.time()
print(f"Time for loading all the files is {two-one} seconds")
print("Imported all files")
down = download_video.Download()
afv = audio_from_video.ExtractAudio()
srt = srt.SRTGeneration()
ttt = ttt.Translate()
tts = tts.AudioGeneration()
ca = combine_audios.CombineAudios()
att = attach_audio.Attach()
three = time.time()
print(f"Time for creating objects is {three-two} seconds")
print("Created objects")

if __name__ == '__main__':
    url = "https://www.youtube.com/watch?v=TpLhLBhFTag"
    four = time.time()
    lang = input("Enter the language: ")
    video_path = 'media/english_video.mp4'
    # if 'youtu' in url:
    #     t1 = time.time()
    #     down.download_yt_video(url)
    #     t2 = time.time()
    #     print(f"Time for downloading the video is {t2-t1} seconds")
    #     audio = afv.extract_from_sys(video_path)
    # else:
    #     url = "media/english.mp4"
    #     audio = afv.extract_from_sys(url) #for seperating audio
    #     print("Generated audio file:",audio) #for seperating audio  # Replace with the path to your video file
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    output_audio_path = 'media/english_audio.mp3'  # Replace with the desired output audio file path
    audio_clip.write_audiofile(output_audio_path)
    indian_languages = {"Hindi": "hi","Bengali": "bn","Telugu": "te","Tamil": "ta","Marathi": "mr","Urdu": "ur","Gujarati": "gu","Kannada": "kn","Odia": "or","Malayalam": "ml","Punjabi": "pa","Assamese": "as","Maithili": "mai","Santali": "sat","Kashmiri": "ks","Nepali": "ne","Konkani": "kok","Sindhi": "sd","Manipuri": "mni","Dogri": "dgo","Bodo": "brx","Sanskrit": "sa"}
    language = indian_languages[lang]
    
    five = time.time()
    # print(f"Time for extracting audio is {five-t2} seconds")
    audio = "media/english_audio.mp3"
    srt_file = srt.generateSRT(audio) #for generating srt file in ENGLISH using whisper model
    six = time.time()
    print(f"Time for generating srt file is {six-five} seconds")
    print("Created srt file(srt.py):",srt_file)
    seven = time.time()
    translated_text = ttt.translate_text(srt_file, lang) #for translating text and generating srt file in REGIONAL LANGUAGE
    eight = time.time()
    print(f"Time for translating text and generating translated srt is {eight-seven} seconds")
    print("Translated and generated srt file in regional language(tts.py)")
    audio_clips = tts.generateAudioFiles(translated_text, lang) #for generating audio clips in REGIONAL LANGUAGE
    nine = time.time()
    print(f"Time for generating audio clips is {nine-eight} seconds")
    print("Generated Audio Clips(tts.py)")
    final_audio = ca.makeFinalAudio(audio_clips, lang) #for combining the audio clips according to timelines
    ten = time.time()
    print(f"Time for combining all audio clips is {ten-nine} seconds")
    print("Translated audio file is created(combine_audios.py)")
    final_video = att.attach_audio(video_path, final_audio, lang)
    eleven = time.time()
    print(f"Time for adding audio to video is {eleven-ten} seconds")
    print("Dubbed video is ready(attach_audio.py)")
    print("Done:)")
    print(f"Total time for dubbing the video is {eleven-one} seconds")