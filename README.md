# 🗳️ Blockchain-based Voting System (Python)

A minimal, **upload-ready** blockchain project demonstrating immutable voting records.  
Short code, easy to run, and perfect for competitions and GitHub.

---

## ✨ Features
- Genesis block creation
- Append-only voting (each vote is a block)
- SHA-256 hashing + previous block linkage
- Full chain integrity validation
- Exports the chain to `chain.json` for transparency

---

## 🛠️ Tech
- Python 3.8+
- Standard library only (no external dependencies)

---

## 🚀 Quick Start
```bash
# 1) Run the script
python voting.py

# 2) See output in terminal and inspect the exported chain
type chain.json   # Windows
cat chain.json    # macOS / Linux
