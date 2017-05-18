import math
import PIL.Image as Image
import os

ls = os.listdir('./image')
each_size = 640*640
lines = 18
image = Image.new('RGBA', (640*lines, 640*lines))
x = 0
y = 0
for i in range(0,len(ls)+1):
    try:
        img = Image.open('./image' + "/" + str(i) + ".jpg")
    except IOError:
        print("Error")
    else:
        img = img.resize((each_size, each_size), Image.ANTIALIAS)
        image.paste(img, (x * each_size, y * each_size))
        x += 1
        if x == lines:
            x = 0
            y += 1
image.save('.' + "/" + "all.jpg")
