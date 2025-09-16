# 📌 QR Code Generator (Python)

This project is a simple **Python-based QR code generator** that allows you to create customized QR codes with **rectangular or circular modules** and **custom colors**.

---

## ✨ Features
- 🔗 Generate QR codes for any **link or text**.  
- ⚪ Choose between **rectangular** (default) or **circular/rounded** pixels.  
- 🎨 Customize **foreground (fill)** and **background** colors (supports color names and hex codes).  
- 📏 Adjust **QR version**, **box size**, and **border size**.  
- 💾 Save the QR code in **PNG**, **JPEG**, or **JPG** formats.  

---

## 📦 Requirements
Make sure you have **Python 3.7+** installed. Install the required libraries:

```bash
pip install qrcode[pil]
pip install pillow
```

## ▶️ How It Works

Run the script:
```bash
 python qr_code.py
```
### You will be prompted to enter:
    1. Your desired link/text
    2. QR version, box size, and border size
    3. Pixel style → circle or rectangle
    4. Foreground and background colors (supports names like red, blue, or hex codes like #FF5733)
    5. Output filename (e.g., myqr.png)

The generated QR code will be saved in:
```swift
  your filepath edited in line 64
```

### 💡 Example
```text
      Enter your desired link:: https://www.github.com
      Enter version:: 1
      Enter box size:: 10
      Enter border size:: 4
      Do you want circle or rectangle shaped pixels?? circle
      Enter the fill color(can provide hexcodes also):: #FF0000
      Enter the back color(can provide hexcodes also):: white
      Enter the name of the downloaded file along with its extension(.png or .jpeg or .jpg):: github_qr.png
```

# ✔️ This will generate a red circular QR code on a white background, saved as github_qr.png.

### 📌 Notes

Version → Determines QR complexity (higher = more data capacity).
Box size → Controls pixel size.
Border → Ensures enough quiet space around the QR (minimum 4 recommended).
Colors are converted using Pillow’s ImageColor.getrgb(), so both hex codes and color names are supported.
