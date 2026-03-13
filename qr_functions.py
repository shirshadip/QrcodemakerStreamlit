import qrcode
from io import BytesIO


def generate_qr(data):
    img = qrcode.make(data)

    buffer = BytesIO()
    img.save(buffer, format="PNG")

    return buffer.getvalue()


def note_qr_code(data):
    return generate_qr(data)


def upi_qr_code(upi_id, name, amount, currency):
    upi_link = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu={currency}"
    return generate_qr(upi_link)


def phone_number_qr_code(number):
    phone = "tel:" + number
    return generate_qr(phone)


def wa_qr_code(number, text):
    link = f"https://wa.me/{number}?text={text}"
    return generate_qr(link)