import network
import time

class WiFiManager:
    def __init__(self):
        self.station = network.WLAN(network.STA_IF)
        self.station.active(True)
        self.ap = network.WLAN(network.AP_IF)  # Access point for configuration
        self.ap.active(False)

    def connect(self, ssid, password):
        print("Connecting to Wi-Fi...")
        self.station.connect(ssid, password)

        for _ in range(10):  # Retry for 10 seconds
            if self.station.isconnected():
                print(f"Connected to {ssid}")
                print("Network configuration:", self.station.ifconfig())
                return True
            time.sleep(1)

        print("Failed to connect")
        return False

    def save_credentials(self, ssid, password):
        with open("wifi_config.txt", "w") as f:
            f.write(f"{ssid}\n{password}")
        print("Wi-Fi credentials saved")

    def load_credentials(self):
        try:
            with open("wifi_config.txt", "r") as f:
                creds = f.readlines()
                ssid = creds[0].strip()
                password = creds[1].strip()
                return ssid, password
        except (OSError, IndexError):
            return None, None

    def start(self):
        ssid, password = self.load_credentials()
        if ssid and password:
            print("Using saved credentials")
            if self.connect(ssid, password):
                return True

        print("Starting configuration mode")
        self.start_access_point()
        return False

    def start_access_point(self):
        ap_ssid = "Config_AP"
        ap_password = "12345678"
        self.ap.config(essid=ap_ssid, password=ap_password)
        self.ap.active(True)
        print(f"Access Point started: {ap_ssid}")
        print("Connect to this network and configure Wi-Fi credentials")

    def stop_access_point(self):
        if self.ap.active():
            self.ap.active(False)
            print("Access Point stopped")
