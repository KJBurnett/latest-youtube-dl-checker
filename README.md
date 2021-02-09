# latest-youtube-dl-checker
Checks the youtube-dl downloads page for the latest youtube-dl.exe and downloads if there's a new version.

## Notes:
Root location to check for latest version.
https://ytdl-org.github.io/youtube-dl/download.html

## Usage
Install the requirements.txt
```
pip install -r requirements.txt
```

Either use this script directly, or import it into an existing python script like so:
```python
from youtubedlchecker import getLatestYoutubeDlVersion
resultLocation = getLatestYoutubeDlVersion()
```
