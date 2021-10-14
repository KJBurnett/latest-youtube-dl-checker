# latest-youtube-dl-checker
Checks the youtube-dl downloads page for the latest youtube-dl.exe and downloads and replaces the existing if there's a new version.

This is useful, because the youtube API, and requirements for youtube-dl to work properly changes on nearly a daily basis, and it is cumbersome to manually upkeep with the changelogs and re-downloading the exe. This script automates this process. And can be imported into existing scripts that call the youtube-dl.exe for a smoother workflow.

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
