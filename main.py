from datetime import date, timedelta

import pytesseract
from PIL import Image


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

print(pytesseract.get_languages())
a = ""

start_year = int(input("Start: "))
end_year = int(input("End: "))

start_date = date(start_year, 8, 28)
end_date = date(end_year, 8, 28)

for sd in daterange(start_date, end_date):
  file = sd.strftime("%Y") + sd.strftime("%m") + sd.strftime("%d") + ".jpg"
  try:
    img = Image.open("../../Documents/data/" + file)
    img.load()
    text = pytesseract.image_to_string(img, lang='spa').replace("\n", " ").replace(";", ",").replace("- ","")
    a = a + ";" + file + ";" + text + "\n"
    print(file)
  except:
    print("No se pudo obtener: " + file)

path_csv = "../../Documents/data/" + str(start_year) + "-" + str(end_year) + ".csv"
with open(path_csv, 'w', newline="\n") as f:
    f.write(a)
f.close()
