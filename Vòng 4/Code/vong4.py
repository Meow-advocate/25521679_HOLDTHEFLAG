from pathlib import Path

# Đọc ciphertext dạng hex từ file output.txt
cipher_hex = Path("output.txt").read_text().strip()
ciphertext = bytes.fromhex(cipher_hex)

# PNG header chuẩn 16 byte đầu
png_header = b"\x89PNG\r\n\x1a\n" + (13).to_bytes(4, "big") + b"IHDR"

# Do keystream 16 byte bị lặp lại,
# ta khôi phục keystream bằng cách XOR ciphertext đầu với PNG header
keystream = bytes(c ^ p for c, p in zip(ciphertext[:16], png_header))

# Giải mã toàn bộ ciphertext
plaintext = bytearray()

for i in range(0, len(ciphertext), 16):
    block = ciphertext[i:i+16]
    decrypted_block = bytes(c ^ k for c, k in zip(block, keystream))
    plaintext.extend(decrypted_block)

# Ghi ảnh đã giải mã ra file
Path("decrypted_flag.png").write_bytes(plaintext)

