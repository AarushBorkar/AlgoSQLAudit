# 🚀 AlgoSQLAudit

## 📌 Project Overview

AlgoSQLAudit is a blockchain-based SQL audit logging system built on the Algorand network.
It ensures that database query logs are immutable, verifiable, and tamper-proof.

## 🎯 Problem Statement

Traditional database logs can be modified or deleted, leading to security and compliance risks.

## 💡 Solution

This project stores cryptographic hashes of SQL queries on the Algorand blockchain, ensuring:

* Data integrity
* Tamper resistance
* Transparent auditing

## 🛠 Tech Stack

* Algorand Blockchain
* Python (Algorand SDK)
* SHA-256 Hashing

## 📂 Project Structure

* `src/` → Core logic for logging queries
* `docs/` → Architecture design
* `README.md` → Documentation

## ⚙️ How It Works

1. SQL query is captured
2. Query is hashed using SHA-256
3. Hash is stored on Algorand blockchain
4. Later verification ensures integrity

## 🚧 Current Status

Initial project setup with hashing-based audit logging.

## 📌 Future Enhancements

* Smart contract integration
* Real-time database hooks
* Dashboard for audit visualization
