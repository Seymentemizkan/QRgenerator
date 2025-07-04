import qrcode
from PIL import Image
url = input("Lutfen url giriniz !")
# code = qrcode.make("https://github.com")
code = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,

)

code.add_data("{}".format(url))

code.make(fit=True)

image = code.make_image(fill_color ="black",bac_color="white")

image.show()

