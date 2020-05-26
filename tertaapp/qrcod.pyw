import qrcode
import sys
data='https://tetrapack.herokuapp.com/datadisplay1/'+sys.argv[1]
sav='media/'+sys.argv[1]+'.png'
#x="01"
qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(sav)
print("check media")
