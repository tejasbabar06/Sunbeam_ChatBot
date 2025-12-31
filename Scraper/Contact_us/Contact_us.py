from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://sunbeaminfo.in/contact-us")

wait = WebDriverWait(driver, 15)

# Locate all contact info blocks
contact_blocks = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "div.contact_page_info div.col-md-4")
    )
)

with open("Contact_us.txt", "w", encoding="utf-8") as file:
    file.write("SUNBEAM CONTACT DETAILS\n")
    file.write("=" * 45 + "\n\n")

    for i, block in enumerate(contact_blocks, 1):
        try:
            text = block.find_element(By.CLASS_NAME, "text_box").text.strip()
            file.write(f"{i}. {text}\n\n")
        except:
            pass

driver.quit()
