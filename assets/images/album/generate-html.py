import os

path = "/home/lovro/Documents/projects/postojim/assets/images/album/"
dir_list = os.listdir(path)
print(dir_list)

#for i in dir_list:
#    i = "resized-" + i + ".webp"
#    if i.endswith(".webp"):
#        print('<img src="assets/images/album/' + i + '" class="w-100 rounded mb-4" alt="slika" />')

for i in dir_list:
    if i.endswith(".jpg") or i.endswith(".jpeg") or i.endswith(".png") or i.endswith(".JPG"):
        print('<img src="assets/images/album/' + i + '" class="w-100 rounded mb-4" alt="slika" />')
