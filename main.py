import qrcode
from PIL import Image

print("Please press 'q' to close !!! ")
while True:
    url = input("Lutfen url giriniz !")
    if url == "q":
        break
    else:
        # code = qrcode.make("https://github.com") # manuel entrance
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

