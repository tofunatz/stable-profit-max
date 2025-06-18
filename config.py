# ✅ FILE: config.py (v5.8.5_SIM_FULL - HARD CODED VERSION)

# ✅ Binance API
API_KEY = 'cq0GU9TVBWHPpD6VX21uu8HMOyCyn3OLCovAmGw5HvQwZeipskM9bi6b4dZOkrN0'
SECRET_KEY = 'MHM1ZuBs90aABLuor1enBMy8FAxEATeVGxsxO5qxMFbnJ0vRolNKNfIGeoEOjPEv'

# ✅ Discord Webhook URLs
DISCORD_WEBHOOK_MONITOR = 'https://discord.com/api/webhooks/1382711004965900378/d1_pWWsG5o_LDsh4wVHHGbxASZQMv6NaJOb24QRAqwZAta1KJ3G0i6XCKYk0ifDC6Wb9'  # <- แก้ตามจริง
DISCORD_WEBHOOK_SIM = 'https://discord.com/api/webhooks/1384206649631313961/o95GJCIOk8f4hBfcrn6LRR7p6dXBrL2sa4KuE5mMaHoyD2sjsK46sRfgQbkZK7cY2dPB'          # <- แก้ตามจริง
DISCORD_WEBHOOK_ERROR = 'https://discord.com/api/webhooks/1384206773531181126/a86z9LrC-OuivdDzKAcds20eXV_hUOOm5zn7IaFZM31hSCQb2pNp6nfDJ2xMYq0KJCbJ'      # <- แก้ตามจริง

# ✅ Google Sheets Config
CREDENTIALS_FILE = 'credentials/credentials.json'
SPREADSHEET_ID = '1YJ8jVjs05ruzC47udGuAmloCXrcXmFBMNR92C24EwWw'

# ✅ Core Trading Config
SYMBOLS = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'SOLUSDT']
VERSION = 'v5.8.5_SIM'
REGION_TAG = 'Asia'

# ✅ Strategy Settings
ENABLE_SESSION_FILTER = True
USE_DYNAMIC_SYMBOLS = True
STRATEGY_MODE = 'MACD_Confirm'
USE_STRATEGY_SWITCH = True

# ✅ Risk & Filters
ML_SELECTOR = False
MIN_CONFIDENCE = 70
MAX_RISK_PER_TRADE = 1.5
MAX_DRAWDOWN_DAILY = 5
MAX_CONCURRENT_TRADES = 2