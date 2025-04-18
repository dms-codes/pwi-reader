# 📝 PWI Text Extractor (UTF-8)

This Python script extracts human-readable text from `.PWI` files (Pocket Word Document files) using UTF-8 decoding. It's designed to cleanly filter out binary noise and retain only meaningful lines containing alphanumeric characters.

---

## 🚀 Features

- ✅ Skips the 512-byte PWI file header
- ✅ Decodes content using UTF-8 (ignores undecodable characters)
- ✅ Filters out empty or binary-like lines
- ✅ Optionally saves the result to a `.txt` file

---

## 📦 Requirements

- Python 3.x  
- No external dependencies (uses built-in modules)

---

## 📂 Usage

1. Save the script as `extract_pwi.py`.
2. Place your `.pwi` file in the same folder or provide the full path.
3. Run the script:

```bash
python extract_pwi.py
