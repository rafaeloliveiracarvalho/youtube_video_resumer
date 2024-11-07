import os
import assemblyai as aai
from pytubefix import Playlist, YouTube
from pytubefix.cli import on_progress
from dotenv import load_dotenv

load_dotenv()
aai.settings.api_key = os.environ["ASSEMBLYAI_API_KEY"]


def create_folder_if_not_exists(folder_path):
    if not os.path.exists(path=folder_path):
        os.mkdir(path=folder_path)


def download_audio(url, audios_path, title):
    yt = YouTube(url=url, on_progress_callback=on_progress)
    print(f"Download audio from video: '{title}'...")

    ys = yt.streams.get_audio_only()
    ys.download(mp3=True, output_path=audios_path, filename=title)


def download_playlist_audios(url, audios_path):
    video_urls = Playlist(url).video_urls

    for url in video_urls:
        download_audio(url, audios_path)
        break


def transcript_audio(audio_file_path, transcript_file_path):
    print(f"Transcript audio from file: '{audio_file_path}'...")
    transcriber = aai.Transcriber()

    transcript = transcriber.transcribe(data=audio_file_path)

    with open(transcript_file_path, "w") as transcript_file:
        transcript_file.write(transcript.text)


def resume():
    url = "https://www.youtube.com/watch?v=69pvhO6mK_o&list=PL2g2h-wyI4Spf5rzSmesewHpXYVnyQ2TS"
    audios_path = "audios"
    transcripts_path = "transcripts"

    create_folder_if_not_exists(audios_path)
    create_folder_if_not_exists(transcripts_path)

    video_urls = Playlist(url).video_urls

    for url in video_urls:
        # Baixar audio do vídeo
        title = YouTube(url=url).title
        audio_file_name = f"{title}.mp3"
        transcript_file_name = f"{title}.txt"
        download_audio(url, audios_path, title)

        # Transcrição dos áudios
        audio_file_path = f"{audios_path}/{audio_file_name}"
        transcript_file_path = f"{transcripts_path}/{transcript_file_name}"
        transcript_audio(audio_file_path, transcript_file_path)
