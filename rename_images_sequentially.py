import os
_src = "./"
_ext = ".jpeg"
_ext2= ".jpg"
i=1
for i,filename in enumerate(os.listdir(_src)):
	if filename.endswith(_ext):
		os.rename(filename, _src+'image' + str(i).zfill(1)+_ext2)
	elif filename.endswith(_ext2):
		os.rename(filename, _src+'image' + str(i).zfill(1)+_ext2)
