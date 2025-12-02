import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

URL = "https://www.stadt-zuerich.ch/de/stadtleben/sport-und-erholung/sport-und-badeanlagen/hallenbaeder/city.html"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# Die Gästezahl steht im HTML als Element mit der Klasse "pool-status__value"
value = soup.select_one(".pool-status__value")
guests = value.get_text(strip=True) if value else "NA"

timestamp = datetime.now().isoformat(timespec="minutes")

# CSV anhängen
with open("gaeste.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([timestamp, guests])
