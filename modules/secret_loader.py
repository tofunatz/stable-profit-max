# ✅ FILE: modules/secret_loader.py

import gspread
import os
from google.oauth2.service_account import Credentials

# 📌 ค่าคงที่
CREDENTIALS_FILE = 'credentials/credentials.json'
SHEET_NAME = 'Secret_Source'

# 📥 โหลดข้อมูลจาก Google Sheet
def load_secrets():
    try:
        scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
        credentials = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=scopes)
        client = gspread.authorize(credentials)

        spreadsheet_id = get_spreadsheet_id()
        sheet = client.open_by_key(spreadsheet_id).worksheet(SHEET_NAME)

        data = sheet.get_all_values()
        secrets = {}

        for row in data[1:]:  # ข้าม Header
            if len(row) >= 2:
                key = row[0].strip()
                value = row[1].strip()
                secrets[key] = value

        return secrets

    except Exception as e:
        print(f"[Secret Loader Error] {e}")
        return {}

# 📌 ใช้สำหรับเรียกค่ารายตัว เช่น API_KEY
def get_secret(key):
    secrets = load_secrets()
    return secrets.get(key)

# 📌 เรียก Spreadsheet ID จาก Sheet ได้โดยตรง
def get_spreadsheet_id():
    # ลองโหลดจาก ENV หรือ fallback จากไฟล์ (ถ้ามี)
    try:
        from config import SPREADSHEET_ID
        return SPREADSHEET_ID
    except:
        return os.getenv("SPREADSHEET_ID", "")