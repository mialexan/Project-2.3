#Imports Image and ImageFilter from PIL
from PIL import Image, ImageFilter
import sys

#Attempts to find specified picture
try:
	img = Image.open("ProjPic.jpg")

#Displays error message and exits program if the image is not found
except IOError:
	print("Unable to load image")
	sys.exit(1)

#Command to blur the specified image
blurred = img.filter(ImageFilter.BLUR)

#Saves the newly altered image to on your disk
blurred.save("blurredProjPic.jpg")