# Baixar audio do vídeo

from pytubefix import Playlist, YouTube
from pytubefix.cli import on_progress
import os

url = "https://www.youtube.com/watch?v=69pvhO6mK_o&list=PL2g2h-wyI4Spf5rzSmesewHpXYVnyQ2TS"

audios_path = "youtube_video_resumer/audios"


def download_playlist_audios(url):
    video_urls = Playlist(url).video_urls

    if not os.path.exists(path=audios_path):
        os.mkdir(path=audios_path)

    for url in video_urls:
        yt = YouTube(url=url, on_progress_callback=on_progress)
        print(f"Download audio from video: '{yt.title}' | ")

        ys = yt.streams.get_audio_only()
        ys.download(mp3=True, output_path=audios_path)


# Transcrição do áudio
# Fazer resumo com IA
def resume():
    download_playlist_audios(url)
