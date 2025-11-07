import qrcode
from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(version=2,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=20,border=4)
qr.add_data("https://alqurankarim.net/ur/surah-al-fatiha/ayat-0/translation/tafsir")
qr.make(fit=True)
img = qr.make_image(fill_color="black",back_color="white")
img.save("Translation_of_Quran.png")