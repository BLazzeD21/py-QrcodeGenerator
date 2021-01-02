import qrcode

link = input('Enter the link: ')
name = input('Enter the name of qrcode: ')
name += ".jpg"

def generate(data=link, img_qrcode=name):
    img = qrcode.make(data) 
    img.save(img_qrcode)
    return img

generate()
