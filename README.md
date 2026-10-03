# 🔐 Message Encryption Program

A simple **Python-based message encryption and decryption program** that demonstrates the basic concept of **substitution-based encryption**.

The program creates a randomized key by shuffling a character set containing letters, digits, punctuation, and spaces. Each character in the original message is then replaced with its corresponding character from the shuffled key.

> ⚠️ **Note:** This project is intended for learning and demonstrating basic cryptography concepts. It is **not designed for securing real-world sensitive information**.

---

## 📌 Features

* 🔒 Encrypt text messages
* 🔓 Decrypt encrypted messages
* 🔑 Automatically generates a randomized substitution key
* 🔤 Supports:

  * Uppercase letters
  * Lowercase letters
  * Numbers
  * Punctuation
  * Spaces
* 🐍 Built entirely with Python
* 💡 Simple implementation suitable for beginners learning cryptography

---

## ⚙️ How It Works

The program creates a character set containing:

```text
Punctuation + Digits + Letters + Space
```

A copy of this character set is then randomly shuffled to create the encryption key.

### Encryption

For every character in the original message:

```text
Original Character
        ↓
Find its position in character set
        ↓
Use the character at the same position in the shuffled key
        ↓
Encrypted Character
```

For example, conceptually:

```text
Character Set → ABCDEFG...
Random Key    → XQPLM...
```

If:

```text
A → X
B → Q
C → P
```

then a message containing `ABC` becomes:

```text
ABC → XQP
```

### Decryption

Decryption performs the reverse process:

```text
Encrypted Character
        ↓
Find its position in the shuffled key
        ↓
Use the character at the same position in original character set
        ↓
Original Character
```

---

## 🛠️ Technologies Used

* **Python 3**
* `random`
* `string`

No external libraries are required.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/RanveerRaj04/Message-Encryption-Program.git
```

### 2. Navigate to the project folder

```bash
cd Message-Encryption-Program
```

### 3. Run the program

```bash
python "Message Encryption Program.py"
```

---

## 💻 Example

### Input

```text
Enter the message: Hello World!
```

### Output

```text
Original text - Hello World!
Encrypted text - <encrypted_message>
```

The program then asks:

```text
Would you like to decrypt any message? (Y/N):
```

Enter `Y` to provide an encrypted message and decrypt it.

---

## 📂 Project Structure

```text
Message-Encryption-Program/
│
├── Message Encryption Program.py
└── README.md
```

---

## 🧠 Concepts Learned

This project demonstrates several important Python and programming concepts:

* String manipulation
* Lists
* Functions
* `random.shuffle()`
* Character mapping
* Encryption and decryption logic
* User input
* Conditional statements
* Loops
* Python modules

---

## ⚠️ Security Disclaimer

This project demonstrates the **basic idea of substitution encryption** and should be considered an educational project.

It should **not be used to protect passwords, financial information, personal data, or other sensitive information**.

Modern cryptographic systems use extensively tested algorithms and secure key-management techniques rather than a simple randomly shuffled substitution table.

---

## 🔮 Future Improvements

Possible improvements include:

* [ ] Allow users to provide their own encryption key
* [ ] Save and load encryption keys
* [ ] Add a graphical user interface (GUI)
* [ ] Support encryption of files
* [ ] Add stronger modern cryptographic algorithms
* [ ] Improve input validation
* [ ] Add automated tests
* [ ] Add proper key management

---

## 👨‍💻 Author

**Ranveer Raj**

B.Tech CSE — Artificial Intelligence & Machine Learning

GitHub: [RanveerRaj04](https://github.com/RanveerRaj04)

---

## ⭐ Support

If you found this project useful for learning Python or basic cryptography, consider giving the repository a ⭐.
