# This script catches video-streams by a given m3u8 address.
# Can be used to catch streams from youtube, but also every other non-encrypted livestream

import m3u8
import requests
import subprocess

# Stream-url
url = 'http://demo.unified-streaming.com/video/tears-of-steel/tears-of-steel.ism/.m3u8'

# Folder2Video
f_path = '/Users/marco/Desktop/VideoCatcher/'

# Get m3u8-master
print("Stream-Url:", url)
r = requests.get(url=url)
m3u8_master = m3u8.loads(r.text)
print("Playlists:", m3u8_master.data['playlists'])

# Fetch url to m3u8/playlist that will be always updated
url2playlist = m3u8_master.data['playlists'][1]['uri']
url2playlist = url[:-5] + url2playlist

# append https://
if url2playlist[0:8] != "https://" and url2playlist[0:7] != "http://":
    print(url2playlist[0:8])
    if url2playlist[0:2] != "//":
        print(url2playlist[0:2])
        url2playlist = "https://" + url2playlist
    else:
        url2playlist = "https:" + url2playlist

# Re-load m3u8 every time and write NEW segments to file
evaluated_segments = list()
with open(f_path+"video.ts", 'wb') as f:
    print("Fetching segments from:", url2playlist)
    while True:
        # Load updated playlist
        r = requests.get(url=url2playlist)
        playlist = m3u8.loads(r.text)

        #print(playlist.data)

        # Check if playlist is not empty
        if not playlist.data['segments']:
            print("No segments. Trying again.")
            continue

        segments = playlist.data['segments']
        for segment in segments:
            url2ts = segment['uri']
            url2ts = url[:-5] + url2ts

            # Check if segment is new
            if url2ts in evaluated_segments:
                #print("Already downloaded segment:", url2ts)
                pass
            else: # Segment is not new -> Download and append to video
                print("Fetching new segment:", url2ts)
                ts_file = requests.get(url=url2ts)
                f.write(ts_file.content)
                evaluated_segments.append(url2ts)

# Done
print("Done.")
