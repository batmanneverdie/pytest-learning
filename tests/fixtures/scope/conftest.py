import smtplib
import pytest


@pytest.fixture()
def smtp_connection():
    return smtplib.SMTP(host="smtp.163.com", port=25, timeout=5)
