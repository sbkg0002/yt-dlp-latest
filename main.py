import scrapetube
import yt_dlp
import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Download some YT channels.')

# Add the optional flag for the directory
parser.add_argument('-d', '--directory', type=str, help='The root directory to store videos.', default='.')
args = parser.parse_args()
directory = args.directory


def dlvideo(channel: str, limit: int = 20) -> None:
    videos = scrapetube.get_channel(channel_username=channel, limit=limit, sort_by='newest', content_type='videos')
    yt_opts = {
        'verbose': False,
        'format_sort': ['res:720', 'ext:mp4:m4a'],
        'writethumbnail': False,
        'outtmpl': f'{directory}/%(uploader)s/%(title)s.%(ext)s'
    }
    ydl = yt_dlp.YoutubeDL(yt_opts)

    for video in videos:
        vide_url = f'https://www.youtube.com/watch?v={video["videoId"]}'

        print(f'Downloading: {vide_url}..')
        try:
            ydl.download(vide_url)
        except ydl.ExtractError as e:
            print(f'Tring alterative for {video}({e})')
        except yt_dlp.utils.DownloadError as e:
            print(f'Tring alterative for {video}({e})')
        else:
            yt_opts = {
                'verbose': False,
                'format': 'best[ext=mp4]',
                'writethumbnail': False,
                'outtmpl': f'{directory}/%(uploader)s/%(title)s.%(ext)s'
            }
            ydl.download(vide_url)


# channel_list = ['BobdeBouwerOfficieel']
# channel_list = ['jilloptv', 'EOCheckpoint', 'GameBawz']
# channel_list = ['EOCheckpoint']
# channel_list = ['deofficielepeppa']
# channel_list = ['BingNederlands']
# channel_list = ['MegaTrucks157']
channel_list = ['creachickofficial']
for channel in channel_list:
    dlvideo(channel=channel, limit=30)
