from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from zoneinfo import ZoneInfo
import csv
import time

CH_TZ = ZoneInfo("Europe/Zurich")

POOLS = {
    "city": {
        "url": "https://www.stadt-zuerich.ch/de/stadtleben/sport-und-erholung/sport-und-badeanlagen/hallenbaeder/city.html",
        "id": "SSD-4_visitornumber",
    },
    "blaesi": {
        "url": "https://www.stadt-zuerich.ch/de/stadtleben/sport-und-erholung/sport-und-badeanlagen/hallenbaeder/blaesi.html",
        "id": "SSD-2_visitornumber",
    },
    "oerlikon": {
        "url": "https://www.stadt-zuerich.ch/de/stadtleben/sport-und-erholung/sport-und-badeanlagen/hallenbaeder/oerlikon.html",
        "id": "SSD-7_visitornumber",
    }
}

# Chrome Options
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

def get_guest_count(url, element_id):
    try:
        driver.get(url)

        time.sleep(3)

        elem = driver.find_element(By.ID, element_id)
        return elem.text.strip()
    except Exception as e:
        print(f"Error scraping {url}:", e)
        return "NA"

results = {}
for name, info in POOLS.items():
    results[name] = get_guest_count(info["url"], info["id"])

driver.quit()

timestamp = datetime.now(CH_TZ).strftime("%Y-%m-%d %H:%M:%S")

# CSV append
with open("gaeste.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        timestamp,
        results["city"],
        results["blaesi"],
        results["oerlikon"]
    ])
