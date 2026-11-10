# Tally XML Bridge 🚀

An open-source lightweight Python CLI utility designed for accountants and developers to convert standardized CSV bank statements and GST tax ledgers into **Tally Prime compliant XML** import files.

## Features
- **Fast CSV Parsing:** Reads bank transaction rows (Date, Narration, Ledger, Amount).
- **Zero External Dependencies:** Built purely on Python's standard library (`csv`, `xml.etree.ElementTree`).
- **Tally Prime Ready:** Generates standard `<ENVELOPE>` tags compatible with Tally XML voucher import.

## Usage
```bash
python converter.py bank_statement.csv tally_vouchers.xml
