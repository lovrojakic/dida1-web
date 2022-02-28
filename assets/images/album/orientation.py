from PIL import Image
import PIL

popis = open("popis.txt")
data = popis.read()
popis.close()
data = data.split("\n")

fixed_width = 832

for i in data:
    if i.endswith(".jpg") or i.endswith(".JPG") or i.endswith(".jpeg"):
      from PIL import Image
      import pexif

      img = pexif.JpegFile.fromFile(i)

      try:
        #Get the orientation if it exists
        orientation = img.exif.primary.Orientation[0]
        img.exif.primary.Orientation = [1]
        img.writeFile(temp_dir + filename)

        #now rotate the image using the Python Image Library (PIL)
        img = Image.open(temp_dir + filename)
        if orientation is 6: img = img.rotate(-90)
        elif orientation is 8: img = img.rotate(90)
        elif orientation is 3: img = img.rotate(180)
        elif orientation is 2: img = img.transpose(Image.FLIP_LEFT_RIGHT)
        elif orientation is 5: img = img.rotate(-90).transpose(Image.FLIP_LEFT_RIGHT)
        elif orientation is 7: img = img.rotate(90).transpose(Image.FLIP_LEFT_RIGHT)
        elif orientation is 4: img = img.rotate(180).transpose(Image.FLIP_LEFT_RIGHT)

        #save the result
        img.save(temp_dir + filename)
      except: pass
