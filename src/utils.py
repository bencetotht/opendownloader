import yt_dlp
import os
from sclib import SoundcloudAPI, Track, Playlist

def get_resource_name(url: str) -> str:
    """
    Extract the name of the resource from the URL.
    """
    if len(url.split('=')) > 1:
        return url.split('=')[-1]
    else:
        return url.split('/')[-1]

def download_audio(url: str, output_path: str = ".") -> str:
    """
    Download an audio from a URL and save it to the output path.
    """
    ydl_opts = {
        'format': 'ba',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'outtmpl': f'{output_path}/{get_resource_name(url)}.%(ext)s',
    }

    resource_name = get_resource_name(url)
    if resource_name == "":
        raise Exception("Invalid video URL")
    try:
        print(f'Trying to download {resource_name}.mp3')
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"Downloaded {resource_name}.mp3")
            return f"{resource_name}.mp3"
    except Exception as e:
        print(f"Error downloading audio: {e}")
        raise e


def download_audio_from_soundcloud(url: str, output_path: str = ".") -> str:
    """
    Download an audio from a SoundCloud URL and save it to the output path.
    """
    try:
      api = SoundcloudAPI()
      track = api.resolve(url)

      assert isinstance(track, Track)
      filename = f'{track.artist} - {track.title}.mp3'
      filename = filename.replace('/', '_')

      print(f'Downloading {filename}...')

      # os.makedirs(os.path.dirname(filename), exist_ok=True)
      with open(f'{output_path}/{filename}', 'wb+') as f:
          track.write_mp3_to(f)
      print(f'Downloaded {track.artist} - {track.title}')
      return filename
    except Exception as e:
      print(f'Error downloading audio: {e}')
      raise e
