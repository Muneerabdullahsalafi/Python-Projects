import qrcode
import image
qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5
)
data = "https://farhan-ur-rahman.github.io/02%20Areas/DEVOPS.html"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black", back_color = "white")
img.save("test.png")