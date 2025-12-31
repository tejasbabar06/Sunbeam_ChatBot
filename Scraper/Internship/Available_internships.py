from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless=new")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.sunbeaminfo.in/internship")
print("Title:", driver.title)

driver.implicitly_wait(5)

toggle = driver.find_element(By.XPATH, "//a[@href='#collapseSix']")
driver.execute_script("arguments[0].click();", toggle)
time.sleep(1)

table = driver.find_element(By.XPATH, "//div[@id='collapseSix']//table")

rows = table.find_elements(By.TAG_NAME, "tr")

with open("Available_internships.txt", "w", encoding="utf-8") as f:
    f.write("Available_internships")
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        if cols:
            line = " | ".join(col.text.strip() for col in cols)
            print(line)
            f.write(line + "\n")

print("Data scraped successfully")

driver.quit()
