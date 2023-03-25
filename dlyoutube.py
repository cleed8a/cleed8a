import pytube

# Ask user for YouTube video URL and download location
url = input("Enter YouTube video URL: ")
download_path = input("Enter download location: ")

# Create YouTube object and download video
yt = pytube.YouTube(url)
stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
stream.download(download_path)
print("Video downloaded successfully to", download_path)