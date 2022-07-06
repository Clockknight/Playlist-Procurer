import shutil
from pytube import *
from moviepy.editor import *

url = input("Please input the URL of the YouTube Playlist that you want to Procure.\n\t")
userPlaylist = Playlist(url)
pltitle = userPlaylist.title
if not os.path.exists(pltitle):
        os.makedirs(pltitle)

for video in userPlaylist.videos:
        mediapath4 = video.streams.filter(mime_type="audio/mp4").order_by("abr").last().download()
        clip = AudioFileClip(mediapath4)

        mediapath3 = mediapath4[:-1] + "3"
        filename = os.path.basename(mediapath3)
        clip.write_audiofile(mediapath3, logger=None)

        os.rename(mediapath3, ".\\" + pltitle + "\\"+filename)
        os.remove(mediapath4)
        print(mediapath4)
