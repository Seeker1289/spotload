from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

playlist_url = input("Enter Spotify playlist URL: ")

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.get(playlist_url)

wait = WebDriverWait(driver, 20)

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="playlist-tracklist"]')))

scrollable = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="playlist-tracklist"]')

collected_links = set()
prev_total = 0
same_rounds = 0

while True:
    # Extract CURRENT visible tracks
    new_links = driver.execute_script("""
        let anchors = document.querySelectorAll('a[href*="/track/"]');
        return Array.from(anchors).map(a => a.href.split("?")[0]);
    """)

    for link in new_links:
        collected_links.add(link)

    print(f"Collected so far: {len(collected_links)}")

    # Scroll a bit (NOT full jump)
    driver.execute_script("""
        arguments[0].scrollTop += arguments[0].offsetHeight;
    """, scrollable)

    time.sleep(1.5)

    # Stop condition
    if len(collected_links) == prev_total:
        same_rounds += 1
    else:
        same_rounds = 0

    if same_rounds >= 6:
        break

    prev_total = len(collected_links)

# Save
with open("links.txt", "w", encoding="utf-8") as f:
    for link in sorted(collected_links):
        f.write(link + "\n")

print(f"\nSaved {len(collected_links)} tracks")

driver.quit()
