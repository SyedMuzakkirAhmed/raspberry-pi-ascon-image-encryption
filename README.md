# Image File Encryption and Decryption Using Ascon Cipher on Raspberry Pi

## Overview

This project implements secure image file encryption and decryption using the Ascon-128a lightweight cryptographic algorithm on a Raspberry Pi. The system protects image data during transmission by encrypting the image into unreadable ciphertext and restoring it at the receiver using authenticated decryption.

Ascon is the winner of the NIST Lightweight Cryptography Standardization Process and is designed for secure communication in embedded and IoT systems.

## Features

- Image file encryption using Ascon-128a
- Secure image transmission over a network
- Authenticated decryption and integrity verification
- Raspberry Pi implementation
- Lightweight cryptography suitable for embedded systems
- Secure file transfer between connected devices

## Hardware Requirements

- Raspberry Pi 3 / Raspberry Pi 4
- MicroSD Card
- Power Supply
- Laptop A (Sender)
- Laptop B (Receiver)
- Wi-Fi or Ethernet Network

## Software Requirements

- Raspberry Pi OS
- Python 3
- Ascon Cryptography Library
- Socket Programming Libraries

## Hardware Configuration

```text
Laptop A (Sender)
        │
        ▼
  Raspberry Pi
(Encryption/Decryption)
        │
        ▼
Laptop B (Receiver)
```

All devices must be connected to the same Wi-Fi or LAN network for successful communication and file transfer.

## Project Files

```text
enc.py       - Encrypts image files using Ascon-128a
enc_test.py  - Decrypts encrypted image files
send.py      - Transfers files between systems
test.jpg     - Sample image file
test.enc     - Encrypted image output
```

## System Architecture

https://drive.google.com/file/d/1qV4Bef0KVAn2HymFPFSk8O5PK99oKmjA/view?usp=sharing

## How to Run

### Step 1: Connect Devices

Connect the following devices to the same network:

- Raspberry Pi
- Laptop A (Sender)
- Laptop B (Receiver)

Check the Raspberry Pi IP address:

```bash
hostname -I
```

Verify connectivity from both laptops:

```bash
ping <Raspberry_Pi_IP>
```

### Step 2: Transfer Image to Raspberry Pi

Place the image file (`test.jpg`) in the project directory and transfer it to the Raspberry Pi if required.

### Step 3: Encrypt the Image

Run the encryption script on the Raspberry Pi:

```bash
python3 enc.py
```

Output:

```text
test.jpg → test.enc
```

The image is encrypted using the Ascon-128a lightweight cryptographic algorithm and stored as `test.enc`.

### Step 4: Transfer Encrypted File

Transfer the encrypted file using:

```bash
python send.py
```

The encrypted file is transmitted over the network to the receiver system.

### Step 5: Decrypt the Image

Run the decryption script:

```bash
python3 enc_test.py
```

Output:

```text
test.enc → recovered_image.jpg
```

The encrypted image is decrypted and restored to its original form.

### Step 6: Verify Results

Compare:

```text
Original Image   : test.jpg
Encrypted File   : test.enc
Decrypted Image  : recovered_image.jpg
```

Successful decryption confirms data confidentiality, integrity, and authenticity.

## Workflow

1. Select image file (`test.jpg`).
2. Transfer image to Raspberry Pi.
3. Encrypt image using Ascon-128a.
4. Generate encrypted file (`test.enc`).
5. Transmit encrypted file through the network.
6. Receive encrypted file at destination.
7. Decrypt using Ascon-128a.
8. Recover the original image.
9. Verify image integrity.

## Applications

- Secure image transmission
- IoT security systems
- Embedded cybersecurity
- Secure cloud storage
- Industrial communication systems
- Medical image protection

## Technologies Used

- Raspberry Pi
- Python 3
- Ascon-128a
- Lightweight Cryptography
- Socket Programming
- Network Communication
- Cybersecurity

## Future Enhancements

- Real-time image streaming encryption
- Video encryption and decryption
- Secure wireless communication
- Graphical User Interface (GUI)
- Public-key based secure key exchange

## Author

Syed Muzakkir Ahmed

B.Tech Electronics and Communication Engineering
SRM Institute of Science and Technology
