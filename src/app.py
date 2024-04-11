from flask import Flask, request, jsonify
from moviepy.editor import *
import time
import download_video
import audio_from_video
import srt
import ttt
import tts
import combine_audios
import attach_audio


app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    print("Hello, API!")
    return "Hello, API!"

@app.route('/dub-video', methods=['POST'])
def dub_video():
    data = request.json
    url = data.get('url')
    lang = data.get('lang')

    one = time.time()
    print("Start dubbing process...")
    
    # Download video
    print("Downloading video...")
    down = download_video.Download()
    video_path = down.download_yt_video(url) 
    print("Video downloaded successfully.")
    
    # # Extract audio
    # print("Extracting audio from the video...")
    # video_clip = VideoFileClip(video_path)
    # audio_clip = video_clip.audio
    # output_audio_path = 'media/english_audio.mp3'  # Replace with the desired output audio file path
    # audio_clip.write_audiofile(output_audio_path)
    # print("audio is extracted successfully")
    
    # Convert video to audio
    print(video_path)
    print("Converting video to audio...")
    video_clip = VideoFileClip(video_path)
    print("created video_clip")
    audio_clip = video_clip.audio
    print('created audio obj')
    output_audio_path = 'media/english_audio.mp3'
    print('defined audio path')
    audio_clip.write_audiofile(output_audio_path)
    print("Video converted to audio successfully.")
    
    # Generate SRT
    print("Generating SRT file...")
    srt_gen = srt.SRTGeneration()
    srt_file = srt_gen.generateSRT(output_audio_path)
    print("SRT file generated successfully.")
    
    # Translate text
    print("Translating text...")
    ttt_trans = ttt.Translate()
    translated_text = ttt_trans.translate_text(srt_file, lang)
    print("Text translated successfully.")
    
    # Generate audio
    print("Generating audio clips...")
    tts_audio = tts.AudioGeneration()
    audio_clips = tts_audio.generateAudioFiles(translated_text, lang)
    print("Audio clips generated successfully.")
    
    # Combine audio clips
    print("Combining audio clips...")
    ca_combine = combine_audios.CombineAudios()
    final_audio = ca_combine.makeFinalAudio(audio_clips, lang)
    print("Audio clips combined successfully.")
    
    # Attach audio to video
    print("Attaching audio to video...")
    att_attach = attach_audio.Attach()
    final_video = att_attach.attach_audio(video_path, final_audio, lang)
    print("Audio attached to video successfully.")
    
    two = time.time()
    total_time = two - one
    print("Dubbing process completed.")
    
    return jsonify({"status": "success", "message": "Dubbing completed.", "total_time": total_time})


if __name__ == '__main__':
    app.run(debug=True)
