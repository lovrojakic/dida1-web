popis = open("popis.txt")
data = popis.read()
popis.close()
data = data.split("\n")

for i in data:
    i = "resized-" + i + ".webp"
    if i.endswith(".webp"):
        print('<img src="assets/images/album/' + i + '" class="w-100 rounded mb-4" alt="slika" />')
