#After installing the qrcode with pip, import qr code
import qrcode

#A qrcode for my github profilr was created 
img = qrcode.make("https://github.com/komaConnect")
img.save("mygithub.png")

#install Pillow using pip, import Image with PIL 
from PIL import Image
# the png qr code converted to jpg 
img_png = Image.open("mygithub.png")
img_jpg = img_png.convert("RGB")
img_jpg.save("mygithub.jpg")

#converting the png file to pdf
img_pdf = img_png.convert("RGB")
img_pdf.save("mygithub.pdf")