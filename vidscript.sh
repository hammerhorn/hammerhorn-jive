#!/bin/sh
# Frame Buffer Youtube Player
# Dependencies: youtube-dl


echo "$@"
VID=`youtube-dl --get-filename $@`
printf "Filename: %s\n" $VID
youtube-dl $@
fgconsole 2> /dev/null && mplayer -vo fbdev $VID || mplayer $VID
