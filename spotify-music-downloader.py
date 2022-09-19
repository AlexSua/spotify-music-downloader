import os
import requests
import spotipy
import yt_dlp
import argparse
import time
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = None
CLIENT_SECRET = None
DEFAULT_DIRECTORY = "./music-download/"

def getYoutube(link, cookies={"CONSENT": "PENDING+955"}):
	try:
		response = requests.get(link, cookies=cookies)
		return response.text
	except:
		print("Error: Waiting 3 seconds to reattempt")
		time.sleep(3)
		return getYoutube(link)


def getVideoId(query):
	url = "https://www.youtube.com/results?search_query=" + query
	response = getYoutube(url)
	return response.split('"videoId":"', 1)[1].split('"', 1)[0]


def spotifyListDownload(playlistCode, directory):
	if CLIENT_ID == None or CLIENT_SECRET == None:
		print(
			"You need to provide a client ID and client secret for fetching spotify lists. Use the -sci and -scs arguments for introducing the client ID and secret respectively. You can obtain a spotify client ID and secret by creating a new application here https://developer.spotify.com/dashboard/applications"
		)
		exit(1)
	client_credentials_manager = SpotifyClientCredentials(
		client_id=CLIENT_ID, client_secret=CLIENT_SECRET
	)
	if client_credentials_manager:
		sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
		playlist = sp.playlist(playlistCode)
		for song in playlist["tracks"]["items"]:
			track = song["track"]
			print(track["name"] + " - " + track["artists"][0]["name"])
			downloadedSongName = track["name"] + " - " + track["artists"][0]["name"]
			if not os.path.exists(directory + downloadedSongName + ".mp3"):
				videoId = getVideoId(track["name"] + " " + track["artists"][0]["name"])
				youtubedl(
					"http://www.youtube.com/watch?v=" + videoId,
					directory + downloadedSongName,
				)


def youtubeDownloader(youtubeLink, directory):
	youtubedl(youtubeLink, directory + "%(title)s")


def youtubedl(youtubeLink, directory):
	ydl_opts = {
		"format": "bestaudio[ext=m4a]",
		"outtmpl": directory + ".%(ext)s",
		" --rm-cache-dir": 1,
		"ignoreerrors": True,
		"postprocessors": [
			{
				
				"key": "FFmpegExtractAudio",
				"preferredcodec": "mp3",
				"preferredquality": "192",
			}
		],
	}
	with yt_dlp.YoutubeDL(ydl_opts) as ydl:
		ydl.download([youtubeLink])


def inputChecker(inp):
	return "spotify" if "youtube.com" not in inp else "youtube"


def argumentsParser():
	global CLIENT_ID, CLIENT_SECRET
	directory = DEFAULT_DIRECTORY

	parser = argparse.ArgumentParser()
	parser.add_argument(
		"--spotify_client_id",
		"-sci",
		help="The client ID of the spotify api. Yoy can obtain a spotify client ID and secret by creating a new application here https://developer.spotify.com/dashboard/applications",
	)
	parser.add_argument(
		"--spotify_client_secret",
		"-scs",
		help="The client ID of the spotify api. Yoy can obtain a spotify client ID and secret by creating a new application here https://developer.spotify.com/dashboard/applications",
	)
	parser.add_argument("--input", "-i", help="Spotify list or youtube link")
	parser.add_argument("--output", "-o", help="Folder where to save music")
	args = parser.parse_args()

	
	if not args.input:
		print("You haven't introduced enough arguments.")
		parser.print_help()
		exit(1)
	if args.output:
		if args.output[-1] != "/":
			args.output = args.output + "/"
		directory = args.output
	CLIENT_ID = args.spotify_client_id
	CLIENT_SECRET = args.spotify_client_secret

	input = {"data": args.input, "type": inputChecker(args.input)}
	return input, directory

if __name__ == "__main__":
	input, directory = argumentsParser()
	switcher = {"spotify": spotifyListDownload, "youtube": youtubeDownloader}
	switcher[input["type"]](input["data"], directory)
