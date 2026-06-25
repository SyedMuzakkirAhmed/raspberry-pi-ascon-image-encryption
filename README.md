# Image File Encryption and Decryption Using Ascon Cipher on Raspberry Pi

## Overview

This project implements secure image file encryption and decryption using the Ascon-128a lightweight cryptographic algorithm on Raspberry Pi.

The system allows secure image transfer between devices by encrypting image data before transmission and decrypting it at the receiver.

## Features

- Ascon-128a encryption
- Secure image transfer
- Raspberry Pi implementation
- Lightweight cryptography
- File integrity verification

## Hardware

- Raspberry Pi 3/4
- Laptop (Sender)
- Laptop (Receiver)

## Software

- Python 3
- Ascon Library
- Socket Programming

## System Architecture

┌─────────────┐       ┌─────────────────────────┐
│  Laptop A   │──────▶│     Raspberry Pi        │
│   Sender    │       │                         │
│             │       │  Ascon-128a Encryption  │
│ image.jpg   │       │                         │
└─────────────┘       └───────────┬─────────────┘
                                  │
                                  ▼
                        ┌────────────────────┐
                        │ Encrypted Image    │
                        │    Ciphertext      │
                        └─────────┬──────────┘
                                  │
                                  ▼
                       ┌─────────────────────┐
                       │ Secure Transmission │
                       └─────────┬───────────┘
                                 │
                                 ▼
                     ┌────────────────────────┐
                     │     Raspberry Pi       │
                     │                        │
                     │ Ascon-128a Decryption  │
                     └───────────┬────────────┘
                                 │
                                 ▼
                     ┌────────────────────────┐
                     │       Laptop B         │
                     │       Receiver         │
                     │   Restored image.jpg   │
                     └────────────────────────┘

## Workflow

1. Select image
2. Encrypt using Ascon
3. Transfer encrypted file
4. Decrypt at receiver
5. Verify image integrity

## Results

Original image size: XX KB

Encryption time: XX ms

Decryption time: XX ms

## Future Scope

- Real-time image streaming
- Video encryption
- IoT device integration

## Author

Syed Muzakkir Ahmed
