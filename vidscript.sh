#!/bin/sh
# Frame Buffer Youtube Player
# Dependencies: youtube-dl

echo "$@"
VID=$(youtube-dl --get-filename "$@")
printf "Filename: %s\n" "$VID"
youtube-dl "$@"

if fgconsole > /dev/null 2>&1
  then mplayer -vo fbdev "$VID"
  else mplayer "$VID"
fi

