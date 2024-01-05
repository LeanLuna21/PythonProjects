import qrcode

web_link = input ('Introduce el link aqui: ')

# The version parameter is an integer from 1 to 40 that controls the size of the QR code.
# The box_size parameter controls how many pixels each “box” of the QR code is.
# The border parameter controls how many boxes thick the border should be.
qr = qrcode.QRCode(version=1,box_size=5,border=5) 

qr.add_data(web_link)
qr.make()

# fill_color = line colour
img = qr.make_image(fill_color = 'black', back_color = 'white')
img.save(input('Introduce nombre del archivo (con la extensión ".png"): '))

# ademas se puede automatizar para poder hacer mas de un cod en cada ejecucion
# tambien puede darsele la chance al usuario que modifique la version o el tamaño
