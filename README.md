# Datelistinator 🗓️
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![GitHub Repo Size](https://img.shields.io/github/repo-size/RohanTheProgrammer/datelistinator)
![Last Commit](https://img.shields.io/github/last-commit/RohanTheProgrammer/datelistinator)

Datelistinator is a simple and flexible **CLI tool written in Python** that generates a list of dates between two given dates in a user-defined format.

It is designed as a **helper tool for authorized security testing**, such as creating date-based wordlists commonly used in password audits and labs.

---

## Features
- Accepts date input in **DD-MM-YYYY** format
- Generates dates between a given range (inclusive)
- Supports **custom output formats** using `strftime`
- Clean command-line interface using `argparse`
- Input validation with meaningful error messages

---

## Requirements
- Python 3.x  
(No external libraries required)

---

## Installation
Clone the repository:

```bash
git clone https://github.com/RohanTheProgrammer/datelistinator.git
cd datelistinator
```

Make the script executable (optional):

```bash
chmod +x datelistinator.py
```

---

## Usage

### Basic usage

```bash
python3 datelistinator.py -i 01-01-2000 -l 05-01-2000
```

This generates a file named `datelist.txt` with dates in the default format (`DDMMYY`).

---

### Custom output format

Use the `-f` flag to specify any valid `strftime` format:

```bash
python3 datelistinator.py -i 01-01-2000 -l 05-01-2000 -f "%Y%m%d"
```

**Output:**

```
20000101
20000102
20000103
20000104
20000105
```

---

### Specify output file

```bash
python3 datelistinator.py -i 01-01-2000 -l 31-12-2000 -o dates.txt
```

---

## Supported Input Format

* **Input dates:** `DD-MM-YYYY`
  Example: `01-01-2001`

* **Output format:** Any valid Python `strftime` format
  Examples:

  * `%d%m%y` → `010101`
  * `%d%m%Y` → `01012001`
  * `%Y%m%d` → `20010101`

---

## Help

Use the help flag to see all options:

```bash
python3 datelistinator.py --help
```

---

## Use Case

This tool is intended for:

* Generating date-based wordlists
* Password auditing (authorized only)
* Cybersecurity labs and CTFs
* Learning and practicing Python CLI development

⚠️ **Use responsibly and only on systems you own or have explicit permission to test.**

---

## Author

**Rohan**\
Self-taught cybersecurity student\
GitHub: [RohanTheProgrammer](https://github.com/RohanTheProgrammer)