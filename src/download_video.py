from pytube import YouTube
class Download:
    def download_yt_video(self, url):
        yt = YouTube(url)
        video = yt.streams.filter(file_extension="mp4",res='720p').first()
        video.download(output_path='media',filename="english_video.mp4")
        return "media/english_video.mp4"