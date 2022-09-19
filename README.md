<a name="readme-top"></a>
<!-- PROJECT LOGO -->
<div align="center">

<h1 align="center">spotify-music-downloader</h2>

  <p align="center">
    A small script to get your music Spotify/Youtube lists locally.
    <br />
    <br />
 <div align="center">


[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



</div>
    <a href="https://github.com/AlexSua/spotify-music-downloader/issues">Report Bug</a>
    ·
    <a href="https://github.com/AlexSua/spotify-music-downloader/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#install-required-python-dependencies">Install required python dependencies</a></li>
      </ul>
    </li>
    <li>
	<a href="#usage">Usage</a>
	<ul>
        <li><a href="#get-spotify-playlist">Get Spotify playlist</a></li>
        <li><a href="#get-youtube-playlist/element">Get youtube playlist/element</a></li>
      </ul>
	</li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>
</br>

<!-- ABOUT THE PROJECT -->
## About The Project
With this script you can download your music from Spotify or Youtube by only providing an ID or a link to your playlists. It uses the library called [yt-dlp](https://github.com/yt-dlp/yt-dlp), a fork of the well-known library [youtube-dl](https://github.com/ytdl-org/youtube-dl) for executing the download process from Youtube.

The script uses the API of Spotify to fetch the specified playlist and then it searches for each song on youtube, to subsequently download each video and transform it into audio. You can use the script to download as well a playlist or an independent element from Youtube.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started
### Prerequisites

Before using the application you need to have installed [python](https://www.python.org/) and the package manager of Python, [pip](https://pip.pypa.io/en/stable/installation/). You can get instructions on how to install both requirements by following the links shown before.

### Install required python dependencies

To get the script working you need to follow the steps shown below.

1. Clone the repo

   ```bash
   git clone https://github.com/AlexSua/spotify-music-downloader.git
   ```

2. Enter the project directory:

   ```bash
   cd spotify-music-downloader
   ```

3. Install python dependencies by executing the following command.

   ```bash
   pip3 install -r requirements.txt
   ```

With the steps mentioned above, you should be ready to use the script.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage
You can check the documentation of the script by typing:

   ```bash
   python3 spotify-music-downloader.py
   ```

### Get Spotify playlist


   ```bash
   python3 spotify-music-downloader.py -sci <CLIENT_ID> -scs <CLIENT_SECRET> -i <SPOTIFY_LIST_ID> -o <OUTPUT_FOLDER>
   ```
where:

- **\-sci**: Spotify API client ID.
- **\-scs**: Spotify API client secret.
- **\-i**: Id of the Spotify playlist.
- **\-o**: Output folder where audios are going to be saved.

> The Spotify client ID and Secret are required to fetch Spotify playlists and can be obtained by creating a new application in the following URL: [https://developer.spotify.com/dashboard/applications](https://developer.spotify.com/dashboard/applications).

### Get Youtube playlist/element
   ```bash
   python3 spotify-music-downloader.py -i <YOUTUBE_URL> -o <OUTPUT_FOLDER>
   ```
where:
- **\-i**: Youtube playlist link *youtube.com/playlist* or youtube video link *youtube.com/watch*
- **\-o**: Output folder where audios are going to be saved.


  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Project Link: [https://github.com/AlexSua/spotify-music-downloader](https://github.com/AlexSua/spotify-music-downloader)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


[issues-shield]: https://img.shields.io/github/issues/AlexSua/spotify-music-downloader?style=flat-square
[issues-url]: https://github.com/AlexSua/spotify-music-downloader/issues

[license-shield]: https://img.shields.io/github/license/AlexSua/spotify-music-downloader?style=flat-square
[license-url]: https://github.com/AlexSua/spotify-music-downloader/blob/main/LICENSE.txt
