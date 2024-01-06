import pytube.exceptions
import streamlit as st
from pytube import YouTube
from io import BytesIO

st.title("Download YouTube Video")

try:
    youtube_link = st.text_input(label="Input the YouTube link")
    if youtube_link:
        video = YouTube(youtube_link)
        video_title = video.title
        video_stream = video.streams.get_highest_resolution()

        # Button to confirm the download
        if st.button(f'Download "{video_title}"'):
            # Create a buffer to hold the video data
            video_buffer = BytesIO()
            video_stream.stream_to_buffer(video_buffer)
            video_buffer.seek(0)

            # Provide the buffer to the download button
            st.download_button(label="Save video to file",
                               data=video_buffer,
                               file_name=f"{video_title}.mp4",
                               mime='video/mp4')

except pytube.exceptions.RegexMatchError:
    st.error("Invalid YouTube link. Please check the URL and try again.")

print("TEST")