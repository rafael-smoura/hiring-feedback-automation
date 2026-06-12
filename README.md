

<p align="center">
  <img src="https://github.com/user-attachments/assets/97ae4be3-816e-4972-805b-ec9aa072cf32" alt="Hiring Feedback Automation" width="250">
</p>

<h1 align="center">
  Hiring Feedback Automation
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/language-Python-blue?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/security-SSL%20%7C%20TLS-red?style=flat-square&logo=google-cloud&logoColor=white" />
  <img src="https://img.shields.io/badge/data-CSV%20%7C%20Google%20Forms-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/license-MIT-green?style=flat-square" />
</p>

---

## 🎯 The Motivation Behind the Project

Finding a job in tech is a challenging journey. One recurring issue in recruitment processes is the **lack of feedback after technical assessments**, leaving candidates uncertain about their progress.

At the same time, many companies—especially small and mid-sized ones—lack the infrastructure to automate communication with candidates.

This project was created to solve that gap by providing a **lightweight, open-source email automation system** that integrates with **Google Forms exports (CSV)** and enables **bulk personalized email delivery via SMTP**.

The goal is to improve communication efficiency while maintaining simplicity, security, and full control over the process.

---

## 🚀 Features

- **Google Forms Integration (CSV-based):** Automatically reads candidate data exported from Google Forms / Google Sheets.
- **Bulk Email Dispatch:** Sends personalized emails to multiple recipients in a single execution.
- **Duplicate Protection:** Prevents sending multiple emails to the same address.
- **Secure Authentication:** Uses external `password.txt` file with Google App Passwords.
- **Encrypted Communication:** Uses `SMTP_SSL` with TLS/SSL context.
- **Fallback System:** Supports default candidates if CSV file is not available.
- **Clean Data Parsing:** Handles UTF-8 encoding and structured CSV ingestion.

---

## 🧰 Architecture Overview

```text
Google Forms
    ↓
Google Sheets
    ↓
CSV Export (candidates.csv)
    ↓
Python Automation Script
    ↓
SMTP Gmail Server
    ↓
Personalized Emails Sent

```

## 📦 Project Structure

```
hiring-feedback-automation/
│
├── main.py
├── password.txt
│
└── candidates/
    └── candidates.csv
```

## 📊 CSV Format (Google Forms Export)

```
Nome,E-mail
Rafael Silva,rafael@gmail.com
Maria Souza,maria@gmail.com
```
⚠️ Column names must match exactly: Nome and E-mail

## ⚙️ How It Works

The script loads candidate data from ```candidates/candidates.csv```
If the file does not exist, fallback candidates are used.
It removes duplicate emails automatically.
A personalized email is generated for each candidate.
All emails are sent through a single secure SMTP session.

## 📦 How to Setup and Run

### 1. Clone the repository
```
git clone https://github.com/rafael-smoura/hiring-feedback-automation.git
cd hiring-feedback-automation
```
### 2. Configure credentials

Create a file named:

`password.txt`

Inside it, place your Google App Password:

`your16digitapppassword`

🔐 Make sure this file is included in `.gitignore`.

### 3. Prepare candidates file (optional)

Export from Google Sheets:

`candidates/candidates.csv`
### 4. Run the application
`python main.py`
## 🔐 Security Notes

- Passwords are never hardcoded.
- Uses SSL/TLS encrypted SMTP connection.
- No external APIs required.
- Fully offline processing of CSV data.


## 🌎 Connect With Me
<p align="left">
  <a href="https://www.linkedin.com/in/rafaelsmouraoficial">
    <img alt="LinkedIn" src="https://custom-icon-badges.demolab.com/badge/-LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white"/>
  </a>&nbsp;
  <a href="https://github.com/rafael-smoura">
    <img alt="GitHub" src="https://custom-icon-badges.demolab.com/badge/-GitHub-black?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
</p>

---

<p align="center">
  
  <b>💡 Developed with purpose.</b><br>
  Engineering software means building solutions that resolve technical roadblocks while positively impacting human experiences.
</p>

---

<p align="center">
  <sub/>Animated icon by <a href="https://www.flaticon.com/free-animated-icons/email" title="email animated icons">Flaticon</a></sub>
</p>
