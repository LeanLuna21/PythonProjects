import qrcode

web_link = 'https://www.youtube.com/watch?v=z6uayny9QN0&ab_channel=V%C3%ADdeosIlVolo-EncontrosVirtuais'

# The version parameter is an integer from 1 to 40 that controls the size of the QR code.
# The box_size parameter controls how many pixels each “box” of the QR code is.
# The border parameter controls how many boxes thick the border should be.
qr = qrcode.QRCode(version=1,box_size=5,border=5) 

qr.add_data(web_link)
qr.make()

# fill_color = line colour
img = qr.make_image(fill_color = 'black', back_color = 'white')
img.save('YT_il_volo_qr.png')