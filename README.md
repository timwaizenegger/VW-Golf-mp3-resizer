# VW-Golf-mp3-resizer
This repo contains a python program that resizes the cover art JPEG image inside the ID3 tag of MP3 files down to 400x400 pixels. This is necessary in order to see the cover art in VW (Golf) cars multi media systems. This is in 2016, maybe newer VW models support higer resolutions.


Usually MP3 files use high-res cover art; well not really it's mostly 640x640 or something like that... 
but that doesn't show up on the VW multi media system! I would have never guessed that if it wasn't for Haydn Williams post (http://www.haydnwilliams.com/blog/vw-golf-mk7-sd-cards-and-album-art)
I think VW uses some old-school proprietary hardware for their multimedia stuff; which they're locked into with their custom OS/software...


So you need to limit the cover art size to 400x400 pixel when you play MP3s from USB or SD card.


# Usage
the program is very short and low-tech. It walks over the "*.mp3" files in one directory. Set the directory directly in the program.


# Limitations
it's not very clever; just resizes the "APIC:Cover" thing to 400x400. So if the source wasn't quadratic in size, it will be distorted. It also doesn't exit if the source is smaller... Everything will be 400x400!


# Dependencies
mutagen, PIL

# Python
uses version 3 (I didn't test it on python2.7)


# Example
No cover art because jpeg is too large: ![too large](/doc/DSC_0003.jpg "no cover art")
cover art visible; it's 400x400 pixels now: ![just right](/doc/DSC_0004.jpg "cover art visible")
