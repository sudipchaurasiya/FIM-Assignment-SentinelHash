# SentinelHash - FIM Test Explanations

## Test 1: Added File
Action: Created a new file named new.txt inside the monitored folder.
Output: The checker reported ADDED for new.txt.
Meaning: The file was not present in the original baseline.
Usefulness: This helps identify unexpected files added to a monitored directory.

## Test 2: Modified File
Action: Added unauthorized test text to critical.txt.
Output: The checker reported MODIFIED for critical.txt.
Meaning: The file's SHA-256 hash no longer matched the saved baseline.
Usefulness: This helps identify unexpected changes to important files.

## Test 3: Deleted File
Action: Deleted readme.txt from the monitored folder.
Output: The checker reported DELETED for readme.txt.
Meaning: A file recorded in the baseline was missing from the current folder.
Usefulness: This helps identify accidental or unauthorized file removal.

## Baseline Reset Verification
Action: Restored the original sample file contents after testing.
Output: The checker reported No file changes detected.
Meaning: The current sample files matched the saved baseline.
Usefulness: This confirms the checker can recognize the expected baseline state.
