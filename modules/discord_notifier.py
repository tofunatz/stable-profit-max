# ✅ FILE: modules/discord_notifier.py
import requests
from datetime import datetime
from config import DISCORD_WEBHOOK_MONITOR, DISCORD_WEBHOOK_SIM, DISCORD_WEBHOOK_ERROR, VERSION

def notify_trade(symbol, result, version=VERSION):
    try:
        if isinstance(version, str) and version.startswith("v5.7"):
            webhook_url = DISCORD_WEBHOOK_MONITOR
        else:
            webhook_url = DISCORD_WEBHOOK_SIM

        embed = {
            "title": f"📢 Signal Detected: {symbol}",
            "color": 3447003,
            "fields": [
                {"name": "📌 Strategy", "value": result.get("signal_tag", "-"), "inline": True},
                {"name": "🔎 Confidence", "value": f"{result.get('confidence', 0)}%", "inline": True},
                {"name": "💰 Expected Value", "value": f"{result.get('expected_value', '-')}", "inline": True},
                {"name": "⚖️ Risk %", "value": f"{result.get('risk_pct', '-')}", "inline": True},
                {"name": "🌐 Regime", "value": result.get("market_regime", "-"), "inline": True},
                {"name": "📊 Volume Spike", "value": result.get("volume_spike", "-"), "inline": True},
                {"name": "📉 ATR Change", "value": result.get("atr_change", "-"), "inline": True},
                {"name": "📤 Exit type", "value": result.get("exit_type", "-"), "inline": True},
                {"name": "📌 Version", "value": version, "inline": False},
            ]
        }

        payload = {"embeds": [embed]}
        response = requests.post(webhook_url, json=payload)

        if response.status_code != 204:
            print(f"[Discord Warn] Status {response.status_code} :: {response.text}")

    except Exception as e:
        print(f"[notify_trade ERROR] {e}")