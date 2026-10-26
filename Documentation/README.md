# SentinelHash - File Integrity Monitoring (FIM)

## Project Overview
SentinelHash is a Python-based File Integrity Monitoring project built on Kali Linux. It uses SHA-256 hashes to detect added, modified, and deleted files.

## Sample Files
- critical.txt
- readme.txt
- system.conf

## Tools Used
- Kali Linux
- Python 3
- SHA-256
- GNU Privacy Guard (GPG)

## Baseline Files
The plain-text baseline is stored at ~/FIM-Lab-baseline.txt.
The encrypted baseline is stored at ~/FIM-Lab-baseline.txt.gpg.
The encrypted copy uses AES-256 and is protected by a private passphrase.

## How to Run
Run the checker using:
python3 ~/FIM-Lab/fim_monitor.py

The checker compares the current files with the saved baseline and reports ADDED, MODIFIED, and DELETED events. A CSV report is saved to ~/FIM-Lab-report.csv.

## Test Results
1. ADDED: The checker detected new.txt after it was created.
2. MODIFIED: The checker detected changes to critical.txt.
3. DELETED: The checker detected when readme.txt was removed.
4. Baseline check: The checker reported no changes after the original files were restored.

## Known Limitations
- This is an educational lab project.
- The checker scans files directly inside the monitored folder and does not scan subfolders.
- It does not run continuously or send automatic alerts.
- If an attacker can modify both the files and the baseline, the changes may not be detected.
- The encrypted baseline requires the correct passphrase to decrypt.

## AI Disclosure
AI assistance was used to help understand the requirements, organize the practical steps, and prepare documentation. Commands were run in the Kali Linux lab, and test results should be supported by the submitted screenshots.
