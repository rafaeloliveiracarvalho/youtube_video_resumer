# Baixar audio do vídeo

import os
from pytubefix import Playlist, YouTube
from pytubefix.cli import on_progress


def download_audio(url, audios_path):
    yt = YouTube(url=url, on_progress_callback=on_progress)
    print(f"Download audio from video: '{yt.title}' | ")

    ys = yt.streams.get_audio_only()
    ys.download(mp3=True, output_path=audios_path)


def download_playlist_audios(url, audios_path):
    video_urls = Playlist(url).video_urls

    for url in video_urls:
        download_audio(url, audios_path)


# Transcrição do áudio
# Fazer resumo com IA
def resume():
    url = "https://www.youtube.com/watch?v=69pvhO6mK_o&list=PL2g2h-wyI4Spf5rzSmesewHpXYVnyQ2TS"
    audios_path = "youtube_video_resumer/audios"

    if not os.path.exists(path=audios_path):
        os.mkdir(path=audios_path)

    download_playlist_audios(url, audios_path)
