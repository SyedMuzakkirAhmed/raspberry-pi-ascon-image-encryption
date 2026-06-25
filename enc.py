import ascon, os

# -------------------------
# FILE PATHS
# -------------------------
input_file = "/home/pi/images/test.jpg"
encrypted_file = "/home/pi/images/test.enc"
decrypted_file = "/home/pi/images/test_dec.jpg"

# -------------------------
# Key & Nonce
# -------------------------
key = os.urandom(16)    # 128-bit key
nonce = os.urandom(16)  # 128-bit nonce
chunk_size = 1024 * 64  # 64 KB per chunk

# -------------------------
# Encrypt
# -------------------------
with open(input_file, "rb") as f_in, open(encrypted_file, "wb") as f_out:
    while chunk := f_in.read(chunk_size):
        ciphertext = ascon.encrypt(key, nonce, b'', chunk)
        f_out.write(ciphertext)

print(f"Encrypted file: {encrypted_file}")

# -------------------------
# Decrypt
# -------------------------
with open(encrypted_file, "rb") as f_in, open(decrypted_file, "wb") as f_out:
    while chunk := f_in.read(chunk_size + 16):  # ciphertext slightly larger than plaintext
        plaintext = ascon.decrypt(key, nonce, b'', chunk)
        f_out.write(plaintext)

print(f"Decrypted file: {decrypted_file}")
