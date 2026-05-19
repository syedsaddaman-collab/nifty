import os
import requests
from datetime import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

# --- MASTER FIX FOR ANDROID & PYTHON 3.11 ---
try:
    import certifi
    os.environ['SSL_CERT_FILE'] = certifi.where()
    # Ye line Android par naye Python versions ko crash hone se rokti hai
    os.environ['KIVY_NO_ARGS'] = '1'
except Exception as e:
    print(f"Initialization Fix Applied: {e}")

class SamPredictionV16(App):
    def build(self):
        self.title = "SAM PREDICTION v16.2"
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # State Variables
        self.last_signal = "READY"
        self.price_history = []
        self.monitoring = False

        # UI Setup
        self.status = Label(
            text="SAM PREDICTION v16.2\n[Initializing Tool...]",
            font_size='22sp',
            bold=True,
            halign='center',
            markup=True
        )

        self.signal_btn = Button(
            text="START LIVE MONITOR",
            size_hint_y=None,
            height='100dp',
            background_color=(0, 0.7, 0.3, 1),
            font_size='18sp',
            bold=True
        )
        self.signal_btn.bind(on_press=self.toggle_monitor)

        self.layout.add_widget(self.status)
        self.layout.add_widget(self.signal_btn)

        return self.layout

    def toggle_monitor(self, instance):
        if not self.monitoring:
            self.monitoring = True
            self.signal_btn.text = "STOP MONITORING"
            self.signal_btn.background_color = (0.7, 0, 0, 1)
            # 15 seconds ka interval taaki network block na ho
            Clock.schedule_interval(self.fetch_data, 15)
            self.status.text = "SAM PREDICTION v16.2\n[Status: Scanning Market...]"
        else:
            self.monitoring = False
            self.signal_btn.text = "START LIVE MONITOR"
            self.signal_btn.background_color = (0, 0.7, 0.3, 1)
            Clock.unschedule(self.fetch_data)
            self.status.text = "SAM PREDICTION v16.2\n[Status: Paused]"

    def fetch_data(self, dt):
        try:
            # Fake Browser User-Agent (Yahoo Fix)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            url = "https://query1.finance.yahoo.com/v8/finance/chart/^NSEI?interval=1m&range=1d"

            r = requests.get(url, headers=headers, timeout=10)

            if r.status_code != 200:
                self.status.text = f"Server Error: {r.status_code}\nRetrying..."
                return

            data = r.json()['chart']['result'][0]
            curr_p = float(data['meta']['regularMarketPrice'])

            # Logic: Smoothing (Average of last 10 ticks)
            self.price_history.append(curr_p)
            if len(self.price_history) > 10:
                self.price_history.pop(0)

            avg_price = sum(self.price_history) / len(self.price_history)

            # --- JACKPOT LOGIC (With 10 Point Stability Filter) ---
            if curr_p > (avg_price + 10):
                new_signal = "JACKPOT CALL"
                color = "00FF00" # Green
            elif curr_p < (avg_price - 10):
                new_signal = "JACKPOT PUT"
                color = "FF0000" # Red
            else:
                new_signal = "STABLE / NO SIGNAL"
                color = "FFFFFF" # White

            self.status.text = f"Nifty: {curr_p:.2f}\nSignal: [color={color}][b]{new_signal}[/b][/color]"

        except Exception as e:
            # Crash hone ke bajaye error screen par dikhayega
            self.status.text = f"Network Issue!\n{str(e)[:40]}"

if __name__ == "__main__":
    SamPredictionV16().run()