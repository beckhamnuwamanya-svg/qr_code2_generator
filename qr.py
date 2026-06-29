import qrcode
data ="""BEGIN:VCARD
VERSION:3.0
FN:Nuwamanya Beckham
TEL:+256780168329
EMAIL:beckhamnuwamanya@gmail.com
END:VCARD"""
#create qr  code
img =qrcode.make(data)
#save image
img.save("my_contact_qr.png")
print("qrcode created successfully!")