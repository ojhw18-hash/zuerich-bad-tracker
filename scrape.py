from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv
from datetime import datetime
import time

URL = "https://www.stadt-zuerich.ch/de/stadtleben/sport-und-erholung/sport-und-badeanlagen/hallenbaeder/city.html"

# Headless Chrome konfigurieren
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

try:
    driver.get(URL)

    # kleine Wartezeit für JS-Daten
    time.sleep(3)

    # Gästezahl aus <td> mit ID "SSD-4_visitornumer" finden
    element = driver.find_element(By.ID, "SSD-4_visitornumber")
    guests = element.text.strip()

except Exception as e:
    guests = "NA"
    print("Fehler beim Scraping:", e)

finally:
    driver.quit()

timestamp = datetime.now().isoformat(timespec="minutes")

# CSV anfügen
with open("gaeste.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([timestamp, guests])
