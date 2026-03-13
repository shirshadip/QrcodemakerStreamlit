import qrcode

def note_qr_code(data, file_name):
    img = qrcode.make(data)
    path = f"{file_name}.png"
    img.save(path)
    return path


def upi_qr_code(upi_id, name, amount, currency, file_name):
    upi_link = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu={currency}"
    img = qrcode.make(upi_link)
    path = f"{file_name}.png"
    img.save(path)
    return path


def phone_number_qr_code(number, file_name):
    phone = "tel:" + number
    img = qrcode.make(phone)
    path = f"{file_name}.png"
    img.save(path)
    return path
import qrcode

def wa_qr_code(data, text, file_name):
    link = f"https://wa.me/{data}?text={text}"
    img = qrcode.make(link)

    path = f"{file_name}.png"

    img.save(path)

    return path