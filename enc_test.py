import ascon

# === File paths ===
input_file = "/home/pi/images/test.jpg"
encrypted_file = "/home/pi/images/test.enc"
decrypted_file = "/home/pi/images/test_dec.txt"  # Optional check (decrypt on Pi)

# === Ascon key & nonce (must match laptop) ===
key = bytes.fromhex("00112233445566778899AABBCCDDEEFF")
nonce = bytes.fromhex("112233445566778899AABBCCDDEEFF00")
ad = b""  # associated data (can be empty)

# === Read input image ===
with open(input_file, "rb") as f:
    plaintext = f.read()

# === Encrypt ===
ciphertext = ascon.encrypt(key, nonce, ad, plaintext, variant="Ascon-128a")

# === Save encrypted file ===
with open(encrypted_file, "wb") as f:
    f.write(ciphertext)

print(f"✅ Encrypted successfully → {encrypted_file}")

# === (Optional) Decrypt locally to verify ===
plaintext_check = ascon.decrypt(key, nonce, ad, ciphertext, variant="Ascon-128a")

if plaintext_check is None:
    print("❌ Decryption test failed — mismatch or corruption.")
else:
    with open(decrypted_file, "wb") as f:
        f.write(plaintext_check)
    print(f"✅ Decryption test successful → {decrypted_file}")
