# sample_strategy.py (กลยุทธ์ทดสอบพร้อม Binance API)
from binance.client import Client
from config import API_KEY, SECRET_KEY
import pandas as pd

client = Client(API_KEY, SECRET_KEY)

def check_signal(symbol):
    try:
        klines = client.get_klines(symbol=symbol, interval=Client.KLINE_INTERVAL_1HOUR, limit=100)
        df = pd.DataFrame(klines, columns=[
            'timestamp', 'open', 'high', 'low', 'close', 'volume',
            'close_time', 'quote_asset_volume', 'number_of_trades',
            'taker_buy_base_vol', 'taker_buy_quote_vol', 'ignore'])

        df['close'] = pd.to_numeric(df['close'])

        if df['close'].iloc[-1] > df['close'].mean():
            return {
                'signal': True,
                'confidence': 80,
                'expected_value': 1.2,
                'strategy_score': 75,
                'signal_tag': 'Sample_Trigger',
                'risk_pct': 1.5,
                'trade_seq': f"SAMPLE-{symbol}",
                'market_regime': 'Neutral',
                'volume_spike': 'Normal',
                'atr_change': 'Low',
                'api_latency': 0.15,
                'execution_latency': 0.25,
                'slippage': 0.02,
                'exit_type': 'TP'
            }
        else:
            return {'signal': False}

    except Exception as e:
        print(f"[Sample Strategy Error] {e}")
        return {'signal': False}