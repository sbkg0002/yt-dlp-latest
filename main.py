import scrapetube
import yt_dlp


def dlvideo(channel: str, limit: int = 20) -> None:
    videos = scrapetube.get_channel(channel_username=channel, limit=limit, sort_by="newest", content_type="videos")
    yt_opts = {
        'verbose': False,
        "format": "mp4[height=720]",
        "writethumbnail": False,
        "outtmpl": "%(uploader)s/%(title)s.%(ext)s"
    }
    ydl = yt_dlp.YoutubeDL(yt_opts)

    for video in videos:
        vide_url = f"https://www.youtube.com/watch?v={video['videoId']}"

        print(f'Downloading: {vide_url}..')
        ydl.download(vide_url)


# channel_list = ["BobdeBouwerOfficieel"]
# channel_list = ["jilloptv"]
# channel_list = ["deofficielepeppa"]
# channel_list = ["BingNederlands"]
channel_list = ["BumbaNL"]
# channel_list = ["Dutchtuber2", "WalnutMax"]
for channel in channel_list:
    dlvideo(channel=channel, limit=40)
