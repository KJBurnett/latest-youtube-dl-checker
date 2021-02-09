# Author: Kyler Burnett

# Notes:
# Root location to check for latest version.
# https://ytdl-org.github.io/youtube-dl/download.html

# USAGE
# Install the requirements.txt: pip install -r requirements.txt
# Either use this script directly, or import it into an existing python script like so:
# from youtubedlchecker import getLatestYoutubeDlVersion
# resultLocation = getLatestYoutubeDlVersion()

import requests
import os

# Set downloadPath to the directory where you want youtube-dl.exe to be downloaded to.
downloadPath = "C:/Users/user/Downloads/gohere"


def downloadFile(downloadPath, url):
    fileName = os.path.join(downloadPath, url.split("/")[-1])
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(fileName, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return fileName

def getLatestYoutubeDlVersion():
    print("Checking ytdl for the latest youtube-dl.exe version...")
    downloadsPage = requests.get("https://ytdl-org.github.io/youtube-dl/download.html")
    siteVersion = downloadsPage.text.split('href="https://yt-dl.org/downloads/')[1].split(
        '/youtube-dl.exe">Windows exe'
    )[0]
    print("Version found on site: " + siteVersion)

    currentVersion = ""
    # Create current_version.txt if it does not already exist.
    if not os.path.isfile("current_version.txt"):
        file = open("myfile.dat", "w+").close()
    else:
        with open("current_version.txt", "r") as f:
            currentVersion = f.read().replace("\n", "")

    if siteVersion != currentVersion:  # It's a new version folks.
        print("A new version of youtube-dl.exe was found!")
        # Write new version to file.
        with open("current_version.txt", "w+") as f:
            f.write(siteVersion)

        url = "https://yt-dl.org/downloads/{0}/youtube-dl.exe".format(siteVersion)

        print("Downloading new file...")
        downloadFile(downloadPath, url)
        print("Download complete!\n youtube-dl.exe downloaded to: " + downloadPath)
        return os.path.join(downloadPath, "youtube-dl.exe")
    else:
        alreadyExistsMsg = "Already on latest version of youtube-dl.exe\nEnd of Line."
        print(alreadyExistsMsg)
        return(alreadyExistsMsg)

if __name__ == '__main__':
   getLatestYoutubeDlVersion()
