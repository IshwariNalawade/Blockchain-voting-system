# 🗳️ Blockchain-based Voting System (Python)

A minimal, **upload-ready** blockchain project demonstrating immutable voting records.
Short code, easy to run, and perfect for competitions and GitHub.

## ✨ Features
- Genesis block creation
- Append-only voting (each vote is a block)
- SHA-256 hashing + previous block linkage
- Full chain integrity validation
- Exports the chain to `chain.json` for transparency

## 🛠️ Tech
- Python 3.8+
- Standard library only (no external dependencies)

## 🚀 Quick Start
```bash
# 1) Run the script
python voting.py

# 2) See output in terminal and inspect the exported chain
type chain.json   # Windows
cat chain.json    # macOS / Linux
```

Expected terminal output (example):
```
Blockchain valid: True
Index: 0, Vote: Genesis Vote, Hash: 8a0d3b1b2f1b9b2e...
Index: 1, Vote: Alice -> Candidate_A, Hash: 2c9d7a4a0c7f3f10...
Index: 2, Vote: Bob -> Candidate_B, Hash: 0e1a9f35db3a5c2b...
Index: 3, Vote: Charlie -> Candidate_A, Hash: 7f9e3d1a0b2c4d6e...
```

This also creates a `chain.json` file like:
```json
[
  {
    "index": 0,
    "vote": "Genesis Vote",
    "timestamp": 1720000000.123,
    "previous_hash": "0",
    "hash": "xxxxxxxx"
  },
  {
    "index": 1,
    "vote": "Alice -> Candidate_A",
    "timestamp": 1720000001.456,
    "previous_hash": "xxxxxxxx",
    "hash": "yyyyyyyy"
  }
]
```

## 📁 Project Structure
```
blockchain-voting-system/
├── voting.py        # main script with Block + Blockchain + demo
├── README.md        # docs and instructions
├── LICENSE          # MIT license
└── .gitignore
```

## 🧪 How It Works (in short)
- Every vote is stored in a **Block** with: index, timestamp, vote text, previous hash, and its own hash.
- A **Blockchain** is a list of blocks where each block references the previous block’s hash.
- Any change to a block’s contents changes its hash → the chain validation fails → **immutability**.

## 📦 GitHub Upload Guide
```bash
git init
git add .
git commit -m "Add blockchain-based voting system (Python)"
git branch -M main
git remote add origin https://github.com/<your-username>/blockchain-voting-system.git
git push -u origin main
```

## 🔒 Notes
- This is a learning/demo project (not production-grade voting).
- No personal data is stored; votes are simple strings for demonstration.

## 📄 License
MIT
