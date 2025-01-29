import yt_dlp

def converter(link):
    with yt_dlp.YoutubeDL({'extract_audio': True, 'format':'bestaudio', 'outtmpl':'diretorio/%(title)s.mp3'}) as video:
        info_dict = video.extract_info(link,download=True)
        video_title = info_dict['title']
        print(video_title)
        video.download(link)
