# Distraction Blocker CLI

A lightweight, cross-platform command-line utility written in Python that temporarily modifies the system `hosts` file to block distracting websites during scheduled focus hours. 

## Features
* **System-Level Blocking:** Bypasses browser extensions by managing local DNS routing to `127.0.0.1`.
* **Cross-Platform:** Automatically detects the host operating system to target the correct file paths (Windows, macOS, Linux).
* **Automated Scheduling:** Uses the `datetime` module to enforce strict focus blocks and cleanly restore internet access during free time.
* **Lightweight Execution:** Runs in the background with minimal CPU footprint.

## Technologies Used
* Python 3
* Standard Library modules: `os`, `time`, `datetime`, `platform`

## How It Works
The script requires administrative privileges to run. Once initiated, it asks for your desired working hours and a list of websites to block. It will then enter a background loop, checking the system time every 60 seconds. During focus hours, it appends the target websites to the `hosts` file. When the shift ends, it safely parses the file and removes only the blocked entries, restoring full access.

## How to Run
1. Clone this repository to your local machine.
2. Open your terminal with administrative privileges:
   * **Windows:** Run Command Prompt as Administrator.
   * **macOS/Linux:** Prefix your execution command with `sudo`.
3. Navigate to the directory and run:
   ```bash
   python blocker.py