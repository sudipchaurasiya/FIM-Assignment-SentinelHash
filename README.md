# File Integrity Monitoring (FIM) — SentinelHash

## Project Overview
This project demonstrates basic file integrity monitoring using Python and SHA-256 hashes in Kali Linux.

## Features
- Creates a baseline for three sample files.
- Stores SHA-256 hashes and file paths.
- Includes a GPG-encrypted baseline copy.
- Detects added, modified, and deleted files.
- Saves test results in CSV format.

## Test Results
The project was tested by adding a new file, modifying an existing file, and deleting a baseline file. The checker detected all three changes. The sample files were then restored, and the final check reported no file changes.

## Project Contents
- `fim_monitor.py` — FIM checker script
- `FIM_Assignment_Report.pdf` — assignment report
- `Baseline/` — plain-text and encrypted baselines
- `Sample_Files/` — original sample files
- `Documentation/` — README and test explanations
- `Evidence_Screenshots/` — practical evidence screenshots
- `FIM_Test_Results.csv` — recorded test findings

## Limitations
The current checker scans files directly inside the monitored directory, does not scan subdirectories, and overwrites its CSV report on each run.

## Tools
Kali Linux, Python 3, SHA-256, GPG, and Git.

## AI Disclosure
AI assistance was used to organize and improve the wording of the documentation. The practical tests and evidence were produced in the lab.

## Disclaimer
This project was created for educational purposes in a controlled lab environment.
