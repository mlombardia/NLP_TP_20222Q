from datetime import date, timedelta
from os import listdir

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


custom_config = r'--oem 3'
a = ""

start_date = date(2002, 8, 28)
end_date = date(2022, 8, 28)

# for file in listdir("c:/data/tapas/"):
for sd in daterange(start_date, end_date):
    file = sd.strftime("%Y") + sd.strftime("%m") + sd.strftime("%d") + ".jpg"
    img = cv2.imread("~/data/" + file)
    try:
        nuevo = pytesseract.image_to_string(img, config=custom_config).replace("\n", " ").replace(";", ",").replace("- ","")
        a = a + ";" + file + ";" + nuevo + "\n"
        print(file)
    except:
        print("No se pudo obtener: " + file)

with open('~/data/Corpus Clarin.csv', 'w', newline="\n") as f:
    f.write(a)
f.close()
