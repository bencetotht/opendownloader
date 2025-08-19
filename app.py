import streamlit as st
import yt_dlp
import src.utils as utils
import os

DOWNLOAD_PATH = os.environ.get("DOWNLOAD_PATH", ".")
os.makedirs(DOWNLOAD_PATH, exist_ok=True)

st.title('Downloader')

st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed",
    page_title="Downloader",
    page_icon=":music:",
    menu_items={
        'About': 'https://github.com/bencetotht/opendownloader'
    }
)

platform = st.segmented_control(
    'Select your platform',
    options=['YouTube', 'SoundCloud'],
)

url = st.text_input('Enter the URL', placeholder=f'{"https://www.youtube.com/watch?v=dQw4w9WgXcQ" if platform == "YouTube" else "https://soundcloud.com/user-739338060/sets/top-100-songs"}')

if st.button('Download'):
    resource_name = utils.get_resource_name(url)
    if resource_name == "":
        st.error('Invalid URL')
    else:
        st.write(f'Downloading {resource_name if platform == "YouTube" else "SoundCloud track"}...')
        if platform == 'YouTube':
            try:
                filename = utils.download_audio(url, DOWNLOAD_PATH)
                st.success('Downloaded successfully')
                st.download_button(
                    label="Download",
                    data=open(os.path.join(DOWNLOAD_PATH, filename), 'rb').read(),
                    file_name=filename,
                    mime='audio/mpeg'
                )
            except Exception as e:
                st.error(f'Error downloading audio: {e}')
        elif platform == 'SoundCloud':
            try:
                filename = utils.download_audio_from_soundcloud(url, DOWNLOAD_PATH)
                st.success('Downloaded successfully')
                st.download_button(
                    label="Download",
                    data=open(os.path.join(DOWNLOAD_PATH, filename), 'rb').read(),
                    file_name=filename,
                    mime='audio/mpeg'
                )
            except Exception as e:
                st.error(f'Error downloading audio: {e}')
