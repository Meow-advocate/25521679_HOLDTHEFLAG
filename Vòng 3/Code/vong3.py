import base64

cipher_text = "SU9ESntXVURRX1lEUV9TS1hSUUp9"

# Bước 1: Decode lớp ngoài bằng Base64
decoded = base64.b64decode(cipher_text).decode()
print("Sau khi decode Base64:", decoded)

# Bước 2: Giải Caesar Cipher
def caesar_decrypt(text, shift):
    result = ""

    for ch in text:
        if "A" <= ch <= "Z":
            # Dịch chữ cái lùi shift ký tự
            new_char = chr((ord(ch) - ord("A") - shift) % 26 + ord("A"))
            result += new_char
        else:
            # Giữ nguyên các ký tự như {, }, _
            result += ch

    return result

flag = caesar_decrypt(decoded, 3)

print("FLAG:", flag)
