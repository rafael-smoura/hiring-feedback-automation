"""
Application designed for automated email dispatching.

Author: https://github.com/rafael-smoura
License: MIT
"""

from email.message import EmailMessage
import smtplib
import ssl
import csv
import os

# ============================================================================
# PASSWORD LOADING
# ============================================================================

try:

    with open(
        'password.txt',
        'r',
        encoding='utf-8-sig'
    ) as f:

        password = (
            f.read()
            .replace(" ", "")
            .replace("\ufeff", "")
            .strip()
        )

except FileNotFoundError:

    print(
        "[ERROR] The file 'password.txt' "
        "was not found."
    )

    exit()

# ============================================================================
# CSV CONFIGURATION
# ============================================================================

CSV_FILE = "candidates/candidates.csv"

# ============================================================================
# DEFAULT CANDIDATES (FALLBACK)
# ============================================================================

candidates = [
    """ {
            "name": "Mario Souza",
            "email": "mario@gmail.com"
        },
        {
            "name": "Maria Souza",
            "email": "maria@gmail.com"
        }
    """
]

# ============================================================================
# LOAD CSV IF EXISTS
# ============================================================================

if os.path.exists(CSV_FILE):

    print(f"Loading candidates from {CSV_FILE}...")

    try:

        with open(
            CSV_FILE,
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                # Google Forms format:
                # Nome, E-mail
                name_key = "Nome"
                email_key = "E-mail"

                if name_key in row and email_key in row:

                    candidates.append(
                        {
                            "name": row[name_key].strip(),
                            "email": row[email_key].strip()
                        }
                    )

    except Exception as error:

        print("[WARNING] Failed to read CSV file:")
        print(error)

else:

    print(f"{CSV_FILE} not found. Using fallback candidates.")

    candidates = []

# ============================================================================
# EMAIL CONFIGURATION
# ============================================================================

company_name = "V-lab"

from_email = "youremail@gmail.com"

subject = f"Hiring Process Update — {company_name}"

# ============================================================================
# EMAIL DISPATCH
# ============================================================================

ssl_context = ssl.create_default_context()
used_emails = set()

if not candidates:

    print("[WARNING] No candidates found. Nothing to send.")
    exit()

print("Connecting to Gmail and sending messages...")

try:

    with smtplib.SMTP_SSL(
        'smtp.gmail.com',
        465,
        context=ssl_context
    ) as smtp:

        smtp.login(from_email, password)

        for candidate in candidates:

            candidate_name = candidate["name"]
            to_email = candidate["email"]

            if to_email not in used_emails:

                used_emails.add(to_email)

                body = f"""
Hello, {candidate_name},

I hope this email finds you well.

Thank you very much for taking the time to participate in our recruitment process.

We had the opportunity to connect with outstanding professionals and, after review, we decided to move forward with another candidate.

Your profile stood out to us, especially regarding your organization and technical skills.

We will keep your information in our talent pool for future opportunities.

Best regards,
{company_name}
"""

                message = EmailMessage()
                message["From"] = from_email
                message["To"] = to_email
                message["Subject"] = subject
                message.set_content(body)

                smtp.send_message(message)

                print(f"[SUCCESS] {candidate_name} ({to_email})")

            else:

                print(f"[WARNING] Duplicate email skipped: {to_email}")

    print("Process completed successfully.")

except Exception as error:

    print("[ERROR] Failed during email dispatch.")
    print(error)