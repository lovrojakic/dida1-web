from PIL import ImageOps, Image
import piexif, os

path = "D:\\Projects\\postojim\\assets\\images\\album\\Original\\"
dir_list = os.listdir(path)
print(dir_list)

for i in dir_list:
    if i.endswith(".jpg") or i.endswith(".JPG") or i.endswith(".jpeg"):
        filename = i
        image = Image.open(path+filename)
        if (image._getexif()):
            print(i)
            image = ImageOps.exif_transpose(image)
            image.save(path + filename)
            image.close()
