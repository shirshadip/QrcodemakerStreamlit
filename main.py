import streamlit as st
import qr_functions as qr

st.title("QR Code Generator")

name = st.text_input("Enter a name of the qr code here you want generate")

########################################################
# Plain text QR code

st.markdown("<h3>Generate a text QR Code</h3>", unsafe_allow_html=True)

text = st.text_input("Enter text or URL")

if st.button("generate a plain text qrcode"):

    if text.strip() == "" or name.strip() == "":
        st.error("All fields are required")
        
    else:

        txt = qr.note_qr_code(text, name)

        showimg = name + ".png"

        st.image(showimg)

        with open(showimg, "rb") as file:
            st.download_button(
                label="Download File",
                data=file,
                file_name=f"{name}.png",
                mime="image/png"
            )

########################################################
# UPI QR code

st.markdown("<h3>Generate a UPI payment QR Code</h3>", unsafe_allow_html=True)

upi_id = st.text_input("Enter the UPI ID")
payer_name = st.text_input("Enter the name")
amount = st.text_input("Enter the amount you want to pay")

currency = st.selectbox("Select the currency",[
    "INR","USD","EUR","GBP","JPY","CNY","AUD","CAD",
    "CHF","SGD","NZD","KRW","BRL","ZAR","RUB"
])

if st.button("generate a UPI Payment qr code"):

    if upi_id.strip()=="" or payer_name.strip()=="" or amount.strip()=="" or name.strip()=="":
        st.error("All fields are required")
       
     
    else :
        
        txt = qr.upi_qr_code(upi_id, payer_name, amount, currency)

        showimg = payer_name + ".png"

        st.image(showimg)

        with open(showimg, "rb") as file:
            st.download_button(
                label="Download File",
                data=file,
                file_name=f"{payer_name}.png",
                mime="image/png"
            )