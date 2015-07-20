#!/bin/sh
# Frame Buffer Youtube Player
# Dependencies: youtube-dl

echo "$@"
VID=$(youtube-dl --get-filename "$@")

printf "Filename: %s\n" $VID
youtube-dl "$@"
fgconsole 2> /dev/null && mplayer -vo fbdev $VID || mplayer $VID

printf "Filename: %s\n" "$VID"
youtube-dl "$@"

if fgconsole > /dev/null 2>&1
  then mplayer -vo fbdev "$VID"
  else mplayer "$VID"
fi

>>>>>>> 2523791ffbd43ec47f9ee2b065f638c4cf9fc5bc
