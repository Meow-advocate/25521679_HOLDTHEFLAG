def xor_decrypt(hex_ciphertext, key):
    # Bước 1: Chuyển chuỗi hex thành mảng các byte
    cipher_bytes = bytes.fromhex(hex_ciphertext)
    
    # Bước 2: Chuyển khóa (key) thành mảng các byte
    key_bytes = key.encode('utf-8')
    
    decrypted_bytes = bytearray()
    
    # Bước 3: Duyệt qua từng byte của bản mã và XOR với từng byte của khóa
    for i in range(len(cipher_bytes)):
        # Dùng phép chia lấy dư (%) để lặp lại khóa khi bản mã dài hơn khóa
        decrypted_byte = cipher_bytes[i] ^ key_bytes[i % len(key_bytes)]
        decrypted_bytes.append(decrypted_byte)
    
    # Bước 4: Chuyển mảng byte kết quả thành chuỗi văn bản (bỏ qua các ký tự lỗi nếu có)
    return decrypted_bytes.decode('utf-8', errors='ignore')

# Dữ liệu từ đề bài
hex_data = "0b19636f651d08737e6b1c197f757a0f0e7a79710616"
secret_key = "HQ604"

flag = xor_decrypt(hex_data, secret_key)
print(f"Kết quả giải mã: {flag}")
