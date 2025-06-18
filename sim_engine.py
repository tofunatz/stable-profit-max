# modules/sim_engine.py

import schedule
import time
from strategies.macd_confirm import check_macd_signal
from modules.sheet_writer import log_trade_execution
from modules.discord_notifier import notify_trade
from config import SYMBOLS, VERSION

def run_simulation():
    print(f"\n🟢 Sim Monitor Running | Version: {VERSION}")

    for symbol in SYMBOLS:
        print(f"\n🔍 Checking symbol: {symbol}")
        strategy = "MACD_Confirm"

        result = check_macd_signal(symbol)

        if result.get("signal"):
            status = "🟢 Signal Confirmed"
        else:
            status = "❌ MACD not confirmed"

        print(f"📤 Sending to Discord: {symbol} | {status}")
        notify_trade(symbol, result, VERSION)

        # ✅ เขียนลงชีต Google Sheet
        log_trade_execution(symbol, strategy, result, VERSION)

# ✅ Schedule ให้รันทุก 1 นาที
schedule.every(1).minutes.do(run_simulation)

if __name__ == "__main__":
    print("⏳ Starting Stable-Profit-Max v5.8.5_SIM simulation loop...")

    run_simulation()  # ✅ run ครั้งแรกทันที
    while True:
        schedule.run_pending()
        time.sleep(1)