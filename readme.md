# 📱 QR code maker streamlit

A versatile QR code generator built with Python and Streamlit — supporting UPI payments, contacts, Wi-Fi, WhatsApp, email, SMS, location, and more.

---
> Link: streamlit app: https://qrcodemakeronline.streamlit.app/
> Windows App(doc): https://qrcodemaker-opal.vercel.app 

## ✨ Features

| Type | Description |
|------|-------------|
| 📝 **Note / Text** | Encode any plain text or URL into a QR code |
| 💸 **UPI Payment** | Generate payment QR codes compatible with PhonePe, GPay, Paytm, etc. |
| 📞 **Phone Number** | Dial-ready QR codes using the `tel:` protocol |
| 💬 **WhatsApp** | Pre-filled WhatsApp message links |
| 📶 **Wi-Fi** | One-scan Wi-Fi joining (supports WPA, WEP, and open networks) |
| 📧 **Email** | Pre-composed email with subject and body |
| 🗺️ **Location** | Geo-coordinates for maps navigation |
| 💬 **SMS** | Pre-filled SMS message to a phone number |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/qr-forge.git
cd qr-forge

# Install dependencies
pip install -r requirements.txt
```

### Running the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## 📦 Dependencies

```txt
streamlit
qrcode[pil]
Pillow
```

Install them all at once:

```bash
pip install streamlit "qrcode[pil]" Pillow
```

---

## 🧩 Module Reference

All core QR generation logic lives in `qr_functions.py`.

### `generate_qr(data: str) -> bytes`
Base function. Encodes any string into a PNG QR code and returns it as raw bytes.

---

### `note_qr_code(data: str) -> bytes`
Encodes plain text or a URL.

```python
note_qr_code("https://example.com")
```

---

### `upi_qr_code(upi_id, name, amount="", currency="INR", note="") -> bytes`
Generates a UPI deep-link QR code.

```python
upi_qr_code("user@upi", "John Doe", amount="199", note="Invoice #42")
```

Produces: `upi://pay?pa=user@upi&pn=John Doe&cu=INR&am=199&tn=Invoice #42`

---

### `phone_number_qr_code(number: str) -> bytes`
Generates a `tel:` QR code to trigger a phone call.

```python
phone_number_qr_code("+919876543210")
```

---

### `wa_qr_code(number: str, text: str) -> bytes`
Generates a WhatsApp click-to-chat link with a pre-filled message.

```python
wa_qr_code("919876543210", "Hello! I saw your listing.")
```

> **Note:** The number must include the country code without `+` (e.g., `919876543210` for India).

---

### `wifi_qr_code(ssid: str, password: str, security: str) -> bytes`
Generates a Wi-Fi join QR code.

```python
wifi_qr_code("MyNetwork", "s3cr3tP@ss", "WPA")
```

`security` options: `WPA`, `WEP`, or `nopass`

---

### `email_qr_code(email: str, subject: str, message: str) -> bytes`
Generates a `mailto:` QR code with a pre-composed email.

```python
email_qr_code("hello@example.com", "Meeting Request", "Hi, are you free on Friday?")
```

---

### `location_qr_code(latitude: float, longitude: float) -> bytes`
Generates a `geo:` QR code that opens in a maps application.

```python
location_qr_code(28.6139, 77.2090)  # New Delhi
```

---

### `sms_qr_code(phone: str, message: str) -> bytes`
Generates an `SMSTO:` QR code with a pre-filled message.

```python
sms_qr_code("+919876543210", "Your OTP is 482910")
```

---

## 🗂️ Project Structure

```
qr-forge/
├── main.py              # Streamlit UI
├── qr_utils.py         # QR generation logic
├── requirements.txt    # Python dependencies
├── README.md           #project overview and documentation
├── CONTRIBUTING.md     # guidelines for contributing
├── LICENSE             # MIT License text
```

---

## 🛣️ Roadmap

- [ ] File/vCard QR code support (`file_qr_code`)
- [ ] Custom QR code colors and logo embedding
- [ ] Batch QR code generation (CSV upload)
- [ ] Download as SVG in addition to PNG
- [ ] QR code history / session storage

---

## 🤝 Contributing

Contributions are welcome! Please open an issue first to discuss what you'd like to change, then submit a pull request.

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---
## Troubleshooting
1. **QR code not scanning?** Make sure the input data is valid and follows the expected format for that QR type. For example, UPI IDs should be in the format `user@bank`, and phone numbers should include the country code without `+`.
2. **Streamlit app not loading?** Check your internet connection and ensure all dependencies are installed. Try running `streamlit run app.py` from the terminal to see any error messages.

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.