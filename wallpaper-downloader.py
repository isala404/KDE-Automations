import json
import urllib.request
import os
from random import choice
import notify2


WALLPAPER_DIR = '/home/supiri/Pictures/Wallpapers'

os.chdir(WALLPAPER_DIR)


notify2.init("Wallpaper Downloader")

req = urllib.request.Request(
    "https://www.reddit.com/r/wallpaper/top.json?count=1",
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
response = json.loads(urllib.request.urlopen(req).read())
top_image_url = response['data']['children'][0]['data']['preview']['images'][0]['source']['url'].replace(
    'amp;', '')
top_image = top_image_url.split('/')[3].split('?')[0]

req = urllib.request.Request(
    top_image_url,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

with open(top_image, 'wb') as f:
    f.write(urllib.request.urlopen(req).read())

n = notify2.Notification(
    "New Wallpaper Downloaded",
    f"{top_image_url} was added to the collection",
    "notification-message-im"
)

wallpapers = os.listdir()
if(len(wallpapers) > 50):
    random_image = choice(wallpapers)
    os.remove(random_image)
    n.update(
        f"{top_image} was added to the collection and {random_image} was removed")

n.show()
