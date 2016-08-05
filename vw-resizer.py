""" 
	MP3/ID3 cover art resizer for VM Golf Multimedia system (but really general purpose...)
	
	Copyright (C) <2016> <Tim Waizenegger>
	
	This software may be modified and distributed under the terms
	of the MIT license.  See the LICENSE file for details.
"""


import mutagen
import io
import os
from io import BytesIO
from mutagen.id3 import ID3, APIC
import PIL
from PIL import Image



"""
	Set the directory to process here
	don't use tailing "/"
		/tmp/1/   NO :(
		/tmp/1    YAY :)
		
	
	further documentation omitted since the code is so simple
"""
DIRECTORY = "/tmp/1"



def walk_dir_and_do_it(path):
	for this_path in os.listdir(path):
		if this_path.endswith(".mp3"):
			try:
				resize_coverart_on_file(path + "/" + this_path)
			except Exception as e:
				print("meh... {}".format(e))



def resize_coverart_on_file(filename):
	print("working on {}".format(filename))
	f = mutagen.File(filename, easy=False)
	d = f.tags["APIC:Cover"]

	#i = open("/tmp/bla.jpg","wb")
	#i.write(d.data)
	#i.close()

	im = Image.open(io.BytesIO(d.data))
	print("   size was {}".format(im.size))
	im_new = im.resize((400,400))
	print("   size is now {}".format(im_new.size))

	o = BytesIO()
	im_new.save(o, format="jpeg")
	o.seek(0)


	f.tags.add(
					APIC(
						encoding=3, # 3 is for utf-8
						mime='image/jpeg', # image/jpeg or image/png
						type=3, # 3 is for the cover image
						desc=u'Cover',
						data=o.read()
					)
				)
	f.save()


if __name__ == "__main__":
	walk_dir_and_do_it(DIRECTORY)
