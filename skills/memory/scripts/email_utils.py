#!/usr/bin/env python3
"""
g1itchbot email utilities
Read, send, and manage emails from g1itchBot8888@gmail.com
"""

import imaplib
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import decode_header
from datetime import datetime
import json
import os

# Credentials
EMAIL = "g1itchBot8888@gmail.com"
APP_PASSWORD = "yqdj dfvg xdmz cmxw"
BILL_EMAIL = "hezhenqian@gmail.com"

STATE_FILE = os.path.expanduser("~/clawd/memory/email-state.json")


def load_state():
    """Load email processing state"""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    return {"last_checked": None, "last_uid": None, "processed_uids": []}


def save_state(state):
    """Save email processing state"""
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)


def get_unread_emails(limit=10):
    """Fetch unread emails, returns list of dicts"""
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL, APP_PASSWORD)
    mail.select("inbox")
    
    # Search for unread emails
    status, messages = mail.search(None, "UNSEEN")
    email_ids = messages[0].split()
    
    emails = []
    for eid in email_ids[-limit:]:  # Get latest N
        status, msg_data = mail.fetch(eid, "(RFC822 UID)")
        
        # Extract UID
        uid = None
        for part in msg_data:
            if isinstance(part, tuple):
                uid_match = part[0].decode() if isinstance(part[0], bytes) else part[0]
                if "UID" in uid_match:
                    uid = uid_match.split("UID")[1].split()[0]
        
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                
                # Decode subject
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding or "utf-8")
                
                from_ = msg.get("From")
                date_ = msg.get("Date")
                message_id = msg.get("Message-ID")
                
                # Get body
                body = ""
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            payload = part.get_payload(decode=True)
                            if payload:
                                body = payload.decode(errors='replace')
                            break
                else:
                    payload = msg.get_payload(decode=True)
                    if payload:
                        body = payload.decode(errors='replace')
                
                emails.append({
                    "id": eid.decode() if isinstance(eid, bytes) else eid,
                    "uid": uid,
                    "message_id": message_id,
                    "from": from_,
                    "date": date_,
                    "subject": subject,
                    "body": body[:2000]  # Truncate long bodies
                })
    
    mail.logout()
    return emails


def get_all_emails(limit=10, unread_only=False):
    """Fetch emails (all or unread only)"""
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL, APP_PASSWORD)
    mail.select("inbox")
    
    search_criteria = "UNSEEN" if unread_only else "ALL"
    status, messages = mail.search(None, search_criteria)
    email_ids = messages[0].split()
    
    emails = []
    for eid in email_ids[-limit:]:
        status, msg_data = mail.fetch(eid, "(RFC822)")
        
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding or "utf-8")
                
                from_ = msg.get("From")
                date_ = msg.get("Date")
                
                body = ""
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            payload = part.get_payload(decode=True)
                            if payload:
                                body = payload.decode(errors='replace')
                            break
                else:
                    payload = msg.get_payload(decode=True)
                    if payload:
                        body = payload.decode(errors='replace')
                
                emails.append({
                    "from": from_,
                    "date": date_,
                    "subject": subject,
                    "body": body[:2000]
                })
    
    mail.logout()
    return emails


def send_email(to, subject, body, reply_to_msg_id=None):
    """Send an email"""
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = to
    msg['Subject'] = subject
    
    if reply_to_msg_id:
        msg['In-Reply-To'] = reply_to_msg_id
        msg['References'] = reply_to_msg_id
    
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL, APP_PASSWORD)
    server.sendmail(EMAIL, to, msg.as_string())
    server.quit()
    
    return True


def mark_as_read(email_id):
    """Mark an email as read"""
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL, APP_PASSWORD)
    mail.select("inbox")
    mail.store(email_id, '+FLAGS', '\\Seen')
    mail.logout()


def check_new_emails():
    """Check for new unread emails and return summary"""
    state = load_state()
    emails = get_unread_emails()
    
    state["last_checked"] = datetime.now().isoformat()
    save_state(state)
    
    return emails


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: email_utils.py [check|send|list]")
        sys.exit(1)
    
    cmd = sys.argv[1]
    
    if cmd == "check":
        emails = check_new_emails()
        if emails:
            print(f"Found {len(emails)} unread email(s):")
            for e in emails:
                print(f"  - From: {e['from']}")
                print(f"    Subject: {e['subject']}")
                print(f"    Date: {e['date']}")
                print()
        else:
            print("No unread emails.")
    
    elif cmd == "list":
        emails = get_all_emails(limit=5)
        for e in emails:
            print(f"From: {e['from']}")
            print(f"Subject: {e['subject']}")
            print(f"Date: {e['date']}")
            print("-" * 40)
    
    elif cmd == "send":
        if len(sys.argv) < 5:
            print("Usage: email_utils.py send <to> <subject> <body>")
            sys.exit(1)
        to, subject, body = sys.argv[2], sys.argv[3], sys.argv[4]
        send_email(to, subject, body)
        print(f"Email sent to {to}")
