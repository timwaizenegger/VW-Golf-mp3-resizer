# VW-Golf-mp3-resizer
This repo contains a python program that resizes the cover art JPEG image inside the ID3 tag of MP3 files down to 400x400 pixels. This is necessary in order to see the cover art in VW (Golf) cars multi media systems.


Usually MP3 files use high-res cover art; well not really it's mostly 640x640 or something like that... 
but that's too much for VWs computers! I would have never guessed that if it wasn't for Haydn Williams post (http://www.haydnwilliams.com/blog/vw-golf-mk7-sd-cards-and-album-art)
I think VW uses some old-school proprietary hardware for their multimedia stuff; which they're locked into with their custom OS/software... or they just have bad programmers; who knows.


So you need to limit the cover art size to 400x400 pixel when you play MP3s from USB or SD card.


# Usage
the program is very short and low-tech. It walks over the "*.mp3" files in one directory. Set the directory directly in the program.


# Dependencies
mutagen, PIL

# Python
uses version 3 (I didn't test it on python2.7)

