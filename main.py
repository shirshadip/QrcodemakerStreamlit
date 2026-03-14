import streamlit as st
import qr_functions as qr
import base64
st.markdown("""
<style>
.stButton button{
    background-color:#0066ff;
    color:white;
    border-radius:15px;
}
</style>
""", unsafe_allow_html=True)

st.title("QR Code Generator")

file_name = st.text_input("Enter file name for QR code")
tab1, tab2, tab3, tab4 , tab5, tab6,tab7 ,tab8= st.tabs([
    "Text QR",
    "UPI QR",
    "Phone QR",
    "WhatsApp QR",
    "Wifi QR ",
    "Email QR",
    "Location QR",
    "SMS QR"
])
########################################################
# TEXT QR
with tab1:
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

with tab2:

    st.markdown("### Generate UPI Payment QR")

    upi_id = st.text_input("Enter UPI ID")
    payer_name = st.text_input("Enter receiver name")
    amount = st.text_input("Enter amount")
    note = st.text_area("Enter a note (optional)")

    currency = st.selectbox(
        "Currency",
        ["INR","USD","EUR","GBP","JPY","CNY","AUD","CAD","CHF","SGD"]
    )

    if st.button("Generate UPI QR"):

        if upi_id.strip()=="" or payer_name.strip()=="" or amount.strip()=="" or file_name.strip()=="":
            st.error("All required fields must be filled")

        else:

            # If note is empty, make it blank
            note_value = note.strip() if note.strip() else ""

            img_bytes = qr.upi_qr_code(
                upi_id,
                payer_name,
                amount,
                currency,
                note_value
            )

            st.image(img_bytes)

            st.download_button(
                "Download QR",
                data=img_bytes,
                file_name=f"{file_name}.png",
                mime="image/png"
            )
########################################################
# PHONE QR
with tab3:
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
with tab4:
    st.markdown("### Generate WhatsApp QR Code")

    wa_number = st.text_input("Enter WhatsApp number (country code required)")
    wa_message = st.text_area("Enter message")

    if st.button("Generate WhatsApp QR"):

        if wa_number.strip()==""  or file_name.strip()=="":
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
            
######################################################################3
# wifi qr code maker 
with tab5:
    
    st.markdown("### Generate WiFi QR Code")

    ssid = st.text_input("WiFi Name (SSID)")
    password = st.text_input("WiFi Password")
    security = st.selectbox("Security Type", ["WPA", "WEP", "nopass"])

    if st.button("Generate WiFi QR"):

        if ssid.strip()=="":
            st.error("WiFi name is required")

        else:
            img_bytes = qr.wifi_qr_code(ssid, password, security)

            st.image(img_bytes)

            st.download_button(
                "Download QR",
                img_bytes,
                file_name=f"{file_name}.png",
                mime="image/png"
            )
################################################33
# Email qr 
with tab6:
    st.markdown("### Generate Email QR Code")

    email = st.text_input("Email address")
    subject = st.text_input("Email subject")
    message = st.text_area("Email message")

    if st.button("Generate Email QR"):

        if email.strip()=="":
            st.error("Email required")

        else:
            img_bytes = qr.email_qr_code(email, subject, message)

            st.image(img_bytes)

            st.download_button(
                "Download QR",
                img_bytes,
                file_name=f"{file_name}.png",
                mime="image/png"
            )
#####################################################################
# Location QR code 
with tab7:
    st.markdown("### Generate Location QR Code")

    lat = st.text_input("Latitude")
    lon = st.text_input("Longitude")

    if st.button("Generate Location QR"):

        if lat.strip()=="" or lon.strip()=="":
            st.error("Coordinates required")

        else:
            img_bytes = qr.location_qr_code(lat, lon)

            st.image(img_bytes)

            st.download_button(
                "Download QR",
                img_bytes,
                file_name=f"{file_name}.png",
                mime="image/png"
            )
##############################################################
# SMS QR
with tab8:
    st.markdown("### Generate SMS QR Code")

    sms_number = st.text_input("Phone number")
    sms_message = st.text_area("Message")

    if st.button("Generate SMS QR"):

        if sms_number.strip()=="":
            st.error("Phone number required")

        else:
            img_bytes = qr.sms_qr_code(sms_number, sms_message)

            st.image(img_bytes)

            st.download_button(
                "Download QR",
                img_bytes,
                file_name=f"{file_name}.png",
                mime="image/png"
            )

st.markdown("---")
st.markdown(
    "<p style='text-align:center'>© Made with love and code by Shirshadip, 2026</p>",
    unsafe_allow_html=True
)