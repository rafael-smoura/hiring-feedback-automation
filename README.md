

<p align="center">
  <img src="https://github.com/user-attachments/assets/97ae4be3-816e-4972-805b-ec9aa072cf32" alt="Hiring Feedback Automation" width="250">
</p>

<h1 align="center">
  Hiring Feedback Automation
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/language-Python-blue?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/security-SSL%20%7C%20TLS-red?style=flat-square&logo=google-cloud&logoColor=white" alt="Security SSL/TLS" />
  <img src="https://img.shields.io/badge/license-MIT-green?style=flat-square" alt="MIT License" />
</p>

---

## 🎯 The Motivation Behind the Project

Finding a job in tech is a challenging journey. Throughout my own experience, as well as observing fellow developers, I noticed a widespread problem in recruitment processes: **the complete lack of feedback**. 

Waiting weeks or months without knowing if you passed a technical assessment creates unnecessary anxiety, a feeling shared by thousands of candidates who are left in the dark. 

On the other side of the spectrum, many small to mid-sized organizations want to do the right thing but simply **lack the automation tools or the budget** to set up expensive HR platforms. 

To bridge this gap, I developed this open-source application. By leveraging an organization's secure SMTP access, it provides a completely **free, secure, and straightforward solution** to automate hiring responses. This project aims to support both sides: helping businesses maintain professional communication while protecting the mental health and peace of mind of job applicants.

---

## 🚀 Features

* **Secure Authentication:** Implements safe credential isolation using external configuration (`password.txt`), leveraging Google App Passwords to avoid hardcoded credentials.
* **Encrypted Dispatch:** Uses standard `SMTP_SSL` via port 465 wrapped in Python's native `ssl` context to secure email communication.
* **Encoding Reliability:** Built with `utf-8-sig` handling to automatically strip hidden Windows Byte Order Marks (BOM - `\ufeff`), mitigating runtime communication crashes.
* **Clean & Professional Templates:** Easily customizable email bodies tailored for HR workflows.

---

## 🧰 Architecture & Components

<table width="100%">
  <tr>
    <td width="220px" align="left" style="border: none;">
      <img src="https://skillicons.dev/icons?i=python" />
    </td>
    <td style="border: none; padding-left: 15px;">
      <strong>Core Automation Module (main.py):</strong> Handles network sockets, SSL wrapper negotiation, environment stream normalization, and structures standard RFC-compliant <code>EmailMessage</code> objects.
    </td>
  </tr>
</table>

---

## 📦 How to Setup and Run

### 1. Repository Setup
Clone the repository to your local environment:
```bash
git clone https://github.com/rafael-smoura/hiring-feedback-automation.git
cd hiring-feedback-automation
```

### 2. Credential Configuration
Create a file named password.txt exactly in the root folder of the project. Generate a 16-digit App Password inside your Google Account Security dashboard and paste it inside the file without spaces:

```
your十六digitapppassword
```
🔐 Security Note: Make sure your .gitignore file includes password.txt so your credentials are never pushed to public servers.

### 3. Execution
Run the script using your Python environment launcher:
```
python main.py
```

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
