
import csv
import hashlib
from pathlib import Path
from datetime import datetime

LAB_DIR = Path.home() / "FIM-Lab"
BASELINE_FILE = Path.home() / "FIM-Lab-baseline.txt"
REPORT_FILE = Path.home() / "FIM-Lab-report.csv"


def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    with file_path.open("rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def load_baseline():
    baseline = {}
    with BASELINE_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(maxsplit=1)
            if len(parts) == 2:
                file_hash, file_path = parts
                baseline[file_path] = file_hash
    return baseline


def main():
    baseline = load_baseline()
    current = {}

    for path in LAB_DIR.iterdir():
        if path.is_file() and path.name != Path(__file__).name:
            current[str(path)] = calculate_hash(path)

    events = []
    for path, old_hash in baseline.items():
        if path not in current:
            events.append(("DELETED", path, old_hash, ""))
        elif current[path] != old_hash:
            events.append(("MODIFIED", path, old_hash, current[path]))

    for path, new_hash in current.items():
        if path not in baseline:
            events.append(("ADDED", path, "", new_hash))

    with REPORT_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "event", "path", "old_sha256", "new_sha256"])
        timestamp = datetime.now().astimezone().isoformat(timespec="seconds")
        for event, path, old_hash, new_hash in events:
            writer.writerow([timestamp, event, path, old_hash, new_hash])

    print("SentinelHash scan complete.")
    if events:
        for event, path, _, _ in events:
            print(f"{event}: {path}")
    else:
        print("No file changes detected.")
    print(f"Report saved to: {REPORT_FILE}")


if __name__ == "__main__":
    main()
