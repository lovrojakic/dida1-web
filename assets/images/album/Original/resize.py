from PIL import Image
import PIL, os

path = "/home/lovro/Documents/projects/postojim/assets/images/album/Original/"
dir_list = os.listdir(path)
print(dir_list)

fixed_width = 416

for i in dir_list:
    if i.endswith(".jpg") or i.endswith(".JPG") or i.endswith(".jpeg"):
        image = Image.open(i)
        width_percent = (fixed_width / float(image.size[0]))
        height_size = int((float(image.size[1]) * float(width_percent)))
        image = image.resize((fixed_width, height_size), Image.ANTIALIAS)
        quality_val = 100
        image.save("resized-" + i, 'JPEG', quality=quality_val)

