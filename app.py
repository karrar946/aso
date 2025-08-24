import socket
import ssl
import smtplib
import logging

logging.basicConfig(level=logging.INFO)
try:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context, timeout=30) as server:
        logging.info("نجاح الاتصال بـ smtp.gmail.com:465")
except Exception as e:
    logging.error(f"فشل الاتصال بـ smtp.gmail.com:465: {e}")
