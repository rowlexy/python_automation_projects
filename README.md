WEEK 1 — Core Python Re-alignment
🧠 1. Expense Tracker (CLI)

Goal: Learn how to read, write, and append CSV data.

Scenario:
You’re managing your daily expenses and want a CLI tool to log transactions.

Requirements:

File: expenses.csv with headers: date,category,amount,description

Script should:

Add new expenses via user input.

Summarize total by category.

Show total expenses for the month.

Concepts Practiced:

CSV read/write

Loops & conditionals

Functions and user input

Bonus:

Add command-line options like --add, --summary.

🧠 2. Batch File Renamer

Goal: Manipulate filenames and use loops + os module.

Scenario:
You receive 100 invoice PDFs with inconsistent names and need to standardize them.

Requirements:

Rename files like INV1234.pdf → invoice_1234.pdf

Handle all .pdf files in a target folder.

Log renamed files in a .txt file.

Concepts Practiced:

Loops

os.listdir() & os.rename()

String operations and regex

WEEK 2 — Automation Building Blocks
🧠 3. Folder Organizer

Goal: Automate file management and apply os and shutil.

Scenario:
Your Downloads folder is cluttered. Create a script that organizes it by file type.

Requirements:

Create folders: /Images, /Docs, /Videos, /Others

Move files based on extension.

Log operations (file name → destination folder).

Concepts Practiced:

Path management

Error handling

Logging

Bonus:
Use argparse to pass the directory path as a command-line argument.

🧠 4. File Backup Script

Goal: Learn to automate backups.

Scenario:
You need to back up your Automation/Projects folder daily.

Requirements:

Copy all files into /Backups/ + date subfolder.

Skip temp or log files.

Print summary of copied files and total size.

Concepts Practiced:

File I/O

shutil.copy2()

Timestamped folders

os.path.getsize()

WEEK 3 — Data & Report Automation
🧠 5. Report Combiner

Goal: Merge CSVs into one clean dataset.

Scenario:
Each department sends a CSV report weekly; you need a master file.

Requirements:

Merge all .csv files in a folder.

Remove duplicates and sort by date.

Export combined report as Master_Report_<YYYYMMDD>.xlsx

Concepts Practiced:

pandas basics: concat, drop_duplicates, sort_values

File naming conventions

Export to Excel

Bonus:
Use environment variables to define the “reports folder.”

🧠 6. PDF Merger

Goal: Work with PDF automation.

Scenario:
You receive multiple PDFs (invoices, shipments, etc.) and need a single document.

Requirements:

Merge all .pdf files in a folder.

Save as merged_report.pdf

Optionally, add page numbers.

Concepts Practiced:

PyPDF2 or pypdf module

File loops

Error handling (skip corrupt files)

🧠 7. Email Report Sender

Goal: Send automated reports via email.

Scenario:
You want your system to automatically send the weekly master report to a recipient list.

Requirements:

Use smtplib and email.mime

Send email with subject: “Weekly Report”

Attach Master_Report.xlsx

Read recipients from recipients.txt

Concepts Practiced:

SMTP authentication

MIME multipart email

Exception handling

Bonus:
Store credentials in a .env file using python-dotenv.

WEEK 4 — System & API Automation
🧠 8. CLI Task Runner

Goal: Combine Linux + Python.

Scenario:
You want to automate repetitive system tasks (e.g., cleanup, backup, notifications).

Requirements:

Run 3 tasks: cleanup temp files, backup folders, log status.

Create a menu in the CLI (1, 2, 3 options).

Schedule daily with cron (crontab -e).

Concepts Practiced:

subprocess.run()

Logging

Automation scheduling

Bonus:
Add a “send email when done” function.

🧠 9. API Fetcher

Goal: Learn to interact with APIs and store results.

Scenario:
You want to track current exchange rates or GitHub issues daily.

Requirements:

Use requests to pull live JSON data.

Extract relevant fields (e.g., currency, rate, time).

Save data into a CSV log with timestamps.

Concepts Practiced:

REST APIs

JSON parsing

CSV write operations

Bonus:
Add retry logic if API request fails.

🧠 10. Log Analyzer (Bonus Project)

Goal: Analyze large text files for patterns.

Scenario:
You need to scan logs for failed transactions or errors.

Requirements:

Parse app.log or server.log

Extract lines with keywords (“ERROR”, “FAIL”)

Save to error_report.txt with timestamps.

Concepts Practiced:

File handling

Regex (re module)

Reporting