from pyzbar.pyzbar import decode
from PIL import Image

name = input("which QR code would you like to decode(add .png at the end of the filename: \n")
d = decode(Image.open(name))
print(d[0].data.decode())
