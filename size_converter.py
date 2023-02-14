from PIL import Image
import os

photos_folder = os.listdir("./Photos")
for file in photos_folder:
    basewidth = 280
    img = Image.open(f"./Photos/{file}")
    wpercent = basewidth / float(img.size[0])
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save("./Resized_Photos/{}".format(file))
