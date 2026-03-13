import streamlit as st
import qr_functions as qr

st.title("QR Code Generator")

file_name = st.text_input("Enter file name for QR code")

########################################################
# TEXT QR

st.markdown("### Generate Text / URL QR Code")

text = st.text_input("Enter text or URL")

if st.button("Generate Text QR"):

    if text.strip() == "" or file_name.strip() == "":
        st.error("All fields are required")

    else:
        img_bytes = qr.note_qr_code(text)

        st.image(img_bytes)

        st.download_button(
            "Download QR",
            data=img_bytes,
            file_name=f"{file_name}.png",
            mime="image/png"
        )

########################################################
# UPI QR

st.markdown("### Generate UPI Payment QR")

upi_id = st.text_input("Enter UPI ID")
payer_name = st.text_input("Enter receiver name")
amount = st.text_input("Enter amount")

currency = st.selectbox(
    "Currency",
    ["INR","USD","EUR","GBP","JPY","CNY","AUD","CAD","CHF","SGD"]
)

if st.button("Generate UPI QR"):

    if upi_id.strip()=="" or payer_name.strip()=="" or amount.strip()=="" or file_name.strip()=="":
        st.error("All fields are required")

    else:
        img_bytes = qr.upi_qr_code(upi_id, payer_name, amount, currency)

        st.image(img_bytes)

        st.download_button(
            "Download QR",
            data=img_bytes,
            file_name=f"{file_name}.png",
            mime="image/png"
        )

########################################################
# PHONE QR

st.markdown("### Generate Phone Number QR")

phone = st.text_input("Enter phone number")

if st.button("Generate Phone QR"):

    if phone.strip()=="" or file_name.strip()=="":
        st.error("All fields are required")

    else:
        img_bytes = qr.phone_number_qr_code(phone)

        st.image(img_bytes)

        st.download_button(
            "Download QR",
            data=img_bytes,
            file_name=f"{file_name}.png",
            mime="image/png"
        )

########################################################
# WHATSAPP QR

st.markdown("### Generate WhatsApp QR Code")

wa_number = st.text_input("Enter WhatsApp number (country code required)")
wa_message = st.text_input("Enter message")

if st.button("Generate WhatsApp QR"):

    if wa_number.strip()=="" or wa_message.strip()=="" or file_name.strip()=="":
        st.error("All fields are required")

    else:
        img_bytes = qr.wa_qr_code(wa_number, wa_message)

        st.image(img_bytes)

        st.download_button(
            "Download QR",
            data=img_bytes,
            file_name=f"{file_name}.png",
            mime="image/png"
        )

st.markdown("---")
st.markdown(
    "<p style='text-align:center'>© Made with love and code by Shirshadip, 2026</p>",
    unsafe_allow_html=True
)