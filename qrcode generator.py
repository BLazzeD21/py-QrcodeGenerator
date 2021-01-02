import qrcode
img_qrcode = "qr.png"


link = input('Enter the link: ')

def generate(data=link, img_qrcode="qr.png"):
    img = qrcode.make(data) 
    img.save(img_qrcode)
    return img


generate()
