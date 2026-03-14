import qrcode
from io import BytesIO


def generate_qr(data):
    img = qrcode.make(data)

    buffer = BytesIO()
    img.save(buffer, format="PNG")

    return buffer.getvalue()


def note_qr_code(data):
    return generate_qr(data)


def upi_qr_code(upi_id, name, amount="", currency="INR", note=""):

    link = f"upi://pay?pa={upi_id}&pn={name}&cu={currency}"

    if amount:
        link += f"&am={amount}"

    if note:
        link += f"&tn={note}"

    return generate_qr(link)


def phone_number_qr_code(number):
    phone = "tel:" + number
    return generate_qr(phone)


def wa_qr_code(number, text):
    link = f"https://wa.me/{number}?text={text}"
    return generate_qr(link)

def file_qr_code(data):
    pass
def wifi_qr_code(ssid, password, security):
    data = f"WIFI:T:{security};S:{ssid};P:{password};;"
    return generate_qr(data)
def email_qr_code(email, subject, message):
    data = f"mailto:{email}?subject={subject}&body={message}"
    return generate_qr(data)
def location_qr_code(latitude, longitude):
    data = f"geo:{latitude},{longitude}"
    return generate_qr(data)
def sms_qr_code(phone, message):
    data = f"SMSTO:{phone}:{message}"
    return generate_qr(data)