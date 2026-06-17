<div align="center">

# 🚫 Distraction Blocker CLI

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)]()
[![macOS](https://img.shields.io/badge/macOS-000000?style=for-the-badge&logo=apple&logoColor=white)]()
[![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)](https://opensource.org/licenses/MIT)

*A lightweight, cross-platform command-line utility to temporarily block distracting websites and reclaim your focus.*

</div>

---

## ✨ Features
* 🛡️ **System-Level Blocking:** Bypasses browser extensions by managing local DNS routing directly to `127.0.0.1`.
* 🌍 **Cross-Platform:** Automatically detects your host operating system to target the correct file paths.
* ⏱️ **Automated Scheduling:** Uses the `datetime` module to enforce strict focus blocks and cleanly restore internet access during free time.
* 🪶 **Lightweight Execution:** Runs quietly in the background with minimal CPU footprint.

## 🛠️ Technologies Used
* **Language:** Python 3
* **Libraries:** `os`, `time`, `datetime`, `platform` (Standard Library)

## 🚀 How It Works
The script requires administrative privileges to modify your system's networking. Once initiated, it asks for your desired working hours and a list of websites to block. It enters a background loop, checking the system clock every 60 seconds. 

During focus hours, it appends the target websites to your local `hosts` file. When the shift ends, it safely parses the file and removes only the blocked entries, restoring full access without corrupting your network settings.

## 💻 How to Run

1. **Clone this repository** to your local machine:
   ```bash
   git clone https://github.com/Coreoflore/distraction-blocker-cli.git
   ```

2. **Open your terminal with administrative privileges:**
   * **Windows:** Run Command Prompt as Administrator.
   * **macOS/Linux:** Prefix your execution command with `sudo`.

3. **Navigate to the directory and run the script:**
   ```bash
   python blocker.py
   ```

4. **Follow the on-screen prompts** to set your schedule and lock in.
