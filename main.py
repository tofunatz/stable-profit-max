# ✅ FILE: main.py (v5.8.5_SIM_FULL - LOOP ENABLED)

from sim_engine import run_simulation
import schedule
import time

if __name__ == "__main__":
    print("🟢 Starting Stable-Profit-Max v5.8.5_SIM simulation loop...")

    # ✅ เรียกทำงานทุก 1 นาที
    schedule.every(1).minutes.do(run_simulation)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)

    except KeyboardInterrupt:
        print("🔴 Simulation manually stopped.")