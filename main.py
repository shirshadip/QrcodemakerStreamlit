import streamlit as st
import qr_functions as qr
from io import BytesIO

st.title("QR Code Generator")
st.header("Generate a text QR Code")

text = st.text_input("Enter text or URL")
name= st.text_input("Enter a name of the qr code here",)

if st.button("Generate QR Code"):

    if not name:
        st.error("name is required")
    txt_qr= qr.note_qr_code(text,name)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")

    st.image(buffer.getvalue(), caption="Generated QR Code")

    st.download_button(
        label="Download QR Code",
        data=buffer.getvalue(),
        file_name="txt.png",
        mime="image/png"
    )