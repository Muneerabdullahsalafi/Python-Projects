# install the qrcode & image module to run this Code
# Command = pip install qrcode && pip install image

import qrcode
import image
qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5
)
data = "https://www.youtube.com/@muneerabdullahsalafi4788"
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black", back_color = "white")
img.save("test.png")