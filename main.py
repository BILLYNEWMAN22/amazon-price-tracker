import encodings.utf_8_sig
import smtplib


import requests
from bs4 import BeautifulSoup

# Change the Amazon URL to the copied address of another amazon product. 👇
URL = "https://www.amazon.co.uk/Hisense-50A6BGTUK-Virtual-Freeview-Bluetooth/dp/B09ZPVPHMV/" \
      "ref=sr_1_3?crid=Z5WERQV3VKOM&keywords=50+inch+tv&qid=1674232449&sprefix=50+inch+tv%2Caps%2C129&sr=8-3"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
              "image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
                  "537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Cookie": "PHPSESSID=980uqogvoc99kfi5v45ibaldm0; _ga=GA1.2.1885123969.1674056149; _gid=GA1.2.1472371917.1674056149",
}

response = requests.get(url=URL, headers=headers)
# response.raise_for_status()

soup = BeautifulSoup(response.content, "html.parser")
title = soup.find(id="productTitle").getText().strip()
price_whole = float(soup.find(class_="a-offscreen").getText().split("£")[1])
# price_decimal = int(soup.find(class_="a-price-fraction").getText())
# print(price_decimal)
whole = soup.find(class_="a-price-whole").getText().split(".")[0]
decimal_ = soup.find(class_="a-price-fraction").getText()
price = float(f"{whole}.{decimal_}")

# print(price)

message = f"{title}\n\nis at a great price \n\n@\n\n#{price}\n\nLink: {URL}"



amount = 0
# Change this around
#              👇or👇 to see the outcome.
if price_whole >= 100:
    amount += 1
    print('Please open the tab "Project" on the left hand pane and open the folder "Product_Outcome" 👍')
    with open(f"Product_Outcome/Outcome_{amount}.text", mode="w") as outcome:
        outcome.write(message)


