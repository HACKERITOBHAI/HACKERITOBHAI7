# === Banner Display ===
import pyfiglet

ascii_banner = pyfiglet.figlet_format("HACKERITOBHAI BOT")
print(ascii_banner)


import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
import random
import requests
import os

# Load proxies
proxy = None
if os.path.exists("proxies.txt"):
    with open("proxies.txt") as f:
        proxies = [p.strip() for p in f if p.strip()]
    # Pick and test one
    def is_proxy_working(proxy_url):
        try:
            r = requests.get("https://geonode.com/free-proxy-list", proxies={"http": proxy_url, "https": proxy_url}, timeout=5)
            return r.status_code == 200
        except:
            return False

    for _ in range(10):
        test_proxy = random.choice(proxies)
        if is_proxy_working(test_proxy):
            proxy = test_proxy
            break

if proxy:
    print(f"[OK] Using Proxy: {proxy}")
else:
    print("[WARNING] No working proxy found. Proceeding without proxy...")

# Chrome options
options = uc.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-extensions")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--start-maximized")
if proxy:
    options.add_argument(f"--proxy-server={proxy}")

driver = uc.Chrome(options=options)

# Open Gmail signup
driver.get("https://accounts.google.com/signup")

time.sleep(5)  # Wait for page to load (simplified)
print("[INFO] Gmail signup page opened.")

# NOTE: Form automation not implemented due to CAPTCHA & Google policy
input("[ACTION] Manually create Gmail account in the browser. Press Enter to close...")
driver.quit()
