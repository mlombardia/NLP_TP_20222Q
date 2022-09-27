import pytesseract
from PIL import Image

print(pytesseract.get_languages())

img = Image.open("../20210103.webp")
img.load()
text = pytesseract.image_to_string(img, lang='spa')
print(text)
data = pytesseract.image_to_data(img)
print(data)