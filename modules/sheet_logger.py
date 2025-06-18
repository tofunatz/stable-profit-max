# ✅ FILE: modules/sheet_logger.py (สำหรับ v5.8.5_SIM)

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from secret_loader import get_secret

# โหลดข้อมูลลับจาก Google Sheet
SPREADSHEET_ID = get_secret('SPREADSHEET_ID')
CREDENTIALS_FILE = get_secret('CREDENTIALS_FILE')

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
client = gspread.authorize(creds)
sheet = client.open_by_key(SPREADSHEET_ID)

def log_simulated_trade(symbol, result, version):
    try:
        worksheet = sheet.worksheet("Trade_Log_v2")

        now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        row = [
            now,
            symbol,
            result.get("signal_tag", ""),
            version,
            result.get("confidence", ""),
            result.get("expected_value", ""),
            result.get("strategy_score", ""),
            result.get("market_regime", ""),
            result.get("volume_spike", ""),
            result.get("atr_change", ""),
            result.get("risk_pct", ""),
            result.get("exit_type", ""),
            result.get("slippage", ""),
            result.get("trade_seq", ""),
        ]

        worksheet.append_row(row)
        print("📗 Sheet updated for", symbol)

    except Exception as e:
        print(f"❌ Error logging to sheet: {e}")