import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO
from pyzbar.pyzbar import decode


st.markdown("<h1 style='color: rgb(90, 5, 62)'>🔲QR Code Encoder </h1>", unsafe_allow_html=True)

if 'data' not in st.session_state:
    st.session_state.data = ''

st.session_state.data = st.text_input('Enter the data to encode', st.session_state.data)

if st.button('Generate QR Code'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=7,
        border=1
    )

    qr.add_data(st.session_state.data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    # Save the QR code image to a BytesIO object
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    st.image(buffer, caption='QR Code', width=200)

    #  download button
    st.download_button(
        label="Download QR Code",
        data=buffer,
        file_name="qr_code.png",
        mime="image/png"
    )

if st.button("Reset"):
    st.session_state.data = ''

# QR code decoder

st.markdown("<h1 style='color: rgb(90, 5, 62)'>🔎QR Code Decoder </h1>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload a QR Code image", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded QR Code', width=200)
    
    decoded_data = decode(image)
    if decoded_data:
        st.write("Decoded Data: ", decoded_data[0].data.decode('utf-8'))
    else:
        st.write("No QR code found in the image.")