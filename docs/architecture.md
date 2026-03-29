# Architecture Overview

1. User/Application executes SQL query
2. Query is passed to audit logger
3. Query is hashed using SHA-256
4. Hash is stored on Algorand blockchain (future step)
5. Verification system checks integrity

Components:
- Logger Module
- Hashing Layer
- Blockchain Storage (Algorand)