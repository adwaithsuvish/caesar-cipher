# 🔡 Caesar Cipher Tool

> A simple Python implementation of the Caesar Cipher — one of the oldest known encryption techniques — built to understand the fundamentals of classical cryptography.

---

## 📖 About

This program encrypts text using the **Caesar Cipher**, a substitution cipher where each letter is shifted a fixed number of positions down the alphabet. This version uses a **fixed shift of 4** (`a → e`, `b → f`, `c → g`, and so on).

While trivially easy to break by modern standards, understanding the Caesar Cipher is a foundational step into cryptography — it introduces core concepts like **substitution** and **shifts** that apply to far more complex encryption systems used today.

---

## ✨ Features

- 🔒 Encrypts lowercase text using a fixed shift of 4
- 🐍 Pure Python — no external dependencies

---

## ⚠️ Current Limitations

- The shift is fixed at 4 — not currently customizable by the user
- Encrypt only — no decrypt function yet

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/adwaithsuvish/caesar-cipher.git
cd caesar-cipher

# Run it
python main.py
```

You'll be prompted to enter text, and the encrypted result will be printed.

---

## 💡 Example

```
Enter the choice:1
Enter the text to encrypt: helloworld
Enter the shift value: 4
lippsasvph
```

---

## 🛠️ Built With

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## 🧩 Planned Improvements

- [ ] Support uppercase letters, spaces, and punctuation
- [x] Let the user choose a custom shift value instead of a fixed one
- [x] Add a decrypt function
- [ ] Add a brute-force mode to crack messages without knowing the shift

---

## 📌 Why I Built This

Classical ciphers like this are the starting point for understanding modern cryptography — before working with real algorithms (AES, RSA, etc.), it helps to understand basic ideas like substitution and shifting, and why simple ciphers like this are easy to break.

---

## 📄 License

No license specified yet.
