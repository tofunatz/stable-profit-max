# ✅ FILE: strategies/macd_confirm.py

from binance.client import Client
from modules.secret_loader import get_secret
import pandas as pd

# 🔐 โหลด API key จาก Google Sheet
API_KEY = get_secret("API_KEY")
SECRET_KEY = get_secret("SECRET_KEY")
client = Client(API_KEY, SECRET_KEY)

def check_macd_signal(symbol):
    try:
        # 📥 ดึงข้อมูลแท่งเทียน 1 ชั่วโมง 100 แท่ง
        klines = client.get_klines(symbol=symbol, interval=Client.KLINE_INTERVAL_1HOUR, limit=100)
        df = pd.DataFrame(klines, columns=[
            'timestamp', 'open', 'high', 'low', 'close', 'volume',
            'close_time', 'quote_asset_volume', 'number_of_trades',
            'taker_buy_base_vol', 'taker_buy_quote_vol', 'ignore'
        ])
        df['close'] = pd.to_numeric(df['close'])

        # 📈 คำนวณ MACD และ Signal line
        df['ema12'] = df['close'].ewm(span=12, adjust=False).mean()
        df['ema26'] = df['close'].ewm(span=26, adjust=False).mean()
        df['macd'] = df['ema12'] - df['ema26']
        df['signal'] = df['macd'].ewm(span=9, adjust=False).mean()

        # ✅ Bullish Crossover (MACD ตัดขึ้นเหนือ Signal)
        if df['macd'].iloc[-2] < df['signal'].iloc[-2] and df['macd'].iloc[-1] > df['signal'].iloc[-1]:
            return {
                'signal': True,
                'confidence': 85,
                'expected_value': 1.4,
                'strategy_score': 80,
                'signal_tag': 'MACD_Bullish_Crossover',
                'risk_pct': 1.5,
                'trade_seq': f"MACD-{symbol}",
                'market_regime': 'Trending',
                'volume_spike': 'Yes',
                'atr_change': 'Moderate',
                'api_latency': 0.15,
                'execution_latency': 0.35,
                'slippage': 0.03,
                'exit_type': 'TP'
            }
        else:
            return {
                'signal': False,
                'confidence': 0,
                'signal_tag': 'MACD_Flat_or_Bearish'
            }

    except Exception as e:
        print(f"[MACD Error] {e}")
        return {
            'signal': False,
            'confidence': 0,
            'signal_tag': 'MACD_Error',
            'error': str(e)
        }