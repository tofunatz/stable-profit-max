import time
from strategies.macd_confirm import check_macd_signal
from strategies.bbw_guard import check_bbw_signal
from strategies.hybrid_strategy import check_hybrid_signal
from modules.sheet_logger import log_simulated_trade
from modules.discord_notifier import notify_simulated_trade
from config import SYMBOLS, VERSION


def simulate_trade():
    print("\n🧪 Running simulated trade logic...")

    for symbol in SYMBOLS:
        print(f"\n📍 Symbol: {symbol}")

        # --- Run strategies ---
        macd = check_macd_signal(symbol)
        bbw = check_bbw_signal(symbol)
        hybrid = check_hybrid_signal(symbol)

        strategies = [
            ('MACD Confirm', macd),
            ('BBW Guard', bbw),
            ('Hybrid Strategy', hybrid)
        ]

        for strat_name, result in strategies:
            if result.get('signal'):
                print(f"✅ {strat_name} confirms entry for {symbol}")

                # Tag strategy
                result['strategy'] = strat_name

                # Log to Sheet
                log_simulated_trade(symbol, result, VERSION)

                # Notify to Discord
                notify_simulated_trade(symbol, result, VERSION)

                time.sleep(1)
            else:
                print(f"❌ {strat_name} no signal for {symbol}")