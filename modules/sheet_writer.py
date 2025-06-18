# modules/sheet_writer.py

import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
from config import CREDENTIALS_FILE, SPREADSHEET_ID

def log_trade_execution(symbol, strategy, result, version):
    try:
        # ✅ เชื่อม Google Sheets
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
        client = gspread.authorize(credentials)

        # ✅ ระบุ worksheet ให้ถูกต้อง
        sheet = client.open_by_key(SPREADSHEET_ID).worksheet("Trade_Log_v2")

        # ✅ เตรียมข้อมูลลงชีต
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        row = [
            now,                                # Timestamp
            symbol,                             # Symbol
            "Market",                           # Entry Type
            "Long",                             # Direction
            "90",                               # Entry Confidence (fixed)
            str(result.get("confidence", 0)),   # Model Confidence (from result)
            strategy,                           # Strategy
            f"{version}_SIM_{symbol}",          # Order Tag / Signal ID
            "Simulated",                        # Real/Simulated
            "Yes",                              # Accepted
            "Moderate",                         # Risk Level
            "0",                                # SL %
            "0",                                # RR Ratio
            "0.01",                             # Trade Size
            "TP"                                # Exit Type (simulated TP)
        ]

        # ✅ เขียนเข้าแถวใหม่ในชีต
        sheet.append_row(row, value_input_option="USER_ENTERED")

    except Exception as e:
        print(f"[Sheet Write Error] {version} | {symbol} | {e}")