import pytube
from pytube.cli import on_progress

# Ask user for YouTube video URL and download location
url = input("Enter YouTube video URL: ")
download_path = r"C:\Users\chadl\Downloads"

# Create YouTube object and download video
yt = pytube.YouTube(url,on_progress_callback=on_progress)
stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
stream.download(download_path)
print("Video downloaded successfully to", download_path)