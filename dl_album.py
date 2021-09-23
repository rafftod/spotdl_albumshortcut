#!/usr/bin/env python3
import argparse as ap
import os

from googlesearch import lucky, search
from os import mkdir, chdir

""" This script is meant to download albums from Spotify easily, after creating its directory.
It will :
- Create a directory for the album and move into it.
- Perform a google search to get a Spotify album url from the album name.
- Use spotdl to then download the album (which will actually be downloaded from YouTube Music).

Usage : ./dl_album.py "Artist - Album name"
"""


def main():
    # Argument parsing
    parser = ap.ArgumentParser(description="Downloads an album with spotdl after creating the corresponding directory.")
    parser.add_argument("album_name", type=str, help="Album name. It is also used as directory name.")
    args = parser.parse_args()
    # Create directory and move into it
    try:
        mkdir(args.album_name)
    except FileExistsError:
        print("This album directory already exists. Downloading into it...")
    chdir(args.album_name)
    # Google search
    query = args.album_name + " spotify"
    result: str = lucky(query, num=1, stop=1)  # search and use only top 1 query
    # spotdl download
    os.system(f"spotdl {result}")


if __name__ == '__main__':
    main()
