from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle
)
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os

OUT = "FIM_Assignment_Report.pdf"

# Use Times New Roman if installed; otherwise use the built-in Times font.
regular = "Times-Roman"
bold = "Times-Bold"
italic = "Times-Italic"

font_paths = [
    ("/usr/share/fonts/truetype/msttcorefonts/Times_New_Roman.ttf",
     "/usr/share/fonts/truetype/msttcorefonts/Times_New_Roman_Bold.ttf",
     "/usr/share/fonts/truetype/msttcorefonts/Times_New_Roman_Italic.ttf"),
    ("/usr/share/fonts/truetype/liberation2/LiberationSerif-Regular.ttf",
     "/usr/share/fonts/truetype/liberation2/LiberationSerif-Bold.ttf",
     "/usr/share/fonts/truetype/liberation2/LiberationSerif-Italic.ttf"),
]

for r, b, i in font_paths:
    if os.path.exists(r):
        pdfmetrics.registerFont(TTFont("ReportTimes", r))
        regular = "ReportTimes"
        if os.path.exists(b):
            pdfmetrics.registerFont(TTFont("ReportTimes-Bold", b))
            bold = "ReportTimes-Bold"
        if os.path.exists(i):
            pdfmetrics.registerFont(TTFont("ReportTimes-Italic", i))
            italic = "ReportTimes-Italic"
        break

doc = SimpleDocTemplate(
    OUT,
    pagesize=letter,
    rightMargin=1*inch,
    leftMargin=1*inch,
    topMargin=1*inch,
    bottomMargin=1*inch,
    title="File Integrity Monitoring (FIM) Assignment",
    author="Sudip Kumar Chaurasiya"
)

styles = getSampleStyleSheet()

body = ParagraphStyle(
    "BodyAPA", fontName=regular, fontSize=12, leading=24,
    alignment=TA_LEFT, spaceAfter=0
)
heading = ParagraphStyle(
    "HeadingAPA", fontName=bold, fontSize=12, leading=24,
    alignment=TA_CENTER, spaceBefore=0, spaceAfter=0,
    keepWithNext=True
)
subheading = ParagraphStyle(
    "SubheadingAPA", fontName=bold, fontSize=12, leading=24,
    alignment=TA_LEFT, spaceBefore=0, spaceAfter=0,
    keepWithNext=True
)
cover = ParagraphStyle(
    "CoverAPA", parent=body, alignment=TA_CENTER, leading=24
)
small = ParagraphStyle(
    "SmallAPA", fontName=regular, fontSize=9, leading=12
)

story = []

# APA-style student title page
story.append(Spacer(1, 1.5*inch))
story.append(Paragraph(
    "<b>SPURVANCE ASSIGNMENT</b>", cover
))
story.append(Spacer(1, 0.25*inch))
story.append(Paragraph(
    "<b>File Integrity Monitoring (FIM)</b>", cover
))
story.append(Spacer(1, 0.25*inch))
for line in [
    "Sudip Kumar Chaurasiya",
    "College: Model Institute of Technology (MIT)",
    "Organization: Spurvance",
    "Date: October 12, 2026"
]:
    story.append(Paragraph(line, cover))

story.append(PageBreak())

def H(text):
    story.append(Paragraph(text, heading))

def SH(text):
    story.append(Paragraph(text, subheading))

def P(text):
    story.append(Paragraph(text, body))

H("Abstract")
P("This assignment describes a small File Integrity Monitoring (FIM) project named SentinelHash. The project creates a SHA-256 baseline for three sample files, protects a separate copy of the baseline with GPG encryption, and compares the current files with the original baseline. The checker reports files that are added, modified, or deleted. Three controlled tests were completed in Kali Linux. The results showed that the checker detected each type of change. The sample files were restored afterward, and a final check reported that no changes were detected.")

H("Introduction")
P("File Integrity Monitoring is a method for checking whether files have changed. A cryptographic hash creates a fixed-length value from a file's contents. If the contents change, the hash will normally change too. By comparing a current hash with a trusted baseline hash, a monitoring script can identify possible additions, modifications, and deletions.")
P("The purpose of this assignment was to build and test a small FIM tool in a controlled Kali Linux lab. The project uses Python for file hashing and comparison, a plain-text baseline for the original hashes, and GPG to create an encrypted copy of the baseline.")

H("Method")
SH("Lab Environment and Sample Files")
P("The project was completed in Kali Linux using Python 3 and GPG. The monitored directory was ~/FIM-Lab. The baseline was stored separately as ~/FIM-Lab-baseline.txt. The checker script was named fim_monitor.py. Three sample files were included in the original baseline.")

table_data = [
    ["Sample file", "Original content", "SHA-256 hash"],
    ["critical.txt", "approved configuration",
     "30488ba9d1cf1884837d03a9b5e9e7108b49c8f28d0ddcc31df764a1149b631e"],
    ["readme.txt", "training sample",
     "4ea2a72ed972663f8e56c9680a9e7e5dde08b2a4810e50f5737b88f5a2fc5cae"],
    ["system.conf", "firewall=enabled",
     "f9906af395d0ee704a68d793b52136ba5a2539b58b92fb5187c9cf5e0a0a3127"]
]
tbl = Table(table_data, colWidths=[1.0*inch, 1.35*inch, 3.1*inch],
            repeatRows=1)
tbl.setStyle(TableStyle([
    ("FONTNAME", (0, 0), (-1, -1), regular),
    ("FONTNAME", (0, 0), (-1, 0), bold),
    ("FONTSIZE", (0, 0), (-1, -1), 8),
    ("LEADING", (0, 0), (-1, -1), 11),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 4),
    ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
]))
story.append(Spacer(1, 6))
story.append(tbl)
story.append(Spacer(1, 12))

SH("Baseline Generation and Encryption")
P("The baseline report recorded the path and SHA-256 hash of each sample file. This baseline acted as the trusted reference for testing. A separate encrypted copy was created with GPG using AES-256 encryption. The encrypted baseline was decrypted for verification and compared with the plain-text baseline. The comparison succeeded, confirming that the encrypted copy matched the original baseline.")

SH("Checker Design")
P("The Python checker reads the baseline, scans files directly inside the FIM-Lab directory, calculates SHA-256 hashes, and compares the current state with the baseline. It reports ADDED when a file is not listed in the baseline, MODIFIED when a known file has a different hash, and DELETED when a baseline file is missing. The checker writes a timestamp, event, path, old hash, and new hash to a CSV report.")

H("Results")
SH("Test 1: Added File")
P("Action: A new file named new.txt was created in the monitored directory. The checker was run after the file was added.")
P("Output: The checker reported ADDED for /home/kali/FIM-Lab/new.txt.")
P("Meaning: The checker detected a file that was not present in the original baseline. This shows that the script can identify newly created files in the monitored directory.")
P("Usefulness: Unexpected new files can indicate an unapproved change. An administrator can investigate the file and decide whether it is expected.")

SH("Test 2: Modified File")
P("Action: Text was appended to critical.txt to simulate an unauthorized change. The checker was run again.")
P("Output: The checker reported MODIFIED for /home/kali/FIM-Lab/critical.txt. It also reported new.txt because that file was still present.")
P("Meaning: The changed contents produced a different SHA-256 hash from the baseline. The mismatch allowed the checker to identify the modified file.")
P("Usefulness: Hash comparison can help detect unexpected edits to configuration files, scripts, or other files that should remain unchanged.")

SH("Test 3: Deleted File")
P("Action: The baseline file readme.txt was deleted. The checker was run a third time.")
P("Output: The checker reported DELETED for /home/kali/FIM-Lab/readme.txt. It also reported the modified critical.txt and added new.txt, which were still different from the baseline.")
P("Meaning: The checker compared the baseline paths with the current directory and found that readme.txt was missing.")
P("Usefulness: Missing files can indicate accidental deletion or unauthorized activity. The result provides a starting point for further investigation.")

SH("Restoration and Final Check")
P("After the tests, critical.txt and readme.txt were restored to their original contents, and new.txt was removed. The checker was run again. The final output stated, No file changes detected. This confirmed that the monitored sample files matched the original baseline at the time of the final check.")
P("The test-results CSV preserves the combined findings from the test run: ADDED for new.txt, MODIFIED for critical.txt, and DELETED for readme.txt. Screenshots document baseline creation, encryption verification, each test action and detection, restoration, and the final clean check.")

H("Discussion")
P("The project demonstrated a basic method for monitoring file integrity with SHA-256 hashes. The separate encrypted baseline provided additional protection for the reference data. The tests showed that the checker could identify the three required event types. The final clean check showed that the sample files had been restored to their expected state.")
P("A hash mismatch indicates that file contents changed, but it does not prove that the change was malicious. A new or deleted file also requires context before its cause can be determined.")

H("Limitations")
P("The current version scans only files directly inside the monitored directory and does not scan subdirectories. The CSV report is overwritten on each run, so evidence from individual runs must be saved separately when a longer history is required. The baseline must be protected from unauthorized changes. If an attacker can change both the files and the baseline, the comparison may no longer be trustworthy.")
P("The checker reports file changes but does not identify who made a change, why it occurred, or whether it is harmful. It does not provide automatic alerts or continuous background monitoring. These features could be added in a future version.")

H("Conclusion")
P("This assignment completed a basic File Integrity Monitoring project using Python, SHA-256, and GPG in Kali Linux. A baseline was created for three sample files, and an encrypted copy was verified. The checker successfully reported an added file, a modified file, and a deleted baseline file. After restoration, the final check reported no changes. This practical work improved understanding of file hashing, baseline protection, change detection, and evidence collection.")

H("Tools Used")
P("Kali Linux, Python 3, Python hashlib, GPG encryption, CSV reporting, and terminal screenshots.")

H("AI Use Disclosure")
P("AI assistance was used to help organize the report and improve wording. The lab setup, commands, file changes, checker runs, and screenshots were completed and verified by the student. The results are based on the recorded lab output.")

H("Evidence Index")
P("The submission includes the Python source code, plain-text baseline, encrypted baseline, test-results CSV, README, test explanations, and timestamped evidence screenshots. The screenshots document baseline creation, encryption and verification, the three tests, restoration of sample files, and the final integrity check.")

def page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont(regular, 12)
    canvas.drawRightString(letter[0] - inch, letter[1] - 0.55*inch,
                           str(doc.page))
    canvas.restoreState()

doc.build(story, onFirstPage=page_number, onLaterPages=page_number)
print("PDF created:", os.path.abspath(OUT))
