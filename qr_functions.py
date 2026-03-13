import qrcode
def note_qr_code(data,file_name):
    txt = qrcode.make(data)
    save=file_name+".png"
    txt.save(save)
    return txt
def link_qr_code(data,file_name):
    link = qrcode.make(data)
    link.save(file_name)
    return link
def whatsapp_qr_code(data,text,file_name):
    link=link= f"https://wa.me/{data}?text={text}"
    whatsapp = qrcode.make(data)
    whatsapp.save(file_name)
    return whatsapp
def upi_qr_code(upi_id,name,amount,currency):
    #upi link 
    upi_link = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu={currency}"
    qr = qrcode.make(upi_link)
    return qr
def phone_number_qr_code(data,file_name):
    phone = "tel:" + data
    qr = qrcode.make(phone)
    qr.save(file_name)
    return qr