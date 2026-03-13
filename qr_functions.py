import qrcode
def note_qr_code(data,name):
    txt = qrcode.make(data)
    txt.save(name)
    return txt
def link_qr_code(data,name):
    link = qrcode.make(data)
    link.save(name)
    return link
def whatsapp_qr_code(data,name):
    whatsapp = qrcode.make(data)
    whatsapp.save(name)
    return whatsapp